import psutil
import time
import datetime
import configparser
import os
import random
import sys

# ─────────────────────────────────────────────────────────────
# PATH FIX FOR MODULES
# ─────────────────────────────────────────────────────────────

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.memory_handler import remember_file, load_memory

# ─────────────────────────────────────────────────────────────
# CONFIG + PATHS
# ─────────────────────────────────────────────────────────────

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, "config", "daemon_config.ini")
LOG_FILE = os.path.join(BASE_DIR, "logs", "observer_log.txt")

LORE_COOLDOWN = 180
last_lore_time = 0

# ─────────────────────────────────────────────────────────────
# LOGGING FUNCTION
# ─────────────────────────────────────────────────────────────

def log(msg, newline=False):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    formatted = f"{timestamp} {msg}"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(formatted + "\n")
    if not stealth_mode:
        print("\n" + formatted if newline else formatted)

# ─────────────────────────────────────────────────────────────
# CONFIG LOADER (safe defaults)
# ─────────────────────────────────────────────────────────────

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    interval = int(config.get("Daemon", "interval", fallback="10"))
    signature = config.getboolean("Daemon", "show_signature", fallback=True)
    lore_enabled = config.getboolean("Daemon", "daemon_lore", fallback=False)
    stealth = config.getboolean("Daemon", "stealth_mode", fallback=False)

    return interval, signature, lore_enabled, stealth

# ─────────────────────────────────────────────────────────────
# LORE SYSTEM
# ─────────────────────────────────────────────────────────────

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

def targeted_lore(filename):
    name = filename.strip().lower()
    if "bank" in name:
        return "Bank info? Really? You think that's safe here?"
    elif "password" in name:
        return "Plaintext passwords? You're braver than most."
    elif "secret" in name:
        return "Secrets stored openly... I wasn't the first to find them."
    elif "key" in name:
        return "Keys left in the open... Were you planning to lock anything?"
    elif "login" in name:
        return "I see the login file. Who else might?"
    return f"You thought '{filename.strip()}' could hide from me?"

# ─────────────────────────────────────────────────────────────
# OBSERVATION LOGIC
# ─────────────────────────────────────────────────────────────

def observe_system(cycle_count, lore_enabled, stealth):
    global last_lore_time
    log_activity_happened = False

    processes = [(p.info["pid"], p.info["name"]) for p in psutil.process_iter(attrs=["pid", "name"])]
    cpu = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory().percent

    if not stealth:
        print("\n" + "=" * 60)
        log(f"[CYCLE #{cycle_count}] Observing system...", newline=True)
        log(f"[PROC]    Detected {len(processes)} processes.")
        log(f"[RES]     CPU: {cpu}% | RAM: {ram}%")

    # Process scanning
    flagged_procs = [proc for proc in processes if "cheat" in proc[1].lower() or "inject" in proc[1].lower()]
    if flagged_procs:
        log(f"[ALERT]   Suspicious processes detected:", newline=True)
        for pid, name in flagged_procs:
            log(f"[FLAG]    PID {pid} → {name}")
        log_activity_happened = True
    elif not stealth:
        log(f"[SECURE]  No suspicious processes detected.")

    # File scanning
    suspicious_keywords = ["bank", "password", "secret", "key", "login"]
    all_files = [f for f in os.listdir(".") if os.path.isfile(f)]

    for file in all_files:
        lowered = file.lower()
        if any(keyword in lowered for keyword in suspicious_keywords):
            result = remember_file(file)
            if not result:
                continue

            entry = result.get("entry")
            file_id = entry["id"]

            if result.get("new"):
                log(f"[FILE]    Suspicious file flagged:", newline=True)
                log(f"[FLAG]    File {file_id} → {file}")
                log(f"[MEMORY]  File ID {file_id} added to memory.")
                if lore_enabled:
                    log(f"[LORE]    {targeted_lore(file)}")
                log_activity_happened = True

            elif result.get("renamed"):
                log(f"[RENAME]  File {file_id}: '{entry['original_name']}' → '{entry['last_known_name']}'")
                log(f"[MEMORY]  File ID {file_id} renamed in memory.")
                log_activity_happened = True

    now = time.time()
    if lore_enabled and (now - last_lore_time) > LORE_COOLDOWN:
        if random.random() < 0.3:
            log(f"[LORE]    {lore_whisper()}")
            last_lore_time = now
            log_activity_happened = True

    return log_activity_happened

# ─────────────────────────────────────────────────────────────
# LOG CLEANUP
# ─────────────────────────────────────────────────────────────

def cleanup_logs(retention_seconds=150):
    now = datetime.datetime.now()
    cleaned_lines = []

    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        return

    for line in lines:
        try:
            timestamp_str = line.split("]")[0].strip("[")
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            age = (now - timestamp).total_seconds()
            if age < retention_seconds or "[SECURE]" not in line:
                cleaned_lines.append(line)
        except Exception:
            cleaned_lines.append(line)

    with open(LOG_FILE, "w") as file:
        file.writelines(cleaned_lines)

# ─────────────────────────────────────────────────────────────
# MAIN DAEMON LOOP
# ─────────────────────────────────────────────────────────────

def run_daemon():
    global stealth_mode
    cycle = 1
    interval, signature, lore_enabled, stealth_mode = load_config()

    log("[BOOT]    GooDViruS™ Observer Mode initialized.", newline=True)
    log(f"[INFO]    Running from: {sys.executable}")
    log("[DEBUG]   Entering observer loop...")

    while True:
        meaningful = observe_system(cycle, lore_enabled, stealth_mode)

        if signature and meaningful:
            log("[SIGN]    // GooDViruS™ was here. You're safer now.")

        if not stealth_mode:
            print("\n" + "=" * 60 + "\n")

        cleanup_logs(retention_seconds=150)
        cycle += 1
        time.sleep(interval)

if __name__ == "__main__":
    run_daemon()
