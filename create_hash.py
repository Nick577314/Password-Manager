from hashlib import sha256
import random

from passwordManager.password import plaintext_pwd

def make_password(plaintext):
    # Create a random salt for the master password
    salt = generate_salt()
    hsh = get_hexdigest(salt, plaintext)
    return ''.join((salt, hsh))


def get_hexdigest(salt, plaintext):
    return sha256((salt + plaintext).encode('utf-8')).hexdigest()

def generate_salt(length=20):
    """Generate a random salt of specified length."""
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


def generate_secret_key():

    # You can directly define the master password here
    plaintext_master_password =  plaintext_pwd
    return make_password(plaintext_master_password)

def verify_password(stored_hashed_password, input_password):
    """Verify an input password against the stored hashed password."""
    salt = stored_hashed_password[:20]  # Extract the first 20 characters (the salt)
    hsh = get_hexdigest(salt, input_password) # Hash the input password with the extracted salt

    return stored_hashed_password == ''.join((salt, hsh))  # Compare the stored and input hashes
