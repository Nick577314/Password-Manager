from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

from passwordManager.database_connect import find_info
from passwordManager.helper import UserSession, show_message
from passwordManager.encryption_handler import encryption_key

class SearchExisting(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.user_session = UserSession()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Search for Account Info")
        self.layout = QVBoxLayout()


        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter the username: ")
        self.layout.addWidget(self.username_input)

        self.platform_input = QLineEdit()
        self.platform_input.setPlaceholderText("Enter the platform: ")
        self.layout.addWidget(self.platform_input)
        # Create a button to search for existing accounts
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search)
        self.layout.addWidget(self.search_button)

        self.back_button = QPushButton("Back to main menu ")
        self.back_button.clicked.connect(self.back_to_main_menu)
        self.layout.addWidget(self.back_button)

        # Set the layout for this window
        self.setLayout(self.layout)

    def back_to_main_menu(self):
        # Closing the existing window
        # Go back to the initial window
        self.main_window.show()
        self.close()


    def search(self):
        user_id = self.main_window.user_session.user_id
        username = self.username_input.text()
        platform = self.platform_input.text()
        password = find_info(user_id,platform,username ,encryption_key)
        if password is not None:
            show_message("Password found:" , f"The entered password is: {password}")
        else:
            show_message("Error:" ,"No password found for the specified username and platform.")