import socket
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Dummy:  # fallback if colorama not installed
        def __getattr__(self, _): return ''
    Fore = Style = Dummy()

PORT_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS",
    143: "IMAP", 443: "HTTPS", 445: "SMB", 3389: "RDP"
}

COMMON_PORTS = list(PORT_SERVICES.keys())

def run_port_scan(target: str, full_scan: bool = False):
    ports = range(1, 1025) if full_scan else COMMON_PORTS
    open_ports = []

    print(f"\n[+] Scanning ports on {target}...\n")

    try:
        hostname = socket.gethostbyaddr(target)[0]
        print(f"[INFO] Hostname: {hostname}")
    except:
        print("[INFO] Hostname: Not found")

    print("\n" + "="*40)
    print(f"{'PORT':<8} | {'STATUS':<10} | SERVICE")
    print("-"*40)

    start_time = datetime.now()

    for index, port in enumerate(ports, start=1):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            service = PORT_SERVICES.get(port, "Unknown")

            if result == 0:
                status = Fore.GREEN + "OPEN" + Style.RESET_ALL
                print(f"{port:<8} | {status:<10} | {service}")
                open_ports.append((port, service))

            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            break
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")

    end_time = datetime.now()
    print("="*40)
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
