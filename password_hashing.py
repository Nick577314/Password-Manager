from base64 import encode

import bcrypt
from passwordManager.password import plaintext_pwd

def make_password(plaintext: str):
    # Create a random salt for the master password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plaintext.encode('utf-8'),salt)
    return hashed_password.decode('utf-8')
# compares the already stored password for a user with the inputted password and then hashes and compares
def verify_password(stored_hashed_password: str,input_password: str) -> bool:
   return bcrypt.checkpw(input_password.encode('utf-8'),stored_hashed_password.encode('utf-8'))
