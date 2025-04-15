import socket

def run_port_scan():
    target = input("Enter target IP address: ")
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]  # Popular ports

    print(f"\n[+] Scanning ports on {target}...\n")

    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            sock.close()
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            break
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")
