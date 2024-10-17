from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

from passwordManager.gui.login_page import loginpage
from passwordManager.setup import register_new_users


class signuppage(QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Signup for Nick's Password Manager")
        self.layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email: ")
        self.layout.addWidget(self.email_input)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username: ")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password: ")
        self.layout.addWidget(self.password_input)

        self.signup_btn = QPushButton("Submit")
        self.signup_btn.clicked.connect(self.signup_submit)
        self.layout.addWidget(self.signup_btn)

        self.back_button = QPushButton("Back to main page ")
        self.back_button.clicked.connect(self.back_to_main_menu)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def signup_submit(self):
        email = self.email_input.text()
        username = self.username_input.text()
        password = self.password_input.text()


        if register_new_users(username,password,email):

            self.show_message("Success", "User registered successfully")
            self.switch_to_login_page()
        else:
            self.show_message("Error", "Registration failed. Username might already exist.")

    def switch_to_login_page(self):
        # Create an instance of the login page and show it
        login_page = loginpage(self.main_window)  # Pass the main window or a reference to it
        login_page.show()  # Show the login page
        self.close()

    def back_to_main_menu(self):
        #Closing the existing window
        #Go back to the initial window
        self.main_window.show()
        self.close()