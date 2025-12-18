# Minimal Log Storage with Privacy Filters 

## Overview
This project is a **privacy-focused log storage system** implemented entirely in Python. It combines concepts from classical and modern cryptography to securely handle log data while minimizing sensitive information exposure.

### Key Features
- **Privacy Filtering:** Masks emails and IP addresses before storage.
- **Hashing:** SHA-256 used for irreversible identifiers.
- **Encryption:** AES (Fernet) symmetric encryption for confidentiality.
- **Integrity Verification:** HMAC-SHA256 to ensure logs are not tampered with.
- **Persistent Storage:** Securely stores logs in JSON format.
- **Streamlit Frontend:** Easy-to-use UI for entering and viewing logs.

### Crypto Concepts Used
- Substitution & Product Cipher (Privacy Filter)
- Cryptographic Hash Functions (SHA-256)
- Block Cipher (AES/Fernet)
- Message Authentication Codes (HMAC)

### Installation
```bash
git clone <repo_url>
cd minimal-log-storage
python -m venv crypto_env
source crypto_env/bin/activate  # Mac/Linux
crypto_env\Scripts\activate     # Windows
pip install -r requirements.txt
streamlit run app.py
