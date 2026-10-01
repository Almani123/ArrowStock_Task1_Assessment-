# Arrowstack Task 1 — Cryptographic Encryption & Hashing Suite

**Student:** Abdul Rehman
**Internship:** Cyber Security — Intermediate / Technical Track
**Task:** Cryptographic Encryption & Hashing Suite (AES, RSA, SHA-256)
**Date:** 1-10-2026

## 1. Objective

The objective of this project was to implement and validate a Python-based educational cryptographic suite demonstrating AES symmetric encryption, RSA asymmetric encryption, and SHA-256 hashing.

## 2. Scope

The project was executed in a local educational/laboratory environment using test messages. No production credentials, private organizational data, or real secrets were used.

## 3. Environment

- Operating system: [Windows/Linux/macOS]
- Python version: [RUN `python --version`]
- IDE/editor: [VS Code/etc.]
- Python package: `cryptography` [VERSION]

## 4. AES-256-GCM

AES was implemented as symmetric authenticated encryption using AES-256-GCM. A randomly generated nonce is combined with the ciphertext for the demonstration. The test verifies that decrypting the generated ciphertext returns the original plaintext.

**Evidence:** Insert `screenshots/aes.png`.

## 5. RSA-2048-OAEP

RSA was implemented as asymmetric encryption using a 2048-bit key pair and OAEP padding with SHA-256. The public key is used for encryption and the private key for decryption.

**Evidence:** Insert `screenshots/rsa.png`.

**Security note:** Never publish the private key. The repository `.gitignore` excludes `keys/private_key.pem`.

## 6. SHA-256

SHA-256 was used to generate a fixed-length cryptographic digest from a test message. Hashing is one-way and is not the same as reversible encryption.

**Evidence:** Insert `screenshots/sha256.png`.

## 7. Validation

Run:

`python crypto_suite.py --self-test`

Record the actual output below:

```text
[PASTE ACTUAL SELF-TEST OUTPUT HERE]
```

Expected validation categories are AES encryption/decryption, RSA encryption/decryption and SHA-256 digest generation. Do not claim PASS until the local command actually passes.

## 8. Security Considerations

- Private keys must not be committed to source control.
- Authenticated encryption is preferable to unauthenticated encryption for application data.
- SHA-256 alone should not be used for password storage; password storage requires a dedicated password-hashing/KDF approach.
- Real secrets should not be placed in screenshots or public repositories.

## 9. Limitations

This project is an educational demonstration rather than a production key-management system. It does not implement enterprise key rotation, hardware-backed key storage, certificate management, access-control policy, or full secure secret management.

## 10. Conclusion

The project demonstrates practical use of symmetric encryption, asymmetric encryption and cryptographic hashing and validates the core operations with automated tests.
