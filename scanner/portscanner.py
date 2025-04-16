# scanner/portscanner.py

import socket
from datetime import datetime

# Optional: Boleh pindah ke utils/constants.py kalau banyak
PORT_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 3389: "RDP"
}

COMMON_PORTS = list(PORT_SERVICES.keys())

def run_port_scan(target: str, full_scan: bool = False):
    """Scan selected ports on a target IP address."""
    ports = range(1, 1025) if full_scan else COMMON_PORTS
    open_ports = []

    print(f"\n[+] Scanning ports on {target}...\n")

    # Try resolve hostname
    try:
        hostname = socket.gethostbyaddr(target)[0]
        print(f"[INFO] Hostname: {hostname}")
    except:
        print("[INFO] Hostname: Not found")

    start_time = datetime.now()

    for index, port in enumerate(ports, start=1):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            service = PORT_SERVICES.get(port, "Unknown")

            if result == 0:
                print(f"[OPEN] Port {port} ({service})")
                open_ports.append((port, service))

            sock.close()
            print(f"Scanning port {port} ({index}/{len(ports)})", end='\r')

        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            break
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\n[✓] Scan completed in {duration}")

    if open_ports:
        with open("scan_result.txt", "w") as f:
            f.write(f"Scan results for {target} ({datetime.now()})\n")
            for port, service in open_ports:
                f.write(f"OPEN: Port {port} ({service})\n")
        print("[✓] Results saved to scan_result.txt")
    else:
        print("[i] No open ports found.")
