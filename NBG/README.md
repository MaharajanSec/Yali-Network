# Netrix Banner Grabber

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Stars](https://img.shields.io/github/stars/MaharajanSec/NetrixBannerGrabber?style=social)
![Forks](https://img.shields.io/github/forks/MaharajanSec/NetrixBannerGrabber?style=social)

Netrix Banner Grabber (NBG) is a simple menu-driven tool for capturing service banners from different protocols.  
It helps identify what software or service is running on a target host.

---

## Features
- Supports multiple services:
  - **HTTP (port 80)** → response headers only
  - **HTTPS (port 443)** → TLS handshake + response headers only
  - **SSH (port 22)** → first line banner
  - **FTP (port 21)** → first line banner
  - **SMTP (port 25)** → first line banner
  - **Custom host + port** → first line banner
- Menu-driven interface
- Colored output for easy readability
- Option to save results to `results.txt`
- Each saved entry includes a timestamp

---

## Installation

### Requirements
- Python **3.7 or higher**
- No external libraries required (uses only Python standard library)

### Clone Repository
```bash
git clone https://github.com/MaharajanSec/NetrixBannerGrabber.git
cd NetrixBannerGrabber
```

### Run the Tool
```bash
python BannerCap.py
```

### Show Help
```bash
python BannerCap.py --help
```

---

## Usage

When you run the tool, you’ll see:

```
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$   N E T R I X   G R A B B E R   $$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

1. Scan a Website (HTTP, port 80)
2. Scan a Secure Website (HTTPS, port 443)
3. Scan SSH Service (port 22)
4. Scan FTP Service (port 21)
5. Scan Mail Server (SMTP, port 25)
6. Custom Host + Port
7. Exit
```

### Example Run (HTTPS)

```
Select an option (1-7): 2
Enter target (hostname or URL): example.com

[*] Connecting to example.com:443 ...

[+] Banner successfully captured:

HTTP/1.1 200 OK
Date: Sat, 30 Aug 2025 10:45:10 GMT
Server: Apache
X-Powered-By: PHP/7.3.33
Content-Type: text/html; charset=UTF-8
```

### Example Run (SSH)

```
Select an option (1-7): 3
Enter target (hostname or URL): test.rebex.net

[*] Connecting to test.rebex.net:22 ...

[+] Banner successfully captured:

SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u7
```

### Example Run (FTP)

```
Select an option (1-7): 4
Enter target (hostname or URL): speedtest.tele2.net

[*] Connecting to speedtest.tele2.net:21 ...

[+] Banner successfully captured:

220 (vsFTPd 3.0.3)
```

---

## Saving Results

After a banner is captured, the program will ask:

```
Save this banner to results.txt? (y/n):
```

If you choose `y`, the banner is saved with a timestamp in `results.txt`.

Example entry:

```
Timestamp: 2025-08-30 12:30:45
Target: example.com:443
HTTP/1.1 200 OK
Server: Apache
X-Powered-By: PHP/7.3.33
------------------------------------------------------------
```

---

## Disclaimer ⚠️

This tool is intended for **educational and security research purposes only**.  
You must only use it on systems you **own** or are **explicitly authorized** to test.  

Unauthorized scanning of systems without permission may be **illegal** and could lead to criminal or civil consequences.  
The author assumes **no liability** for any misuse of this tool.

---

## Author

Developed by **MaharajanSec** as part of the **Netrix Security Toolkit**.
