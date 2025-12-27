import os
from cryptography.fernet import Fernet

# -------------------------------
# Privacy Filter Configuration
# -------------------------------
PRIVACY_FILTERS = {
    "email": True,
    "ip_address": True,
    "phone_number": False
}

# -------------------------------
# Cryptographic Configuration
# -------------------------------
HASH_ALGORITHM = "SHA256"

# Load persistent encryption key
ENCRYPTION_KEY = os.getenv("FERNET_SECRET_KEY")

if not ENCRYPTION_KEY:
    raise RuntimeError("FERNET_SECRET_KEY not set")

fernet = Fernet(ENCRYPTION_KEY.encode())

# MAC settings
MAC_KEY = os.getenv("MAC_SECRET_KEY").encode()

# -------------------------------
# Log Storage Configuration
# -------------------------------
LOG_FILE_PATH = "logs/secure_logs.json"
ENABLE_ENCRYPTION = True
ENABLE_MAC = True