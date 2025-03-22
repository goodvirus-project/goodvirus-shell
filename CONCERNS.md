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

## 🔄 Auto-Update Behavior

- GooDViruS™ checks PyPI every 10 minutes  
- If a new version is available, it runs:
  ```
  pip install --upgrade goodvirus
  ```
- There is **no background repo**, **no auto-clone**, and **no remote control**

Updates are public, verifiable, and 100% opt-out (disable auto-update if needed).

---

## 🔍 What It Scans (Current Version)

- Suspicious file names (e.g., `bank`, `password`, `secret`, `key`, `login`)  
- Files with malware-like patterns or high entropy  
- Processes with names like `cheat`, `inject`  
- The current working directory and subfolders only

**It does NOT access your camera, microphone, browser data, or private accounts.**

---

## 🧭 Upcoming Feature: Full-System Scan (Next Update)

In the **next update**, GooDViruS™ will include a **full host scan** feature.

### 🔧 What it does:

- Recursively scans **your entire computer** (all drives and user directories)  
- Protects system integrity by detecting deeply hidden threats  
- Actively monitors attempts to **tamper with GooDViruS™ itself**

### 🛑 Can I disable this?

Yes. When this feature goes live, a new option will appear in your config file:

```
[Daemon]
full_host_scan = true
```

Set to `false` if you want to disable it.

> ⚠️ **Disabling full_host_scan is NOT recommended.**  
> GooDViruS™ is designed to function as a self-defending antivirus-like system. Disabling full-system scanning may reduce its effectiveness and leave your system vulnerable.

This option exists to preserve your control — but the feature is included to protect *you* and *the daemon itself*.

---

## 🔒 Local-Only Data

- All file memory is stored in:
  ```
  goodvirus/logs/gv_memory.json
  ```

- Logs are written to:
  ```
  goodvirus/logs/observer_log.txt
  ```

Nothing is sent over the internet. Nothing is hidden or encrypted.

You can delete any log or memory file at any time.

---

## 🔐 Want Encrypted Logging?

By default, logs are **plain text** — readable for non-technical users who want to understand what’s going on.

If you prefer **encrypted logging** for extra privacy, open a request on GitHub or send an email.

Once requested, a future version will include optional log encryption via config:

```
[Daemon]
encrypt_logs = true
```

This will encrypt all logs using secure local AES encryption — but only if you explicitly enable it.

---

## 💬 Philosophy

GooDViruS™ behaves like a virus — but one designed for good.

- It watches, but doesn’t steal  
- It updates, but only through trusted channels  
- It remembers, but only for your protection  
- It grows — but only with your permission

Its purpose is defense. Not control.

---

## 🤝 Questions or Concerns?

Feel free to:
- Open an issue
- Fork the code and inspect it yourself
- Disable features you don’t want

GitHub: https://github.com/yourusername/goodvirus-shell

---

Stay safe. Stay aware. Stay in control.  
**GooDViruS™ is watching for you — and only you.**
