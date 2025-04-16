import os
from utils.banner import print_banner  # Make sure filename is banners.py

def main_menu():
    while True:
        os.system("clear")  # Guna 'cls' kalau Windows
        print_banner()
        print("Select option:")
        print("1. Port Scanning")
        print("2. Service Version & CVE")
        print("3. RDP Checking")
        print("4. Exit\n")

        choice = input("Insert Input: ")

        if choice == '1':
            from scanner.portscanner import run_port_scan

            target = input("Enter target IP address: ")
            print("\n1. Scan common ports [1]")
            print("2. Scan full range [2]")
            scan_type = input("Choose [1] or [2]: ")
            full_scan = scan_type == "2"

            run_port_scan(target, full_scan)

        elif choice == '2':
            from scanner.versioncve import run_version_cve_check
            run_version_cve_check()

        elif choice == '3':
            from scanner.rdpchecker import run_rdp_check
            run_rdp_check()

        elif choice == '4':
            print("\n[!] Exiting... Goodbye!")
            break

        else:
            print("\n[!] Invalid Option, please try again!")

        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main_menu()
