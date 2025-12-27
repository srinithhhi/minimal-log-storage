import streamlit as st
import os
import hashlib
from cryptography.fernet import InvalidToken

from log_processor import process_log
from log_storage import save_log, load_logs, delete_log
from crypto_utils import decrypt_log, verify_mac

# -------------------------------
# Session state
# -------------------------------
if "delete_success" not in st.session_state:
    st.session_state.delete_success = False

# -------------------------------
# Admin password verification
# -------------------------------
def verify_admin_password(input_password: str) -> bool:
    stored_hash = os.getenv("ADMIN_PASSWORD_HASH")
    if not stored_hash:
        return False

    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_hash == stored_hash

# -------------------------------
# Streamlit config
# -------------------------------
st.set_page_config(
    page_title="Minimal Log Storage with Privacy Filters",
    layout="centered"
)

st.title("🔐 Minimal Log Storage with Privacy Filters")

st.write(
    "Privacy-preserving log storage using hashing, AES encryption (Fernet), "
    "and Message Authentication Codes (MAC)."
)

# -------------------------------
# Log input section
# -------------------------------
st.subheader("📥 Enter Raw Log")

raw_log = st.text_area(
    "Log Entry",
    placeholder="Example: User john.doe@gmail.com logged in from IP 192.168.1.25"
)

if st.button("Process & Store Log"):
    if raw_log.strip():
        secure_log = process_log(raw_log)
        save_log(secure_log)
        st.success("✅ Log processed and stored securely")
    else:
        st.warning("⚠️ Please enter a log message")

# -------------------------------
# View stored logs
# -------------------------------
st.subheader("📂 Stored Secure Logs")

logs = load_logs()

if not logs:
    st.info("No logs stored yet.")
    st.stop()

# Show delete success message (after rerun)
if st.session_state.delete_success:
    st.success("🗑 Log deleted successfully")
    st.session_state.delete_success = False

# Select log
selected_index = st.radio(
    "Select a log entry",
    options=list(range(len(logs))),
    format_func=lambda i: f"Log {i + 1} | {logs[i]['timestamp']}"
)

selected_log = logs[selected_index]

# -------------------------------
# Admin-only decryption
# -------------------------------
st.subheader("🔑 Admin Decryption")

admin_password = st.text_input(
    "Admin Password",
    type="password"
)

if st.button("Decrypt Selected Log"):
    if not verify_admin_password(admin_password):
        st.error("❌ Incorrect admin password")
        st.stop()

    try:
        decrypted = decrypt_log(
            selected_log["encrypted_log"].encode()
        )
        mac_valid = verify_mac(decrypted, selected_log["mac"])

        st.success("🔓 Decryption Successful")
        st.write("**Decrypted Log:**")
        st.write(decrypted)
        st.write("**MAC Valid:**", mac_valid)

    except InvalidToken:
        st.error("❌ Decryption failed (invalid key or tampered data)")

# -------------------------------
# Admin log deletion
# -------------------------------
st.subheader("🗑 Log Deletion")

delete_password = st.text_input(
    "Admin Password (for deletion)",
    type="password",
    key="delete_pwd"
)

if st.button("Delete Selected Log"):
    if not verify_admin_password(delete_password):
        st.error("❌ Incorrect admin password")
        st.stop()

    delete_log(selected_index)
    st.session_state.delete_success = True
    st.rerun()
