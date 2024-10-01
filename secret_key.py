from passwordManager.create_hash import generate_secret_key
from cryptography.fernet import Fernet

import base64


encryption_key = Fernet.generate_key()
print(encryption_key)
#base64
def encrypt_password(password: str, encryption_key: bytes):
    # Ensure the password is encoded to bytes
    password_bytes = password.encode()
    cipher_suite = Fernet(encryption_key)
    encrypted_pwd = cipher_suite.encrypt(password_bytes)
    return base64.urlsafe_b64encode(encrypted_pwd).decode('utf-8')

def decrypt_password(encrypted_pwd_str: str, encryption_key: bytes):
    encrypted_pwd_bytes = base64.urlsafe_b64decode(encrypted_pwd_str.encode('utf-8'))
    cipher_suite = Fernet(encryption_key)
    try:
        decrypted_value = cipher_suite.decrypt(encrypted_pwd_bytes)
    except Exception as e:
        print(f"Decryption failed: {e}")
        return None
    return decrypted_value.decode()

### WAS TESTING ###
# password = "my_secure_password"
# encrypted_password = encrypt_password(password, encryption_key)
# print("Encrypted:", encrypted_password)
#
# decrypted_password = decrypt_password(encrypted_password, encryption_key)
# print("Decrypted:", decrypted_password)