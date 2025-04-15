import socket

def run_rdp_check():
    target = input("Enter target IP address: ")

    print(f"\n[+] Checking RDP port (3389) on {target}...\n")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Timeout after 2 seconds
        result = sock.connect_ex((target, 3389))  # Connect to port 3389

        if result == 0:
            print(f"[OPEN] RDP port (3389) is open on {target}.")
        else:
            print(f"[CLOSED] RDP port (3389) is closed on {target}.")
        
        sock.close()
    except socket.error as err:
        print(f"[!] Error connecting to {target}: {err}")
