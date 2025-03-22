import os
import hashlib
import hmac
import requests
import subprocess
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_VERSION_FILE = os.path.join(BASE_DIR, "version.txt")
UPDATE_LOG = os.path.join(BASE_DIR, "logs", "self_update_log.txt")

REMOTE_BASE = "https://github.com/goodvirus-project/GooDViruS-updates/tree/main/latest"
REMOTE_VERSION_URL = REMOTE_BASE + "version.txt"
REMOTE_MANIFEST_URL = REMOTE_BASE + "files_manifest.txt"
REMOTE_SIGNATURE_URL = REMOTE_BASE + "update.sig"
REMOTE_UPDATER_URL = REMOTE_BASE + "self_update/self_update.py"
DOWNLOADED_UPDATER = os.path.join(BASE_DIR, "self_update_temp.py")

TRUSTED_HMAC_KEY_HASH = "68744b481da7f61d3bf46253d668007c5dca0ff3c033e72f2cf9be4df681ecec"

# ─────────────────────────────────────────────────────────────

def log_update(msg):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(UPDATE_LOG, "a") as f:
        f.write(f"{timestamp} {msg}\n")
    print(f"[UPDATE] {msg}")

def read_local_version():
    if not os.path.exists(LOCAL_VERSION_FILE):
        return "0.0.0"
    with open(LOCAL_VERSION_FILE, "r") as f:
        return f.read().strip()

def fetch_remote_file(url):
    try:
        r = requests.get(url, timeout=5)
        return r.text.strip() if r.status_code == 200 else None
    except Exception as e:
        log_update(f"Error fetching {url}: {e}")
        return None

def verify_signature(manifest_text, signature, provided_key):
    try:
        test_sig = hmac.new(provided_key.encode(), manifest_text.encode(), hashlib.sha256).hexdigest()
        return test_sig == signature
    except Exception:
        return False

def hash_key(key):
    return hashlib.sha256(key.encode()).hexdigest()

# ─────────────────────────────────────────────────────────────

def check_and_trigger_update():
    local_version = read_local_version()
    remote_version = fetch_remote_file(REMOTE_VERSION_URL)
    manifest_text = fetch_remote_file(REMOTE_MANIFEST_URL)
    signature = fetch_remote_file(REMOTE_SIGNATURE_URL)

    if not remote_version or not manifest_text or not signature:
        log_update("Update check failed: Could not retrieve remote files.")
        return

    if local_version == remote_version:
        log_update("Already up to date.")
        return

    log_update(f"New version detected: {remote_version} (Local: {local_version})")

    # Secure verification
    print("🔐 Verifying update authenticity...")
    update_key = input("Enter update key to proceed: ").strip()
    key_hash = hash_key(update_key)

    if key_hash != TRUSTED_HMAC_KEY_HASH:
        log_update("❌ Invalid update key. Update aborted.")
        return

    if not verify_signature(manifest_text, signature, update_key):
        log_update("❌ Signature verification failed. Update aborted.")
        return

    log_update("✅ Signature verified. Downloading updater...")

    # Download self_update.py
    try:
        r = requests.get(REMOTE_UPDATER_URL)
        if r.status_code == 200:
            with open(DOWNLOADED_UPDATER, "wb") as f:
                f.write(r.content)
            log_update("Updater downloaded. Executing...")

            subprocess.run(["python", DOWNLOADED_UPDATER])

        else:
            log_update(f"Failed to download self_update.py: HTTP {r.status_code}")
    except Exception as e:
        log_update(f"Error running self_update.py: {e}")
