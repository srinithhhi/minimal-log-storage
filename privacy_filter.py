import re
from config import PRIVACY_FILTERS

# -------------------------------
# Regex Patterns
# -------------------------------
EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
IP_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


def mask_email(email: str) -> str:
    """
    Masks an email address using substitution.
    Example: john.doe@gmail.com -> j***@gmail.com
    """
    username, domain = email.split("@")
    return username[0] + "***@" + domain


def mask_ip(ip: str) -> str:
    """
    Masks an IP address.
    Example: 192.168.1.25 -> 192.168.xxx.xxx
    """
    parts = ip.split(".")
    return parts[0] + "." + parts[1] + ".xxx.xxx"


def apply_privacy_filters(log_text: str) -> str:
    """
    Detects and masks sensitive information in logs
    based on enabled privacy filters.
    """

    filtered_log = log_text

    # Mask email addresses
    if PRIVACY_FILTERS.get("email"):
        filtered_log = re.sub(
            EMAIL_PATTERN,
            lambda match: mask_email(match.group()),
            filtered_log
        )

    # Mask IP addresses
    if PRIVACY_FILTERS.get("ip_address"):
        filtered_log = re.sub(
            IP_PATTERN,
            lambda match: mask_ip(match.group()),
            filtered_log
        )

    return filtered_log
