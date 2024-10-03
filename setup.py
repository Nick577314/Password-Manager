from operator import truediv

from passwordManager.password_hashing import make_password, verify_password
import psycopg2
from database_connect import connect

def register_new_users(username: str, plaintext_password: str, email: str):
    hashed_password = make_password(plaintext_password)
    try:
        connection = connect()
        cursor = connection.cursor()
        insert_query = """INSERT INTO users (username, hashed_password, email) VALUES( %s,%s,%s)"""
        record_to_insert = (username,hashed_password,email)
        cursor.execute(insert_query,record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def login_user(username: str , input_password: str):

    try:
        connection = connect()
        cursor = connection.cursor()
        select_query = """SELECT hashed_password FROM users WHERE username = %s"""
        record_to_select = (username)
        cursor.execute(select_query,record_to_select)
        result = cursor.fetchone()

        if result: # if there is a result it goes inside the if statement else returns username not found
            stored_hashed_password = result[0]
            if verify_password(stored_hashed_password,input_password):
                print("Login Successful.")
                return True
            else:
                print("Login Unsuccessful.")
                return False
        else:
            print("Username not found.")
            return False

    except (Exception, psycopg2.Error) as error:
        print(error)

