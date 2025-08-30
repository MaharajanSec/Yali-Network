import socket

target = "scanme.nmap.org"
ports = [21, 22, 80, 443]

print(f"Scanning {target}...")
for port in ports:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        print(f"[-] Port {port} is closed")