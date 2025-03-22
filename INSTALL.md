# 🛠️ GooDViruS™ Installation & Setup Guide

Welcome! This guide walks you through installing, configuring, and running GooDViruS™ — even if you're not a tech expert.

---

## ✅ Requirements

- Python **3.7 or higher**
- Internet connection (only for installation & updates)
- Basic comfort with a terminal or command prompt

---

## 📦 Step-by-Step Installation

### 1. Install Python

- Download from: https://www.python.org/downloads/
- During installation, **check this box**:

```
[x] Add Python to PATH
```

---

### 2. Open a Terminal

- **Windows:** Open PowerShell or CMD  
- **macOS/Linux:** Open Terminal

---

### 3. (Optional) Create a Virtual Environment

```bash
python -m venv env
```

### Activate it:

- **Windows:**

```bash
.\env\Scripts\activate
```

- **macOS/Linux:**

```bash
source env/bin/activate
```

You'll know it's active if you see `(env)` at the beginning of your terminal line.

---

### 4. Install GooDViruS™

```bash
pip install goodvirus
```

You should see: `Successfully installed goodvirus`

---

## 🚀 Run the Daemon

```bash
goodvirus
```

It will start scanning your system and logging any suspicious behavior.

---

## 🧾 Configuration File

Open this file to configure the daemon:

```
goodvirus/config/daemon_config.ini
```

### Options:

| Key             | Description                          | Default |
|------------------|--------------------------------------|---------|
| `interval`       | Delay between scans (in seconds)     | `10`    |
| `stealth_mode`   | Hide output in terminal              | `false` |
| `daemon_lore`    | Enable creepy lore messages          | `false` |
| `show_signature` | Show signature after each alert      | `true`  |

### Example:

```ini
[Daemon]
interval = 15
stealth_mode = false
daemon_lore = true
show_signature = true
```

---

## 🔄 Updating

GooDViruS™ updates itself automatically via PyPI.

It checks for new versions every 10 minutes and installs updates automatically.

You can also manually update it anytime with:

```bash
pip install --upgrade goodvirus
```

---

## 🧯 Troubleshooting

### ❗ `'goodvirus' is not recognized` or `command not found`?

Make sure:
- Python is correctly installed with "Add to PATH"
- Your virtual environment is activated (you see `(env)`)

### ❗ Still having issues?

Try reinstalling:

```bash
pip uninstall goodvirus
pip install goodvirus
```

Then run:

```bash
goodvirus
```

---

## 🤝 Need Help?

Open an issue on GitHub:  
https://github.com/yourusername/goodvirus-shell/issues

---

Stay aware. Stay protected.  
**GooDViruS™ is always watching — for the right reasons.**
