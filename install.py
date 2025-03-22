import os
import sys
import subprocess
import urllib.request
import shutil
import configparser
import ctypes
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

REQUIRED_PACKAGES = [
    "altgraph==0.17.4",
    "backports.tarfile==1.2.0",
    "certifi==2025.1.31",
    "charset-normalizer==3.4.1",
    "configparser==7.2.0",
    "docutils==0.21.2",
    "goodvirus==1.3.0",
    "id==1.5.0",
    "idna==3.10",
    "importlib_metadata==8.6.1",
    "jaraco.classes==3.4.0",
    "jaraco.context==6.0.1",
    "jaraco.functools==4.1.0",
    "keyring==25.6.0",
    "markdown-it-py==3.0.0",
    "mdurl==0.1.2",
    "more-itertools==10.6.0",
    "nh3==0.2.21",
    "packaging==24.2",
    "pefile==2023.2.7",
    "psutil==7.0.0",
    "Pygments==2.19.1",
    "pyinstaller==6.12.0",
    "pyinstaller-hooks-contrib==2025.1",
    "pywin32-ctypes==0.2.3",
    "readme_renderer==44.0",
    "requests==2.32.3",
    "requests-toolbelt==1.0.0",
    "rfc3986==2.0.0",
    "rich==13.9.4",
    "twine==6.1.0",
    "typing_extensions==4.12.2",
    "urllib3==2.3.0",
    "zipp==3.21.0"
]

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate():
    """Rerun script with admin rights"""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)

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
        print("📥 Downloading Python...")
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

    venv_python = os.path.join(venv_path, "Scripts", "python.exe")

    print("📦 Installing requirements...")
    subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)

    for package in REQUIRED_PACKAGES:
        subprocess.run([venv_python, "-m", "pip", "install", package], check=True)

    return venv_path

def detect_config(install_dir):
    config_path = os.path.join(install_dir, "config", "daemon_config.ini")
    print("\n🔍 Detected Settings:")
    if os.path.exists(config_path):
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8")
        for key in config["Daemon"]:
            val = config.get("Daemon", key)
            print(f"   • {key.replace('_', ' ').capitalize()}: {val}")
    else:
        print("   ⚠️  No config file found.")

def copy_project_files(src_root, install_dir):
    print(f"📁 Copying project files to {install_dir}...")
    folders_to_copy = ["goodvirus", "config"]
    files_to_copy = ["README.md", "LICENSE", "SECURITY.md"]

    for item in folders_to_copy:
        src = os.path.join(src_root, item)
        dst = os.path.join(install_dir, item)
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)

    for item in files_to_copy:
        src = os.path.join(src_root, item)
        dst = os.path.join(install_dir, item)
        if os.path.exists(src):
            shutil.copy2(src, dst)

def finish(install_dir):
    print("\n✅ Installation complete.")
    print(f"📍 Installed to: {install_dir}")
    print(f"💡 To run it manually:")
    print(f"   {install_dir}\\goodvirus-env\\Scripts\\python.exe goodvirus\\observer.py")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input("\n[Press ENTER to exit]")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(ASCII_BANNER)

    if not is_admin():
        print("⚠️  Admin rights required — requesting elevation...\n")
        elevate()
        sys.exit()

    install_dir = prompt_install_location()
    install_python_if_missing()
    venv = create_venv_and_install(install_dir)

    project_root = os.path.dirname(os.path.abspath(__file__))
    copy_project_files(project_root, install_dir)

    detect_config(install_dir)
    finish(install_dir)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n❌ INSTALLER ERROR:")
        print(str(e))
        input("\n[Press ENTER to exit]")
