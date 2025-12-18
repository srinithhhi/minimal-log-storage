import hashlib
import hmac
from config import fernet, MAC_KEY

# -------------------------------
# Hashing (SHA-256)
# -------------------------------
def hash_data(data: str) -> str:
    """
    Hashes data using SHA-256.
    Used for irreversible identifiers.
    """
    return hashlib.sha256(data.encode()).hexdigest()


# -------------------------------
# Encryption (AES - Fernet)
# -------------------------------
def encrypt_log(log_text: str) -> bytes:
    """
    Encrypts log text using AES (Fernet).
    """
    return fernet.encrypt(log_text.encode())


def decrypt_log(encrypted_log: bytes) -> str:
    """
    Decrypts encrypted log text.
    """
    return fernet.decrypt(encrypted_log).decode()


# -------------------------------
# Message Authentication Code
# -------------------------------
def generate_mac(message: str) -> str:
    """
    Generates HMAC-SHA256 for log integrity.
    """
    mac = hmac.new(MAC_KEY, message.encode(), hashlib.sha256)
    return mac.hexdigest()


def verify_mac(message: str, received_mac: str) -> bool:
    """
    Verifies message integrity using MAC.
    """
    expected_mac = generate_mac(message)
    return hmac.compare_digest(expected_mac, received_mac)