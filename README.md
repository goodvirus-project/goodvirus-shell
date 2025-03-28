# GooDViruS™

**Version:** 1.2.6  
**Author:** Nico  
**License:** MIT  
**Platform:** Cross-platform  
**Install:** Available on [PyPI](https://pypi.org/project/goodvirus/)

---

## 📚 Documentation

- 📦 [Installation Guide (INSTALL.md)](./INSTALL.md)
- 🔐 [Concerns & Ethics (CONCERNS.md)](./CONCERNS.md)
- 🧾 [Security Policy (SECURITY.md)](./SECURITY.md)
- 🧪 [Changelog (Coming Soon)](./CHANGELOG.md)

---

## 🧬 What is GooDViruS™?

**GooDViruS™** is an ethical system watchdog daemon that quietly runs in the background and scans your system for:

- 🧱 Suspicious files (like `bankinfo.txt`, `passwords.txt`, etc.)
- 🧬 Malicious patterns (entropy detection, stealthy signatures)
- 💉 Dangerous-looking processes (`cheat`, `inject`, etc.)
- 📁 Files that have been renamed, moved, or manipulated in shady ways

It behaves *like* a virus — but only to **protect** you.

---

## 🛠️ Key Features

- 📁 **Persistent file memory** — remembers flagged files even after reboot
- 🔍 **Process monitoring** — detects suspicious programs
- 🧠 **Behavior-based heuristics** — no hardcoded virus list
- 🔄 **Auto-updates from PyPI** — secure and verifiable
- 👻 **Stealth mode** — quiet background operation
- 🕵️ **Lore mode** — optional creepy messages for flair
- ✅ **User-readable logs** — clear, timestamped activity reports

---

## 🆕 What’s New in v1.2.6

| Feature | Description |
|--------|-------------|
| 🧠 `ignore_system_noise` | New config option to **skip noisy system files** unless truly suspicious |
| 💾 Full-host scanning | Scans your entire system instead of just the project folder |
| 📍 Exact path logging | Logs show **full file paths** of flagged or renamed files |
| 🧮 Memory filter logic | Smart filtering of files from Windows system paths if `ignore_system_noise = true` |
| 🧭 Smarter output | Shows what’s happening, where, and why — even to non-tech users |
| ⚠️ Known Limitation | **No log bloat prevention yet** – log file can grow to **gigabytes** over time if left running unsupervised |

---

## ⚠️ Important Log Warning

GooDViruS™ logs **everything suspicious** it finds — which is great for visibility, but:

- ❗ The log file can grow **very large over time**
- ❗ It can reach **gigabytes** if left unattended
- ❗ There is **no automatic cleanup or size limit yet**

For now, you can manually clean the log:
```bash
del goodvirus/logs/observer_log.txt
```
Or disable certain modes in the config file.

> 🔐 Future updates will include smart log trimming, confidence levels, and whitelist support.

---

## 🧾 Configuration

After first run, open:
```
goodvirus/config/daemon_config.ini
```

You can toggle features like:
```ini
[Daemon]
interval = 10
stealth_mode = false
daemon_lore = true
show_signature = true
auto_update = true
full_host_scan = true
ignore_system_noise = true
```

---

## 🚀 Getting Started

### Install from PyPI:
```bash
pip install goodvirus
```

### Run the daemon:
```bash
goodvirus
```

Logs will appear in:
```
goodvirus/logs/observer_log.txt
```

---

## 📘 Full Setup Help

See the new guide:  
👉 [INSTALL.md](./INSTALL.md) — step-by-step for non-tech users

---

## 💬 Concerns or Ethics?

Everything is documented in:  
👉 [CONCERNS.md](./CONCERNS.md)

GooDViruS™ is open, local-only, and self-contained.  
It never sends data, and it works only for **you**.

---

Stay safe. Stay aware. Stay in control.  
**GooDViruS™ is watching — for your safety.** 💉
