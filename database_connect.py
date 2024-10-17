import base64

import psycopg2
from passwordManager.encryption_handler import encrypt_password, decrypt_password
from passwordManager.password import plaintext_pwd


#function to connect to the database based on the required criteria needed
def connect():
    try:
        connection = psycopg2.connect(user='postgres', password=plaintext_pwd, host='127.0.0.1', port='2022', database='password_manager')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

#function that is used to insert data into the table by a query and if it fails the appropriate error is printed to the terminal
def store_info(user_id: int, username: str, password: str, platform_name: str, encryption_key: bytes):
    try:
        encrypted_pwd = encrypt_password(password, encryption_key)  # Use the encryption_key here
        # Ensure encrypted_pwd is stored as a string
        encrypted_pwd_str = base64.urlsafe_b64encode(encrypted_pwd).decode('utf-8')

        connection = connect()  # function to connect to your database
        cursor = connection.cursor()

        postgres_insert_query = """INSERT INTO passwords (user_id, username, encrypted_pwd, platform) VALUES (%s, %s, %s, %s)"""
        record_to_insert = (user_id, username, encrypted_pwd_str, platform_name)  # Use encrypted_pwd_str here
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print(error)



#function that searches return the password based on the user_id, username and platform given in the search boxes
def find_info(user_id: int, platform_name: str, username: str, encryption_key: bytes):
    try:
        connection = connect()  # Ensure this function properly connects to your database
        cursor = connection.cursor()

        # Query to select the encrypted password
        postgres_select_query = """SELECT encrypted_pwd FROM passwords 
                                   WHERE user_id = %s AND platform = %s AND username = %s"""
        cursor.execute(postgres_select_query, (user_id, platform_name, username))

        result = cursor.fetchone()  # Fetch the result directly

        # Check if a result was found
        if result:
            encrypted_pwd_str = result[0]
            # Decode the string to bytes before decrypting
            encrypted_pwd_bytes = base64.urlsafe_b64decode(encrypted_pwd_str.encode('utf-8'))
            # Decrypt the retrieved password
            decrypt_pwd = decrypt_password(encrypted_pwd_bytes, encryption_key)
            return decrypt_pwd
        else:
            return None  # No entry found for the given parameters

    except (Exception, psycopg2.Error) as error:
        print(f"Error fetching password for user_id {user_id}, platform '{platform_name}', username '{username}': {error}")
        return None
    finally:
        if cursor:
            cursor.close()  # Close the cursor if it was opened
        if connection:
            connection.close()  # Close the connection to the database


