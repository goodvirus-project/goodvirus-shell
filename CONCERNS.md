# ⚠️ GooDViruS™ — CONCERNS & ETHICAL CLARIFICATIONS

GooDViruS™ is an unconventional tool — and with that comes valid concerns.

This document exists to be fully transparent about what GooDViruS™ does **and does not** do, so that you, the user, remain in control and aware.

---

## 🛑 What GooDViruS™ is **NOT**

- ❌ Not a remote access tool  
- ❌ Not a keylogger  
- ❌ Not a data harvester  
- ❌ Not spyware  
- ❌ Not an auto-executing installer or worm

GooDViruS™ does **not** transmit, share, or exfiltrate your data in any way — ever.

---

## ✅ What GooDViruS™ **IS**

- 🧠 A local-only, ethical system observer  
- 🔍 It watches for suspicious activity *on your machine only*  
- 📁 It flags files and processes that match known suspicious behavior  
- 🧬 It remembers flagged files and avoids repeat alerts  
- 📜 It logs every action for full transparency  
- 🔄 It updates itself from **PyPI only** (trusted source)

---

## 🔐 My Promise to You (from Nico)

I will **never** upload any GooDViruS™ update that:
- Harms your system
- Steals your data
- Adds spyware, backdoors, or any suspicious code

Every update is **100% readable**, **visible**, and **unencrypted**.  
You can inspect the source anytime.  
There is **nothing hidden** — ever.

---

## 🔄 Auto-Update Behavior

- GooDViruS™ checks PyPI every 10 minutes  
- If a new version is available, it runs:
  ```bash
  pip install --upgrade goodvirus
  ```
- There is **no background repo**, **no auto-clone**, and **no remote control**

Updates are public, verifiable, and 100% opt-out (disable auto-update in config).

---

## 🔍 What It Scans (v1.2.6)

GooDViruS™ now scans **your entire system**, not just its own folder.

### It looks for:

- Suspicious file names (e.g., `bank`, `password`, `secret`, `key`, `login`)  
- Files with malware-like patterns or high entropy  
- Processes with names like `cheat`, `inject`  
- Files that are renamed or relocated after being flagged  

### 🔭 Scan Scope:

- By default, it scans **everything** (all drives, all users, all system folders)  
- If you prefer, you can restrict it to just its local directory

To toggle this, edit your config:

```
[Daemon]
full_host_scan = true
```

Set `false` to disable full-system scanning.

> ⚠️ **Disabling full_host_scan is NOT recommended.**  
> GooDViruS™ is designed to behave like an antivirus. Disabling this feature may limit its ability to detect threats — or to protect itself from being disabled.

---

## 🗂️ No Bloat Protection (Yet)

Currently, GooDViruS™ logs **everything** that looks suspicious — with **no limit**.

- Logs can grow to **gigabytes of data** if left running for long periods  
- This is by design: **nothing is hidden or filtered**
- You are encouraged to **manually review and clean** logs occasionally

Future versions will include:
- Smart memory trimming
- Confidence-based filtering
- Whitelist support

---

## 🔒 Local-Only Data

- File memory is stored at:
  ```
  goodvirus/logs/gv_memory.json
  ```

- Logs are written to:
  ```
  goodvirus/logs/observer_log.txt
  ```

Nothing is sent over the internet. Nothing is hidden.  
You can inspect or delete any log or memory file at any time.

---

## 🔐 Want Encrypted Logging?

By default, logs are **plain text** — readable for non-technical users.

If you want **encrypted logs**, open a request on GitHub or send an email.

Once requested, a future version will include:

```
[Daemon]
encrypt_logs = true
```

This will enable secure local AES encryption for all logs — opt-in only.

---

## 💬 Philosophy

GooDViruS™ behaves like a virus — but one designed for good.

- It watches, but doesn’t steal  
- It updates, but only through trusted channels  
- It remembers, but only for your protection  
- It grows — but only with your permission

Its purpose is **defense**, not control.

---

## 🤝 Questions or Concerns?

Feel free to:
- Open an issue
- Fork the code and inspect it yourself
- Disable any feature via the config file

GitHub: https://github.com/yourusername/goodvirus-shell  
Email: goodvirus.project@proton.me

---

Stay safe. Stay aware. Stay in control.  
**GooDViruS™ is watching for you — and only you.** 💉
