# Changelog

All notable changes to **Netrix Banner Grabber** will be documented in this file.

---

## [v1.0.0] - 2025-08-30
### Added
- Initial release of Netrix Banner Grabber.
- Supports banner grabbing for:
  - HTTP (port 80) → response headers only
  - HTTPS (port 443) → TLS handshake + response headers only
  - SSH (port 22) → first line banner
  - FTP (port 21) → first line banner
  - SMTP (port 25) → first line banner
  - Custom host + port → first line banner
- Menu-driven CLI interface.
- Colored output for readability.
- Option to save results with timestamps to `results.txt`.
- Documentation in README.md with disclaimer.
- MIT License file included.
- `.gitignore` for Python projects.
- `VERSION` file for release tracking.

