import os
import subprocess
import sys
import time
import shutil
import urllib.request
import platform

VENV_DIR = "env"
REQUIREMENTS_FILE = "requirements.txt"
WATCHER_SCRIPT = "src/watcher.py"
PYTHON_MIN_VERSION = (3, 6)

def log(msg):
    print(f"[GooDViruS™ Installer] {msg}")

def slowlog(msg, dots=3, delay=0.2):
    print(f"[GooDViruS™ Installer] {msg}", end="", flush=True)
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="", flush=True)
    print()

def banner():
    print("\n")
    print(" ╔════════════════════════════════════╗")
    print(" ║      Summoning: GooDViruS™        ║")
    print(" ║     Ethical Daemon Installer      ║")
    print(" ╚════════════════════════════════════╝\n")
    time.sleep(0.5)

def is_python_installed():
    return shutil.which("python") or shutil.which("python3")

def install_python_linux():
    log("Attempting to install Python on Linux...")
    distro = platform.linux_distribution()[0].lower() if hasattr(platform, "linux_distribution") else ""

    if shutil.which("apt"):
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", "python3", "python3-venv", "python3-pip"])
    elif shutil.which("dnf"):
        subprocess.run(["sudo", "dnf", "install", "-y", "python3", "python3-pip"])
    elif shutil.which("pacman"):
        subprocess.run(["sudo", "pacman", "-Sy", "--noconfirm", "python", "python-pip"])
    else:
        log("❌ No supported package manager found. Install Python manually.")
        sys.exit(1)

def download_python_windows():
    url = "https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe"
    local_file = "python-installer.exe"
    print(f"\n[GooDViruS™ Installer] Downloading Python installer from:\n{url}\n")
    urllib.request.urlretrieve(url, local_file)
    print("[GooDViruS™ Installer] Running installer...")
    subprocess.run([local_file], shell=True)

def check_python_or_prompt():
    if sys.version_info < PYTHON_MIN_VERSION:
        print("[GooDViruS™ Installer] ❌ Your Python version is too old.")
        sys.exit(1)

    if is_python_installed():
        return

    print("\n[GooDViruS™ Installer] ❗ Python is not installed.")
    print("1 = Download / Install it now")
    print("2 = Cancel and exit\n")

    choice = input("> ").strip()

    if choice == "1":
        if platform.system() == "Windows":
            download_python_windows()
        elif platform.system() == "Linux":
            install_python_linux()
        else:
            log("❌ Unsupported OS. Please install Python manually.")
            sys.exit(1)
        print("\n[GooDViruS™ Installer] After installing Python, re-run this script.")
        sys.exit(0)
    else:
        print("[GooDViruS™ Installer] Exiting. The daemon waits.")
        sys.exit(0)

def find_pip(scripts_dir):
    possible_names = ["pip", "pip3", "pip.exe", "pip3.exe", "pip.bat"]
    for name in possible_names:
        full_path = os.path.join(VENV_DIR, scripts_dir, name)
        if os.path.isfile(full_path):
            return full_path
    return None

def run_installer():
    banner()
    check_python_or_prompt()
    log("Initializing secure daemon environment...")

    if not os.path.exists(VENV_DIR):
        slowlog("Creating isolated environment")
        subprocess.run([sys.executable, "-m", "venv", VENV_DIR])
    else:
        log("Found existing environment. Using it.")

    scripts_dir = "Scripts" if os.name == "nt" else "bin"
    python_executable = os.path.join(VENV_DIR, scripts_dir, "python")

    slowlog("Locating pip inside virtual environment")
    pip_executable = find_pip(scripts_dir)

    if not pip_executable:
        log("pip not found — attempting to inject with ensurepip...")
        subprocess.run([python_executable, "-m", "ensurepip", "--upgrade"])
        pip_executable = find_pip(scripts_dir)

    if not pip_executable:
        log("❌ Failed to install or locate pip in the environment.")
        sys.exit(1)

    slowlog("Installing required modules from requirements.txt")
    result = subprocess.run([pip_executable, "install", "-r", REQUIREMENTS_FILE])

    if result.returncode != 0:
        log("❌ Failed to install required modules.")
        sys.exit(1)

    log("✅ Installation complete.")
    log(f"Python interpreter: {python_executable}")

    print("\n[GooDViruS™ Installer] The daemon shell has been prepared.")
    print("[GooDViruS™ Installer] Would you like to run it now?")
    print("1 = Yes")
    print("2 = No\n")

    choice = input("> ").strip()

    if choice == "1":
        log("Launching GooDViruS™ in Observer Mode...")
        time.sleep(0.5)
        subprocess.run([python_executable, WATCHER_SCRIPT])
    else:
        log("Daemon installation is complete.")
        log("It now waits in silence until you are ready to summon it again.")

if __name__ == "__main__":
    run_installer()
