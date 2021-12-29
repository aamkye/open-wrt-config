# OpenWRT config via ansible

## Repos
- https://downloads.openwrt.org/releases/21.02.0/targets/mvebu/cortexa9/packages/
- https://downloads.openwrt.org/releases/packages-21.02/arm_cortex-a9_vfpv3-d16/packages/
- https://downloads.openwrt.org/releases/packages-21.02/arm_cortex-a9_vfpv3-d16/base/
- https://openwrt.org/packages/pkgdata/

## Commands

```bash
opkg upgrade $(opkg list-upgradable | awk '{ print $1 }')

uci show dropbear; ls -l /etc/dropbear; cat /etc/dropbear/authorized_keys

while uci -q delete dhcp.@dnsmasq[0]; do :; done
```

## Restarts:

### Soft reset
* `firstboot -y && reboot now`

### Hard reset
* `umount /overlay && jffs2reset && reboot now`

## Types:

### Managed:

```yaml
<type>:
  - __type: <type>
    __name: <name>
    __fields:
      field1: 1
      field2: 0
  - __type: <type>
    __name: <name>
    __fields:
      field1: 2
      field2: 5
```

### Un-managed:

```yaml
<type>:
  - __type: <type>
    __fields:
      field1: 1
      field2: 0
  - __type: <type>
    __fields:
      field1: 2
      field2: 5
```
