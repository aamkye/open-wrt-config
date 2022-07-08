```bash
/var/prometheus/adblock.prom
/var/prometheus/opkg.prom
```

```bash
> /etc/init.d/adblock status
::: adblock runtime information
  + adblock_status  : enabled
  + adblock_version : 4.1.3
  + blocked_domains : 492953
  + active_sources  : adaway, adguard, adguard_tracking, android_tracking, disconnect, oisd_full, openphish, phishing_ar
                      my, spam404, stopforumspam, wally3k, whocares, winhelp, winspy, yoyo
  + dns_backend     : unbound (unbound-control), /var/lib/unbound
  + run_utils       : download: /bin/uclient-fetch, sort: /usr/libexec/sort-coreutils, awk: /bin/busybox
  + run_ifaces      : trigger: wan, report: lan
  + run_directories : base: /tmp, backup: /tmp/adblock-Backup, report: /tmp/adblock-Report, jail: /tmp
  + run_flags       : backup: ✔, flush: ✔, force: ✔, search: ✘, report: ✔, mail: ✘, jail: ✘
  + last_run        : start, 1m 17s, 509/282/267, 2022-07-05T21:01:29+00:00
  + system          : Linksys WRT3200ACM, OpenWrt 21.02.0 r16279-5cc0535800
```

```bash
> /etc/init.d/adblock list
::: Available adblock sources
:::
    Name                 Enabled   Size   Focus                Info URL
    -------------------------------------------------------------------
  + adaway               x         S      mobile               https://github.com/AdAway/adaway.github.io
  + adguard              x         L      general              https://adguard.com
  + adguard_tracking     x         S      tracking             https://github.com/AdguardTeam/cname-trackers
  + android_tracking     x         S      tracking             https://github.com/Perflyst/PiHoleBlocklist
  + andryou                        L      compilation          https://gitlab.com/andryou/block/-/blob/master/rea
  + anti_ad                        L      compilation          https://github.com/privacy-protection-tools/anti-A
  + anudeep                        M      compilation          https://github.com/anudeepND/blacklist
  + bitcoin                        S      mining               https://github.com/hoshsadiq/adblock-nocoin-list
  + disconnect           x         S      general              https://disconnect.me
  + energized                      VAR    compilation          https://energized.pro
  + firetv_tracking                S      tracking             https://github.com/Perflyst/PiHoleBlocklist
  + games_tracking                 S      tracking             https://www.gameindustry.eu
  + hblock                         XL     compilation          https://hblock.molinero.dev
  + notracking                     XL     tracking             https://github.com/notracking/hosts-blocklists
  + oisd_basic                     L      general              https://oisd.nl
  + oisd_nsfw                      XL     general              https://oisd.nl
  + oisd_full            x         XXL    general              https://oisd.nl
  + openphish            x         S      phishing             https://openphish.com
  + phishing_army        x         S      phishing             https://phishing.army
  + reg_cn                         M      reg_china            https://easylist.to
  + reg_cz                         M      reg_czech+slovak     https://easylist.to
  + reg_de                         M      reg_germany          https://easylist.to
  + reg_es                         M      reg_spain            https://easylist.to
  + reg_fi                         S      reg_finland          https://github.com/finnish-easylist-addition
  + reg_fr                         M      reg_france           https://forums.lanik.us/viewforum.php?f=91
  + reg_id                         M      reg_indonesia        https://easylist.to
  + reg_it                         M      reg_italy            https://easylist.to
  + reg_kr                         S      reg_korea            https://github.com/List-KR/List-KR
  + reg_nl                         M      reg_netherlands      https://easylist.to
  + reg_pl1                        S      reg_poland           https://kadantiscam.netlify.app
  + reg_pl2                        S      reg_poland           https://www.certyficate.it
  + reg_ro                         M      reg_romania          https://easylist.to
  + reg_se                         s      reg_sweden           https://github.com/lassekongo83/Frellwits-filter-l
  + reg_ru                         M      reg_russia           https://easylist.to
  + reg_vn                         S      reg_vietnam          https://bigdargon.github.io/hostsVN
  + smarttv_tracking               S      tracking             https://github.com/Perflyst/PiHoleBlocklist
  + spam404              x         S      general              https://github.com/Dawsey21
  + stevenblack                    VAR    compilation          https://github.com/StevenBlack/hosts
  + stopforumspam        x         S      spam                 https://www.stopforumspam.com
  + utcapitole                     VAR    general              https://dsi.ut-capitole.fr/blacklists/index_en.php
  + wally3k              x         S      compilation          https://firebog.net/about
  + whocares             x         M      general              https://someonewhocares.org
  + winhelp              x         S      general              https://winhelp2002.mvps.org
  + winspy               x         S      win_telemetry        https://github.com/crazy-max/WindowsSpyBlocker
  + yoyo                 x         S      general              https://pgl.yoyo.org/as
    ---------------------------------------------------------------------------
  * Configured shallalist categories: -
  * Configured utcapitole categories: -
  * Configured energized variants: -
  * Configured stevenblack variants: -
    ---------------------------------------------------------------------------
    Sources without valid configuration
    ---------------------------------------------------------------------------
  - stalkerware
```

```bash
> /etc/init.d/adblock report
:::
::: Adblock DNS-Query Report
:::
  + Start    ::: 2022-07-08, 04:02:48
  + End      ::: 2022-07-08, 10:38:58
  + Total    ::: 9440
  + Blocked  ::: 2544 (26.95%)
:::
::: Top 10 Clients
:::
  + 4574     ::: 10.255.0.4
  + 1560     ::: 10.255.0.226
  + 1171     ::: 10.255.0.100
  + 951      ::: 10.255.0.158
  + 714      ::: 10.255.0.176
  + 466      ::: 10.255.0.10
  + 2        ::: 10.255.0.236
  + 2        ::: 10.255.0.2
:::
::: Top 10 Domains
:::
  + 199      ::: ews.mail.eu-west-1.awsapps.com
  + 193      ::: ssl.gstatic.com
  + 191      ::: outlook.ha.office365.com
  + 187      ::: CDG-efz.ms-acdc.office.com
  + 178      ::: signaler-pa.clients6.google.com
  + 128      ::: www.messenger.com
  + 110      ::: www.msftconnecttest.com
  + 104      ::: dns1.cscdns.net
  + 98       ::: star.fallback.c10r.facebook.com
:::
::: Top 10 Blocked Domains
:::
  + 126      ::: ssl.google-analytics.com
  + 90       ::: firebase-settings.crashlytics.com
  + 78       ::: browser.pipe.aria.microsoft.com
  + 68       ::: browser.pipe.aria.microsoft.com.dc0.ak95.io
  + 57       ::: alb.reddit.com
  + 55       ::: alb.reddit.com.dc0.ak95.io
  + 51       ::: smart-widget-assets.ekomiapps.de.dc0.ak95.io
  + 51       ::: smart-widget-assets.ekomiapps.de
  + 48       ::: device-api.asnapieu.com
:::
::: Latest DNS Queries
:::
Date           Time           Client                                       Domain                                                                          Answer
2022-07-08     10:38:58       10.255.0.4                                   signaler-pa.clients6.google.com                                                 OK
2022-07-08     10:38:52       10.255.0.226                                 ssl.google-analytics.com                                                        NX
```
