import os
from utils.banner import print_banner

def main_menu():
    os.system("clear")  # Guna 'cls' kalau Windows
    print_banner()
    print("Select option:")
    print("1. Port Scanning")
    print("2. Service Version & CVE")
    print("3. RDP Checking\n")

    choice = input("Insert Input: ")

    if choice == '1':
        from scanner.portscanner import run_port_scan
        run_port_scan()
    elif choice == '2':
        from scanner.versioncve import run_version_cve_check
        run_version_cve_check()
    elif choice == '3':
        from scanner.rdpchecker import run_rdp_check
        run_rdp_check()
    else:
        print("\n[!] Invalid Option")

if __name__ == "__main__":
    main_menu()
