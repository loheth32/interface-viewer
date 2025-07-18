import psutil

print("📡 Network Interface Viewer\n")

interfaces = psutil.net_if_addrs()
stats = psutil.net_if_stats()

for iface_name, addr_list in interfaces.items():
    print(f"🔌 Interface: {iface_name}")

    if iface_name in stats:
        stat = stats[iface_name]
        print(f"  🔄 Status       : {'UP' if stat.isup else 'DOWN'}")
        print(f"  ↕️  Duplex       : {stat.duplex}  (0=Unknown, 1=Half, 2=Full)")
        print(f"  🚀 Speed        : {stat.speed} Mbps")
        print(f"  📦 MTU          : {stat.mtu}")

    for addr in addr_list:
        if addr.family.name == 'AF_INET':
            print(f"  🌐 IPv4 Address : {addr.address}")
            print(f"  🧾 Netmask      : {addr.netmask}")
            print(f"  📢 Broadcast IP : {addr.broadcast}")
        elif addr.family.name == 'AF_INET6':
            print(f"  🧬 IPv6 Address : {addr.address}")
            print(f"  🧾 Netmask      : {addr.netmask}")
        elif addr.family.name == 'AF_LINK':
            print(f"  🔗 MAC Address  : {addr.address}")
            print(f"  📢 Broadcast MAC: {addr.broadcast}")
    
    print("-" * 60)
