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
```
