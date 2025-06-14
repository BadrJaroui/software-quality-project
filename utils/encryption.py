# pip install cryptography python-dotenv

import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_private_key(private_key, filename="private_key.pem", password=None, secrets_dir="secrets"):
    os.makedirs(secrets_dir, exist_ok=True)
    filepath = os.path.join(secrets_dir, filename)
    encoding = serialization.Encoding.PEM
    format = serialization.PrivateFormat.PKCS8
    encryption_algorithm = serialization.NoEncryption()

    if password:
        encryption_algorithm = serialization.BestAvailableEncryption(password.encode())

    with open(filepath, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=encoding,
            format=format,
            encryption_algorithm=encryption_algorithm
        ))
    print(f"Private key saved to {filepath}")

def load_private_key(filename="private_key.pem", password=None, secrets_dir="secrets"):
    """Loads a private key from a file."""
    filepath = os.path.join(secrets_dir, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Private key file not found at {filepath}")
    with open(filepath, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=password.encode() if password else None,
            backend=default_backend()
        )
    return private_key

def save_public_key(public_key, filename="public_key.pem", secrets_dir="secrets"):
    os.makedirs(secrets_dir, exist_ok=True)
    filepath = os.path.join(secrets_dir, filename)
    with open(filepath, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    print(f"Public key saved to {filepath}")

def load_public_key(filename="public_key.pem", secrets_dir="secrets"):
    filepath = os.path.join(secrets_dir, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Public key file not found at {filepath}")
    with open(filepath, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )
    return public_key

def encrypt_message(public_key, message):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_message(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

if __name__ == "__main__":
    load_dotenv()
    private_key_password = os.getenv("private_key_password")

    if not private_key_password:
        print("Error: PRIVATE_KEY_PASSWORD not found in .env file. Please set it.")
    else:
        # 1. Generate RSA key pair
        print("Generating RSA key pair...")
        private_key, public_key = generate_rsa_key_pair()
        print("Key pair generated.")

        # 2. Save keys to the 'secrets' folder
        save_private_key(private_key, password=private_key_password)
        save_public_key(public_key)

        # 3. Load Keys (simulating loading for a new session or different party)
        print("\nLoading keys from files in 'secrets' folder...")
        try:
            loaded_private_key = load_private_key(password=private_key_password)
            loaded_public_key = load_public_key()
            print("Keys loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error loading keys: {e}. Ensure keys are generated and in the 'secrets' folder.")
            exit() # Exit if keys can't be loaded

        # 4. Define the message
        original_message = "This is a very secret message that needs to be encrypted!"
        print(f"\nOriginal Message: {original_message}")

        # 5. Encrypt the message using the public key
        print("Encrypting message...")
        encrypted_msg = encrypt_message(loaded_public_key, original_message)
        print(f"Encrypted Message (bytes): {encrypted_msg}")

        # 6. Decrypt the message using the private key
        print("Decrypting message...")
        decrypted_msg = decrypt_message(loaded_private_key, encrypted_msg)
        print(f"Decrypted Message: {decrypted_msg}")

        # Verify
        if original_message == decrypted_msg:
            print("\nEncryption and Decryption successful! The messages match.")
        else:
            print("\nError: Decrypted message does not match original message.")
