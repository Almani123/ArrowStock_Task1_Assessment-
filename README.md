# Cryptographic Encryption & Hashing Suite

**Arrowstack Cyber Security Internship — Task 1**

A Python laboratory project demonstrating:
- AES-256-GCM symmetric encryption/decryption
- RSA-2048-OAEP asymmetric encryption/decryption
- SHA-256 one-way hashing
- Basic automated self-testing

## Important security note
This is an educational demonstration. The project deliberately uses AES-GCM
(authenticated encryption) and RSA-OAEP rather than obsolete/insecure modes.
Never commit `keys/private_key.pem` or real secrets to GitHub.

## Requirements
- Python 3.10+
- `pip install -r requirements.txt`

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run the self-test
```bash
python crypto_suite.py --self-test
```

## SHA-256 demonstration
```bash
python crypto_suite.py --hash "Arrowstack cybersecurity lab"
```

## AES demonstration
```bash
python crypto_suite.py --aes-demo "Confidential lab message"
```

## RSA demonstration
```bash
python crypto_suite.py --rsa-demo "RSA lab message"
```

## What each primitive demonstrates
| Primitive | Purpose | Reversible? |
|---|---|---|
| AES-GCM | Confidentiality + integrity | Yes |
| RSA-OAEP | Public-key encryption/key transport concept | Yes |
| SHA-256 | Integrity/fingerprint/password-hashing concept | No |

**Note:** SHA-256 is not password hashing by itself. Real password storage should use a
dedicated password-hashing/KDF such as Argon2id, scrypt, or PBKDF2.

## Evidence to capture
1. Project folder in VS Code.
2. `--self-test` showing all PASS results.
3. SHA-256 output.
4. AES encryption/decryption output.
5. RSA encryption/decryption output.
6. GitHub repository with README.

## Limitations
- This is a learning project, not a production key-management system.
- RSA is demonstrated with short text; large files should use hybrid encryption.
- Private-key protection and secure key storage are outside this small lab.

## Responsible use
Use only your own data and authorized lab systems.
