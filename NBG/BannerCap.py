#!/usr/bin/env python3
"""
Netrix Banner Grabber (NBG)

A menu-driven tool to capture service banners (HTTP, HTTPS, SSH, FTP, SMTP, Custom).
Shows clean headers or first-line banners.  
Run with `--help` for usage info or see README.md for full details.
"""

import sys
import socket
import ssl
from urllib.parse import urlparse
from datetime import datetime

# Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

def framed_banner(text: str, width: int = 55) -> str:
    border = "$" * width
    line = f"$$$   {text}   $$$"
    return f"{GREEN}{border}\n{line.center(width)}\n{border}{RESET}"

def clean_target(target: str, default_port: int):
    if not target.startswith(("http://", "https://")):
        target = "http://" + target
    parsed = urlparse(target)
    host = parsed.hostname
    port = parsed.port or default_port
    return host, port

def grab_banner(host: str, port: int, timeout: int = 5, use_ssl=False) -> str:
    """Grab only headers for HTTP/HTTPS. For other services, first line only."""
    try:
        if use_ssl:  # HTTPS
            context = ssl.create_default_context()
            with socket.create_connection((host, port), timeout=timeout) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
                    ssock.sendall(request.encode())

                    data = b""
                    while b"\r\n\r\n" not in data:
                        chunk = ssock.recv(1024)
                        if not chunk:
                            break
                        data += chunk
                    headers = data.split(b"\r\n\r\n")[0]
                    return headers.decode(errors="ignore")

        else:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                sock.connect((host, port))

                if port == 80:  # HTTP
                    request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
                    sock.sendall(request.encode())

                    data = b""
                    while b"\r\n\r\n" not in data:
                        chunk = sock.recv(1024)
                        if not chunk:
                            break
                        data += chunk
                    headers = data.split(b"\r\n\r\n")[0]
                    return headers.decode(errors="ignore")

                # SSH, FTP, SMTP, custom → just grab first line
                data = sock.recv(1024)
                first_line = data.split(b"\r\n")[0]
                return first_line.decode(errors="ignore")

    except Exception as e:
        return f"{RED}[!] Error: {e}{RESET}"

def show_menu():
    print()
    print(f"{GREEN}1{RESET}. {WHITE}Scan a Website (HTTP, port 80){RESET}")
    print(f"{GREEN}2{RESET}. {WHITE}Scan a Secure Website (HTTPS, port 443){RESET}")
    print(f"{GREEN}3{RESET}. {WHITE}Scan SSH Service (port 22){RESET}")
    print(f"{GREEN}4{RESET}. {WHITE}Scan FTP Service (port 21){RESET}")
    print(f"{GREEN}5{RESET}. {WHITE}Scan Mail Server (SMTP, port 25){RESET}")
    print(f"{GREEN}6{RESET}. {WHITE}Custom Host + Port{RESET}")
    print(f"{GREEN}7{RESET}. {WHITE}Exit{RESET}")

def main():
    print(framed_banner("N E T R I X   G R A B B E R"))

    while True:
        show_menu()
        choice = input(f"{CYAN}Select an option (1-7): {RESET}").strip()

        if choice == "7":
            print(f"{YELLOW}Goodbye 👋{RESET}")
            break

        if choice in ["1","2","3","4","5","6"]:
            target_input = input(f"{CYAN}Enter target (hostname or URL): {RESET}").strip()
            if not target_input:
                print(f"{RED}[!] No target entered. Try again.{RESET}")
                continue

            if choice == "1":
                host, port = clean_target(target_input, 80)
                use_ssl = False
            elif choice == "2":
                host, port = clean_target(target_input, 443)
                use_ssl = True
            elif choice == "3":
                host, port = clean_target(target_input, 22)
                use_ssl = False
            elif choice == "4":
                host, port = clean_target(target_input, 21)
                use_ssl = False
            elif choice == "5":
                host, port = clean_target(target_input, 25)
                use_ssl = False
            elif choice == "6":
                host = target_input
                port_input = input(f"{CYAN}Enter the port: {RESET}").strip()
                if not port_input.isdigit():
                    print(f"{RED}[!] Port must be a number{RESET}\n")
                    continue
                port = int(port_input)
                use_ssl = (port == 443)

            print(f"{CYAN}[*] Connecting to {host}:{port} ...{RESET}\n")
            banner = grab_banner(host, port, use_ssl=use_ssl)

            if banner and not banner.startswith(f"{RED}[!]"):
                print(f"{GREEN}[+] Banner successfully captured:{RESET}\n")
                print(banner)

                save = input(f"\n{CYAN}Save this banner to results.txt? (y/n): {RESET}").strip().lower()
                if save == "y":
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    with open("results.txt", "a", encoding="utf-8") as f:
                        f.write(f"Timestamp: {timestamp}\n")
                        f.write(f"Target: {host}:{port}\n")
                        f.write(banner + "\n" + "-"*60 + "\n")
                    print(f"{GREEN}[+] Saved to results.txt{RESET}\n")
            else:
                print(banner or f"{RED}[-] No banner received.{RESET}\n")
        else:
            print(f"{RED}[!] Invalid choice, please try again.{RESET}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print(__doc__)
        sys.exit(0)
    main()
