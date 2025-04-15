import nmap # type: ignore
import requests

def run_version_cve_check():
    target = input("Enter target IP address: ")
    nm = nmap.PortScanner()

    print(f"\n[+] Scanning {target} for service versions...\n")
    try:
        nm.scan(target, arguments='-sV')  # Service version scan

        for host in nm.all_hosts():
            print(f"Host: {host}")
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['version']
                    product = nm[host][proto][port]['product']
                    extra = nm[host][proto][port]['extrainfo']
                    
                    print(f"[PORT {port}] {product} {version} {extra}")

                    # Cari CVE berdasarkan product + version
                    query = f"{product} {version}"
                    get_cve(query)
    except Exception as e:
        print(f"[!] Error during version scan: {e}")

def get_cve(query):
    print(f"\n[•] Searching CVEs for: {query}")
    try:
        res = requests.get(f"https://cve.circl.lu/api/search/{query}")
        if res.status_code == 200:
            data = res.json()
            results = data.get("results", [])
            if results:
                for i, cve in enumerate(results[:3], 1):  # Limit to 3 CVEs
                    print(f"  CVE-{i}: {cve['id']} - {cve['summary']}")
            else:
                print("  [-] No CVE found.")
        else:
            print("  [!] CVE API error.")
    except Exception as e:
        print(f"  [!] CVE lookup failed: {e}")
