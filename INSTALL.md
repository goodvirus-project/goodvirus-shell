```markdown
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

#### Activate it:

- **Windows:**

```bash
.\env\Scripts\activate
```

- **macOS/Linux:**

```bash
source env/bin/activate
```

You’ll know it's active when your terminal line starts with `(env)`

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

It will begin scanning your system and logging any suspicious behavior.

---

## 🧾 Configuration File

Edit this file:

```
goodvirus/config/daemon_config.ini
```

Available options:

```
[Daemon]
interval = 15
stealth_mode = false
daemon_lore = true
show_signature = true
```

---

## 🔄 Updating

GooDViruS™ checks PyPI for updates automatically every 10 minutes and upgrades itself if needed.

You can also update manually:

```bash
pip install --upgrade goodvirus
```

---

## 🧯 Troubleshooting

### `command not found` or `'goodvirus' is not recognized`?

Make sure:
- Python was installed with “Add to PATH” checked
- Your virtual environment is activated (`(env)` shows in terminal)

### Still stuck?

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
```
