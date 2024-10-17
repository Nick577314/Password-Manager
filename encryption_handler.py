
from cryptography.fernet import Fernet
import os

# Load the encryption key from a file
def load_encryption_key():
    if os.path.exists('encryption_key.key'):
        with open('encryption_key.key', 'rb') as key_file:
            return key_file.read()
    else:
        raise FileNotFoundError("Encryption key file not found.")

# Encrypt a password
def encrypt_password(password: str, encryption_key: bytes):
    password_bytes = password.encode('utf-8') # converts into bytes
    cipher_suite = Fernet(encryption_key)
    encrypted_pwd = cipher_suite.encrypt(password_bytes)
    return encrypted_pwd  # Return bytes directly

# Decrypt an encrypted password
def decrypt_password(encrypted_pwd_bytes: bytes, encryption_key: bytes):
    cipher_suite = Fernet(encryption_key)
    try:
        decrypted_value = cipher_suite.decrypt(encrypted_pwd_bytes)
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None
    return decrypted_value.decode() # converts bytes back into a string

# Load the encryption key when the module is imported
encryption_key = load_encryption_key()


