#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import subprocess

class opkg_upgrade_pending():
    def __init__(self):
        # https://regex101.com/r/vjPcHs/1
        self.opkg_list_re = re.compile(r'^([\S]+)+[\s\-]+([\S]+)[\s\-]+([\S]+)$')
        self.non_proccessable = 0
        self.get_opkg_upgradable_list()
        self.print_non_proccessable()

    def get_opkg_upgradable_list(self):
        p = subprocess.Popen(["opkg", "list-upgradable"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        (stdout, stderr) = p.communicate()
        print('# HELP node_opkg_return_status OPKG return code.')
        print('# TYPE node_opkg_return_status gauge')

        if p.returncode == 0:
            print('node_opkg_return_status 0')
            print("")
        else:
            print(f'node_opkg_return_status {p.returncode}')
            exit(0)

        print('# HELP node_opkg_upgrade_pending Opkg package pending updates by origin.')
        print('# TYPE node_opkg_upgrade_pending gauge')
        for line in stdout.decode().split("\n"):
            m = re.search(self.opkg_list_re, str(line))
            if not m:
                self.non_proccessable += 1
            else:
                print('node_opkg_upgrade_pending{{package_name="{0}", current_version="{1}" ,new_version="{2}"}} 1'.format(m.group(1), m.group(2), m.group(3)))
        if len(stdout) == 0:
            print('node_opkg_upgrade_pending{{package_name="",new_version="",origin="",arch="", security=""}} 0')
        print("")

    def print_non_proccessable(self):
        print('# HELP node_opkg_upgrade_non_processable Not procesable lines.')
        print('# TYPE node_opkg_upgrade_non_processable gauge')
        print(f'node_opkg_upgrade_non_processable {self.non_proccessable}')
        print("")

def main():
    opkg_upgrade_pending()

if __name__ == '__main__':
    main()
