
from PyQt5.QtWidgets import QMessageBox


from passwordManager.setup import login_user


def show_message( title: str, message: str):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(QMessageBox.Information)  # For info messages; can be changed to Warning, Critical, etc.
    msg.exec_()

class UserSession:

    def __init__(self):
        self.user_id = None

    def login(self, username: str, password: str):
        try:
            user_id = login_user(username, password)

            if user_id is not None:
                self.user_id = user_id
                show_message("Success", "Login was successful")  # Use the show_message function
                print(f"User logged in with user_id: {self.user_id}")  # Debugging line
                return True
            else:
                show_message("Error", "Login failed.")
                return False
        except Exception as e:
            show_message("Error", f"An error occurred: {e}")
            return False

    def logout(self):
        show_message("Logging Out", "Logging current user out")
        self.user_id = None
        print("User logged out")

    def is_logged_in(self):
        return self.user_id is not None
