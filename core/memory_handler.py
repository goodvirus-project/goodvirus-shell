import os
import json
import hashlib
import datetime
import random
import string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_FILE = os.path.join(BASE_DIR, ".gv_memory.json")

def _generate_id():
    return "GV-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

def _get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _calculate_hash(file_path):
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_memory(memory):
    try:
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)
    except Exception as e:
        print(f"[GooDViruS™] [MEMORY ERROR] Could not save memory: {e}")

def remember_file(file_path):
    memory = load_memory()
    file_hash = _calculate_hash(file_path)
    if not file_hash:
        return None  # Skip unhashable

    for entry in memory:
        if entry["hash"] == file_hash:
            if entry["last_known_name"] != file_path:
                entry["last_known_name"] = file_path
                save_memory(memory)
                return {"renamed": True, "entry": entry}
            return {"renamed": False, "entry": entry}

    # If new file, add it
    new_entry = {
        "hash": file_hash,
        "original_name": file_path,
        "last_known_name": file_path,
        "first_seen": _get_timestamp(),
        "id": _generate_id()
    }
    memory.append(new_entry)
    save_memory(memory)
    return {"new": True, "entry": new_entry}

def get_known_hashes():
    memory = load_memory()
    return [entry["hash"] for entry in memory]

def get_entry_by_hash(file_hash):
    memory = load_memory()
    for entry in memory:
        if entry["hash"] == file_hash:
            return entry
    return None