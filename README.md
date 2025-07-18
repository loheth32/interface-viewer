# 📡 Interface Viewer Tool

A Python-based CLI tool that displays detailed information about your system's network interfaces, including status, speed, duplex mode, MTU, IP addresses, and MAC addresses. It also logs all output to a timestamped `.txt` file for future analysis.

---

## 🔧 Features

- ✅ Lists all network interfaces (e.g., `eth0`, `wlan0`, `lo`)
- ✅ Displays:
  - Interface status (UP/DOWN)
  - Duplex mode (Full/Half)
  - Speed (in Mbps)
  - MTU (Maximum Transmission Unit)
  - IPv4 and IPv6 addresses
  - MAC address and broadcast info
- ✅ Saves detailed logs to `logs/` folder with timestamps

---

## 📦 Dependencies

- Python 3.x
- `psutil` (install via pip)

```bash
pip install psutil
