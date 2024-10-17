from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

from passwordManager.database_connect import store_info
from passwordManager.encryption_handler import encryption_key
from passwordManager.helper import UserSession


class NewEntries(QWidget):
    def __init__(self, main_window, user_session: UserSession):
        super().__init__()
        self.main_window = main_window
        self.user_session = user_session

        self.initUI()

    def initUI(self):
        self.setWindowTitle("New Entries")
        self.layout = QVBoxLayout()

        self.platform_input = QLineEdit()
        self.platform_input.setPlaceholderText("Enter the platform: ")
        self.layout.addWidget(self.platform_input)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username: ")
        self.layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password: ")
        self.layout.addWidget(self.password_input)

        # Create a button to submit the new entry
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_entries)
        self.layout.addWidget(self.submit_button)


        self.back_button = QPushButton("Back to main menu " )
        self.back_button.clicked.connect(self.back_to_main_menu)
        self.layout.addWidget(self.back_button)


        self.setLayout(self.layout)


    def back_to_main_menu(self):
        #Closing the existing window
        #Go back to the initial window
        self.main_window.show()
        self.close()


    def submit_entries(self):
        user_id = self.user_session.user_id
        username = self.username_input.text()
        password = self.password_input.text()
        platform = self.platform_input.text()

        try:
            store_info(user_id,username,password,platform,encryption_key)
            print("submission successful!")
            self.main_window.show()
            self.close()
        except Exception as e:
            print(f"Failed to submit entries: {e}")