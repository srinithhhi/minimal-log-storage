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
HASH_ALGORITHM = "SHA256"   # Used for irreversible hashing

# Generate this once and keep it secret
ENCRYPTION_KEY = Fernet.generate_key()
fernet = Fernet(ENCRYPTION_KEY)

# MAC settings
MAC_KEY = b"super_secret_mac_key"

# -------------------------------
# Log Storage Configuration
# -------------------------------
LOG_FILE_PATH = "logs/secure_logs.json"
ENABLE_ENCRYPTION = True
ENABLE_MAC = True
