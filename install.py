import os
import sys
import subprocess
import urllib.request
import zipfile
import ctypes
import shutil
import configparser
from pathlib import Path

ASCII_BANNER = r"""
  ____                  _    _     _               
 / ___| ___   ___   ___(_)  | | __ _ ___ ___  ___  
| |  _ / _ \ / _ \ / __| |  | |/ _` / __/ __|/ _ \ 
| |_| | (_) | (_) | (__| |  | | (_| \__ \__ \  __/ 
 \____|\___/ \___/ \___|_|  |_|\__,_|___/___/\___| 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧬 GooDViruS™ Secure Installer
"""

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate():
    """Rerun script with admin rights"""
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

def prompt_install_location():
    default = r"C:\Program Files\GooDViruS"
    print(f"\n📂 Enter install location [Default: {default}]")
    user_input = input("→ ").strip()
    return user_input if user_input else default

def install_python_if_missing():
    try:
        subprocess.check_output(["python", "--version"])
        print("✔️  Python is already installed.")
    except:
        print("📥 Downloading latest Python installer...")
        url = "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
        local_path = "python_installer.exe"
        urllib.request.urlretrieve(url, local_path)
        print("⚙️  Installing Python silently...")
        subprocess.run([local_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"])
        os.remove(local_path)

def create_venv_and_install(install_dir):
    venv_path = os.path.join(install_dir, "goodvirus-env")
    os.makedirs(install_dir, exist_ok=True)

    print("🌱 Creating virtual environment...")
    subprocess.run(["python", "-m", "venv", venv_path], check=True)

    pip_path = os.path.join(venv_path, "Scripts", "pip.exe")

    print("📦 Installing requirements...")
    subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
    subprocess.run([pip_path, "install", "psutil", "configparser"], check=True)

    return venv_path

def detect_config(install_dir):
    config_path = os.path.join(install_dir, "config", "daemon_config.ini")
    print("🔍 Detected Settings:")
    if os.path.exists(config_path):
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8")
        for key in config["Daemon"]:
            val = config.get("Daemon", key)
            print(f"   • {key.replace('_', ' ').capitalize()}: {val}")
    else:
        print("   ⚠️  No config file found.")

def finish(install_dir):
    print("\n✅ Installation complete.")
    print(f"📍 Installed to: {install_dir}")
    print("You may now launch GooDViruS by running:")
    print(f"  {install_dir}\\goodvirus-env\\Scripts\\python.exe goodvirus\\observer.py")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def main():
    os.system("cls")
    print(ASCII_BANNER)

    if not is_admin():
        print("⚠️  Admin rights required — requesting elevation...\n")
        elevate()
        sys.exit()

    install_dir = prompt_install_location()
    install_python_if_missing()
    venv = create_venv_and_install(install_dir)

    # Copy the current source files into install_dir
    source_root = os.path.dirname(os.path.abspath(__file__))
    print(f"📁 Copying files to {install_dir}...")
    for folder in ["goodvirus", "config", "README.md", "SECURITY.md", "LICENSE"]:
        src = os.path.join(source_root, folder)
        dst = os.path.join(install_dir, folder)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        elif os.path.isfile(src):
            shutil.copy2(src, dst)

    detect_config(install_dir)
    finish(install_dir)

if __name__ == "__main__":
    main()
