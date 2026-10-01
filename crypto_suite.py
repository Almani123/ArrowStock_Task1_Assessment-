"""
Arrowstack Task 1
Cryptographic Encryption & Hashing Suite
AES-GCM, RSA-OAEP, SHA-256

Educational/lab project. Uses modern authenticated AES-GCM and RSA-OAEP.
"""

import argparse
import base64
import hashlib
import os
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def b64e(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def b64d(data: str) -> bytes:
    return base64.b64decode(data.encode("ascii"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def aes_encrypt(text: str, key: bytes) -> str:
    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, text.encode("utf-8"), None)
    return b64e(nonce + ciphertext)


def aes_decrypt(token: str, key: bytes) -> str:
    raw = b64d(token)
    nonce, ciphertext = raw[:12], raw[12:]
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")


def generate_aes_key() -> bytes:
    return AESGCM.generate_key(bit_length=256)


def generate_rsa_keypair(private_path="keys/private_key.pem",
                         public_path="keys/public_key.pem") -> None:
    Path(private_path).parent.mkdir(parents=True, exist_ok=True)
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    Path(private_path).write_bytes(
        private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
    )
    Path(public_path).write_bytes(
        public_key.public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )


def load_private_key(path="keys/private_key.pem"):
    return serialization.load_pem_private_key(
        Path(path).read_bytes(), password=None
    )


def load_public_key(path="keys/public_key.pem"):
    return serialization.load_pem_public_key(Path(path).read_bytes())


def rsa_encrypt(text: str, public_path="keys/public_key.pem") -> str:
    public_key = load_public_key(public_path)
    ciphertext = public_key.encrypt(
        text.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return b64e(ciphertext)


def rsa_decrypt(token: str, private_path="keys/private_key.pem") -> str:
    private_key = load_private_key(private_path)
    plaintext = private_key.decrypt(
        b64d(token),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext.decode("utf-8")


def self_test() -> None:
    print("=== Cryptographic Suite Self-Test ===")

    message = "Arrowstack cybersecurity lab"
    aes_key = generate_aes_key()
    aes_token = aes_encrypt(message, aes_key)
    assert aes_decrypt(aes_token, aes_key) == message
    print("[PASS] AES-GCM encryption/decryption")

    generate_rsa_keypair()
    rsa_token = rsa_encrypt(message)
    assert rsa_decrypt(rsa_token) == message
    print("[PASS] RSA-OAEP encryption/decryption")

    digest = sha256_text(message)
    assert len(digest) == 64
    print("[PASS] SHA-256 hashing")

    print("\nAll self-tests passed.")


def main():
    parser = argparse.ArgumentParser(description="AES/RSA/SHA-256 security suite")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--hash", metavar="TEXT")
    parser.add_argument("--aes-demo", metavar="TEXT")
    parser.add_argument("--rsa-demo", metavar="TEXT")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    if args.hash is not None:
        print("SHA-256:", sha256_text(args.hash))

    if args.aes_demo is not None:
        key = generate_aes_key()
        token = aes_encrypt(args.aes_demo, key)
        print("AES-GCM key (Base64):", b64e(key))
        print("Ciphertext (Base64):", token)
        print("Decrypted:", aes_decrypt(token, key))

    if args.rsa_demo is not None:
        generate_rsa_keypair()
        token = rsa_encrypt(args.rsa_demo)
        print("RSA-OAEP ciphertext (Base64):", token)
        print("Decrypted:", rsa_decrypt(token))

    if not any([args.self_test, args.hash, args.aes_demo, args.rsa_demo]):
        parser.print_help()


if __name__ == "__main__":
    main()
