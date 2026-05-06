import socket
from datetime import datetime

# Target to scan
target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except:
    print("Invalid target")
    exit()

print("-" * 50)
print(f"Scanning Target: {target_ip}")
print(f"Time Started: {datetime.now()}")
print("-" * 50)

open_ports = []

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    result = sock.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)
    sock.close()

# Basic vulnerability checks
vulnerabilities = []

if 21 in open_ports:
    vulnerabilities.append("FTP port open (Possible insecure configuration)")

if 23 in open_ports:
    vulnerabilities.append("Telnet port open (Highly insecure)")

if 445 in open_ports:
    vulnerabilities.append("SMB port open (Check for vulnerabilities like EternalBlue)")

if 3389 in open_ports:
    vulnerabilities.append("RDP port open (Check for brute-force protection)")

# Generate report
print("\n--- Vulnerability Report ---")
print(f"Target: {target_ip}")
print(f"Open Ports: {open_ports}")

if vulnerabilities:
    print("\nPossible Vulnerabilities:")
    for v in vulnerabilities:
        print(f"- {v}")
else:
    print("\nNo obvious vulnerabilities detected.")

print("\nScan Completed.")
with open("report.txt", "w") as f:
    f.write(f"Target: {target_ip}\n")
    f.write(f"Open Ports: {open_ports}\n")
    f.write("Vulnerabilities:\n")
    for v in vulnerabilities:
        f.write(f"- {v}\n")
        sock.send(b"Hello\r\n")
banner = sock.recv(1024)
print(banner)