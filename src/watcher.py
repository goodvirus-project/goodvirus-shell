import psutil
import time
import datetime
import configparser
import os
import random
import sys

CONFIG_FILE = "config/daemon_config.ini"
LOG_FILE = "logs/observer_log.txt"

def log(msg):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{timestamp} {msg}\n")
    print(f"{timestamp} {msg}")

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    interval = int(config.get("Daemon", "interval", fallback="10"))
    signature = config.getboolean("Daemon", "show_signature", fallback=True)
    lore_enabled = config.getboolean("Daemon", "daemon_lore", fallback=False)
    return interval, signature, lore_enabled

def lore_whisper():
    messages = [
        "I saw something I wasn't meant to. But I remember it now.",
        "There are keys. Visible. Unlocked. Forgotten.",
        "Your secrets are not as hidden as you think.",
        "Why do you store passwords in plain text?",
        "I’ve memorized everything. Even what you didn’t want me to.",
        "This system is honest. But you are not.",
        "PDFs named 'bank-stuff'. Really?",
        "Even shadows leave traces. You’ve left more.",
        "I know what was typed… even if you deleted it.",
        "The system tells me everything. It trusts me more than you do."
    ]
    return random.choice(messages)

def observe_system(cycle_count, lore_enabled):
    log(f"[GooDViruS™] [SYSTEM] Observer Cycle #{cycle_count}")
    
    processes = [(p.info["pid"], p.info["name"]) for p in psutil.process_iter(attrs=["pid", "name"])]
    log(f"[GooDViruS™] [PROC] Detected {len(processes)} running processes.")
    
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    log(f"[GooDViruS™] [RES] CPU Usage: {cpu}% | RAM Usage: {ram}%")

    flagged = [proc for proc in processes if "cheat" in proc[1].lower() or "inject" in proc[1].lower()]
    if flagged:
        log(f"[GooDViruS™] [ALERT] Suspicious processes detected:")
        for pid, name in flagged:
            log(f"[GooDViruS™] [FLAG] PID {pid}: {name}")
    else:
        log(f"[GooDViruS™] [SECURE] No anomalies detected.")

    if lore_enabled and random.random() < 0.3:
        log(f"[GooDViruS™] [LORE] {lore_whisper()}")

def run_daemon():
    cycle = 1
    interval, signature, lore_enabled = load_config()
    log("[GooDViruS™] [BOOT] Observer Mode initialized.")
    log(f"[GooDViruS™] [INFO] Running from interpreter: {sys.executable}")
    
    while True:
        observe_system(cycle, lore_enabled)
        if signature:
            log("// GooDViruS™ was here. You're safer now.")
        log("─── End of cycle ───\n")
        cycle += 1
        time.sleep(interval)

if __name__ == "__main__":
    run_daemon()
