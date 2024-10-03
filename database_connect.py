import psycopg2
from passwordManager.encryption_handler import encrypt_password, encryption_key, decrypt_password
from passwordManager.password import plaintext_pwd

#function that is used to insert data into the table by a query and if it fails the appropriate error is printed to the terminal
def store_info( username:str ,password: str, platform_name: str):
    try:
        encrypted_pwd = encrypt_password(password,encryption_key)
        connection = connect()  # function to connect to your database
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (username, password, platform) VALUES (%s, %s, %s)"""
        record_to_insert = (username, encrypted_pwd, platform_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

#function to connect to the database based on the required criteria needed
def connect():
    try:
        connection = psycopg2.connect(user='nick', password=plaintext_pwd, host='127.0.0.1', port='2022', database='password_manager')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)
#function that searches return the password based on the username and platform given in the search boxes
def find_info(platform_name: str ,username: str ):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """SELECT password FROM accounts WHERE platform = %s AND username = %s"""
        cursor.execute(postgres_select_query, (platform_name, username))
        connection.commit()
        result = cursor.fetchone()
        if result:
            encrypted_pwd = result[0]
            decrypt_pwd = decrypt_password(encrypted_pwd,encryption_key)
            return decrypt_pwd
        else:
            return None

    except (Exception, psycopg2.Error) as error:
        print(error)
        return None

