#Yali Network Recon Suite

A collection of **network reconnaissance tools** written in Python.  
Built to assist **penetration testers** and **security researchers** during the discovery phase of assessments.

---

  Tools Included

 Port Scanner (`portscan.py`)
- Scans target hosts for **open ports**.  
- Supports **TCP scanning** and fast execution.  
- Displays **service banners** when available.

(Network Banner Grabber)('bannercap.py')
- Extracts service banners from open ports.  
- Helps identify running services, versions, and potential vulnerabilities.  
- Supports common protocols: **HTTP, HTTPS, FTP, SSH, SMTP, custom ports**.

---

 Directory Structure

```bash
network/
│── portscan.py      # TCP port scanner
│── NBG/             # Network banner grabber scripts
│── README.md        # Documentation

Disclaimer
This repo is for educational & authorized security testing only.
Do not run these tools against systems you don’t own or don’t have explicit permission to test.
You are responsible for your own actions.

