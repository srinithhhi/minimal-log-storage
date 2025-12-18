from privacy_filter import apply_privacy_filters
from crypto_utils import encrypt_log, generate_mac
from datetime import datetime


def process_log(raw_log: str) -> dict:
    """
    Processes a raw log entry through:
    1. Privacy filtering
    2. Encryption
    3. MAC generation
    """

    # Step 1: Apply privacy filters (masking)
    filtered_log = apply_privacy_filters(raw_log)

    # Step 2: Encrypt the filtered log
    encrypted_log = encrypt_log(filtered_log)

    # Step 3: Generate MAC for integrity
    mac = generate_mac(filtered_log)

    # Step 4: Create secure log object
    secure_log = {
        "timestamp": datetime.utcnow().isoformat(),
        "encrypted_log": encrypted_log.decode(),  # store as string
        "mac": mac
    }

    return secure_log
