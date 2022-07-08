#!/usr/bin/env python3

import subprocess
import re

class adblock_status:
    def __init__(self):
        self.get_adblock_status()

    status = ""
    version = ""
    dns_backend = ""
    system = ""
    hardware = ""
    run_flags = []

    def adblock_status(self, line):
        self.status = line.split(":")[1].strip()

    def adblock_version(self, line):
        self.version = line.split(":")[1].strip()

    def adblock_blocked_domains(self, line):
        m = line.split(":")[1].strip()
        print('# HELP node_adblock_status_blocked_domains Adblock blocked domains.')
        print('# TYPE node_adblock_status_blocked_domains gauge')
        print('node_adblock_status_blocked_domains {0}'.format(m))
        print("")

    def adblock_dns_backend(self, line):
        self.dns_backend = line.split(":")[1].strip().split(",")[0].strip()

    def adblock_run_flags(self, line):
        print('# HELP node_adblock_status_run_flags Adblock run flags.')
        print('# TYPE node_adblock_status_run_flags gauge')
        ### HERE
        for x in ":".join(line.split(":")[1:]).split(","):
            print('node_adblock_status_run_flags{{type="{0}"}} {1}'.format(x.split(":")[0].strip(), 1 if x.split(":")[1].strip() == "✔" else 0))
        print("")

    def adblock_system(self, line):
        self.system = line.split(":")[1].split(",")[1].strip()
        self.hardware = line.split(":")[1].split(",")[0].strip()

    def compose_adblock_status(self):
        print('# HELP node_adblock_status Adblock internal status.')
        print('# TYPE node_adblock_status gauge')
        print('node_adblock_status{{status="{0}", version="{1}", dns_backend="{2}", system="{3}", hardware="{4}"}} 1'.format(self.status, self.version, self.dns_backend, self.system, self.hardware))
        print("")

    def get_adblock_status(self):
        p = subprocess.Popen(["/etc/init.d/adblock", "status"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        (stdout, stderr) = p.communicate()
        print('# HELP node_adblock_status_return_status Adblock return code.')
        print('# TYPE node_adblock_status_return_status gauge')

        if p.returncode == 0:
            print('node_adblock_status_return_status 0')
            print("")
        else:
            print(f'node_adblock_status_return_status {p.returncode}')
            print("")
            exit(0)

        for line in stdout.decode().split("\n"):
            if "+ adblock_status" in line:
                self.adblock_status(line)
            elif "+ adblock_version" in line:
                self.adblock_version(line)
            elif "+ blocked_domains" in line:
                self.adblock_blocked_domains(line)
            elif "+ dns_backend" in line:
                self.adblock_dns_backend(line)
            elif "+ run_flags" in line:
                self.adblock_run_flags(line)
            elif "+ system" in line:
                self.adblock_system(line)

        self.compose_adblock_status()

class adblock_list:
    def __init__(self):
        self.get_adblock_list()

    printed_available_adblock_sources_info = 0
    printed_sources_without_valid_configuration_info = 0

    def print_available_adblock_sources_info(self):
        if not self.printed_available_adblock_sources_info:
            print('# HELP node_adblock_available_sources Adblock available sources.')
            print('# TYPE node_adblock_available_sources gauge')
            self.printed_available_adblock_sources_info = 1

    def print_sources_without_valid_configuration_info(self):
        if not self.printed_sources_without_valid_configuration_info:
            print("")
            print('# HELP node_adblock_sources_without_valid_configuration Adblock invalid config source.')
            print('# TYPE node_adblock_sources_without_valid_configuration gauge')
            self.printed_sources_without_valid_configuration_info = 1

    def available_adblock_sources(self, line):
        self.print_available_adblock_sources_info()
        source = re.split(r'\s{2,}', line.split("  + ")[1].strip())
        if len(source) == 5:
            print('node_adblock_available_sources{{name="{0}", size="{1}", focus="{2}", url="{3}"}} 1'.format(source[0], source[2], source[3], source[4]))
        else:
            print('node_adblock_available_sources{{name="{0}", size="{1}", focus="{2}", url="{3}"}} 0'.format(source[0], source[1], source[2], source[3]))

    def sources_without_valid_configuration(self, line):
        self.print_sources_without_valid_configuration_info()
        source = re.split(r'\s{2,}', line.split("  - ")[1].strip())
        print('node_adblock_sources_without_valid_configuration{{name="{0}"}} 1'.format(source[0]))

    def get_adblock_list(self):
        p = subprocess.Popen(["/etc/init.d/adblock", "list"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        (stdout, stderr) = p.communicate()
        print('# HELP node_adblock_list_return_status Adblock return code.')
        print('# TYPE node_adblock_list_return_status gauge')

        if p.returncode == 0:
            print('node_adblock_list_return_status 0')
            print("")
        else:
            print(f'node_adblock_list_return_status {p.returncode}')
            print("")
            exit(0)

        for line in stdout.decode().split("\n"):
            if "  + " in line:
                self.available_adblock_sources(line)
            elif "  - " in line:
                self.sources_without_valid_configuration(line)

def main():
    adblock_status()
    adblock_list()
    adblock_report()

if __name__ == '__main__':
    main()
