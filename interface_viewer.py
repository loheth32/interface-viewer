#!/usr/bin/env python3

import psutil
import datetime
import os

# 📂 Create a 'logs' directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 📅 Generate timestamped log file
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"interface_log_{timestamp}.txt")

# 📝 Open log file for writing
with open(log_file, "w") as log:
    def logprint(msg):
        print(msg)
        log.write(msg + "\n")

    # 🛰️ Header
    logprint("📡 Interface Viewer Tool")
    logprint(f"🕒 Time: {timestamp}")
    logprint("=" * 60)

    # 🔍 Get interfaces and stats
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    # 🔁 Loop through each interface
    for iface_name, addr_list in interfaces.items():
        logprint(f"\n🔌 Interface: {iface_name}")

        # 📊 Show status if available
        if iface_name in stats:
            stat = stats[iface_name]
            logprint(f"  🔄 Status       : {'UP' if stat.isup else 'DOWN'}")
            logprint(f"  ↕️  Duplex       : {stat.duplex}  (0=Unknown, 1=Half, 2=Full)")
            logprint(f"  🚀 Speed        : {stat.speed} Mbps")
            logprint(f"  📦 MTU          : {stat.mtu}")

        # 🌐 Show IP/MAC details
        for addr in addr_list:
            if addr.family.name == 'AF_INET':
                logprint(f"  🌐 IPv4 Address : {addr.address}")
                logprint(f"  🧾 Netmask      : {addr.netmask}")
                logprint(f"  📢 Broadcast IP : {addr.broadcast}")
            elif addr.family.name == 'AF_INET6':
                logprint(f"  🧬 IPv6 Address : {addr.address}")
            elif addr.family.name == 'AF_LINK':
                logprint(f"  🔗 MAC Address  : {addr.address}")
                logprint(f"  📢 Broadcast MAC: {addr.broadcast}")

        logprint("-" * 60)
