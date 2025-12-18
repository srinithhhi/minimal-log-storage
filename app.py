import streamlit as st
from log_processor import process_log
from log_storage import save_log, load_logs
from crypto_utils import decrypt_log, verify_mac

st.set_page_config(page_title="Minimal Log Storage with Privacy Filters")

st.title("🔐 Minimal Log Storage with Privacy Filters")

st.write(
    "This application demonstrates privacy-preserving log storage "
    "using cryptographic techniques such as hashing, AES encryption, and MAC."
)

# -------------------------------
# Log Input Section
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
        st.success("✅ Log processed and stored securely!")
    else:
        st.warning("⚠️ Please enter a log message.")

# -------------------------------
# View Stored Logs
# -------------------------------
st.subheader("📂 Stored Secure Logs")

logs = load_logs()

if not logs:
    st.info("No logs stored yet.")
else:
    for i, log in enumerate(logs, start=1):
        with st.expander(f"Log Entry {i}"):
            st.write("**Timestamp:**", log["timestamp"])
            st.write("**Encrypted Log:**", log["encrypted_log"])
            st.write("**MAC:**", log["mac"])

            # Optional admin-only decryption
            if st.checkbox(f"Decrypt Log {i} (Admin Only)"):
                decrypted = decrypt_log(log["encrypted_log"].encode())
                mac_valid = verify_mac(decrypted, log["mac"])

                st.write("🔓 **Decrypted Log:**", decrypted)
                st.write("🛡 **MAC Valid:**", mac_valid)
