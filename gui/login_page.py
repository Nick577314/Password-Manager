from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

from passwordManager.gui.main_menu import MainMenu
from passwordManager.helper import UserSession, show_message
from passwordManager.setup import login_user


class loginpage(QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.user_session = UserSession()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Login Page")
        self.layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username: ")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password: ")
        self.layout.addWidget(self.password_input)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login_submit)
        self.layout.addWidget(self.login_btn)

        self.back_button = QPushButton("Back to main page ")
        self.back_button.clicked.connect(self.back_to_main_page)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def login_submit(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Attempt to log in and get the user_id
        user_id = login_user(username, password)
        if user_id:
            self.user_session.user_id = user_id  # Store the user_id in the session
            print(f"User logged in with user_id: {user_id}")  # Debug log
            show_message("Success", "Login successful")
            self.switch_to_main_menu()  # Switch to main menu on successful login
        else:
            show_message( "Error", "Login failed. Please check your username and password.")

    def switch_to_main_menu(self):
        try:
            self.main_menu = MainMenu(self.user_session)  # Create an instance of the MainMenu
            self.close()  # Close the current window
            self.main_menu.show()  # Show the main menu

        except Exception as e:
            print(f"Error while switching to main menu: {e}")  # Print the error message
            show_message("Error", "An error occurred while switching to the main menu.")


    def back_to_main_page(self):
        #Closing the existing window
        #Go back to the initial window
        self.main_window.show()
        self.close()