from PyQt5.QtWidgets import QMessageBox

from passwordManager.password_hashing import make_password, verify_password
import psycopg2
from passwordManager.database_connect import connect

current_user_id = None

def register_new_users(username: str, plaintext_password: str, email: str):
    hashed_password = make_password(plaintext_password)

    try:

        connection = connect()
        cursor = connection.cursor()
        # checks if username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))

        if cursor.fetchone():
            print("Username already exists. ")
            return False #username already exists

        insert_query = """INSERT INTO users (username, hashed_password, email) VALUES( %s,%s,%s)"""
        record_to_insert = (username,hashed_password,email)
        cursor.execute(insert_query,record_to_insert)
        connection.commit()
        return True


    except (Exception, psycopg2.Error) as error:

        print(f"Error: {error}")  # Print the error for debugging

        return False  # Registration failed

    finally:
        if connection:
            cursor.close()
            connection.close()


def login_user(username: str, input_password: str):
    try:
        connection = connect()
        cursor = connection.cursor()

        # Query to get both the hashed password and the user_id
        select_query = """SELECT user_id, hashed_password FROM users WHERE username = %s"""
        record_to_select = (username,)  # Ensure this is a tuple
        cursor.execute(select_query, record_to_select)
        result = cursor.fetchone()

        if result:
            user_id = result[0]  # Get the user_id
            stored_hashed_password = result[1]

            # Verify the input password against the stored hashed password
            if verify_password(stored_hashed_password, input_password):
                return user_id  # Return the user_id upon successful login
            else:
                return "Incorrect password."  # Return a message for incorrect password
        else:
            return "Username not found."  # Return a message for user not found

    except (Exception, psycopg2.Error) as error:
        return f"Database error: {error}"  # Return the error message for the caller
    finally:
        if cursor:
            cursor.close()  # Close cursor if it was opened
        if connection:
            connection.close()  # Ensure connection is closed






