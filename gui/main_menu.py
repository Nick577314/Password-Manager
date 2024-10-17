from PyQt5.QtWidgets import QWidget, QSizePolicy, QPushButton, QVBoxLayout, QSpacerItem
from PyQt5.QtCore import Qt

from passwordManager.gui.new_entry_page import NewEntries
from passwordManager.gui.search_page import SearchExisting
from passwordManager.helper import UserSession


class MainMenu(QWidget):
    def __init__(self, user_session: UserSession):
        super().__init__()
        self.setGeometry(600, 300, 500, 500)
        self.user_session = user_session
        self.user_id = self.user_session.user_id  # Get the user_id from session
        self.initUI()

    def initUI(self):
        if self.user_session.is_logged_in():  # Check if user is logged in
            print(f"User ID: {self.user_session.user_id}")  # Use user_id from the session
        else:
            print("No user is logged in.")

        self.setWindowTitle("Main Menu")
        self.layout = QVBoxLayout()

        # adding a spacer surrounding the buttons so that its in the middle
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)
        # Create a button to open the new entry window
        self.open_newentry_btn = QPushButton("Add Passwords", self)
        self.open_newentry_btn.clicked.connect(self.open_new_entries)
        self.layout.addWidget(self.open_newentry_btn, alignment= Qt.AlignCenter)

        # Create a button to open the search existing window (optional)
        self.open_search_btn = QPushButton("Search for existing passwords", self)
        self.open_search_btn.clicked.connect(self.open_search_existing)
        self.layout.addWidget(self.open_search_btn,alignment= Qt.AlignCenter)
        # adding a spacer surrounding the buttons so that its in the middle
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        # Set the main widget and layout
        self.setLayout(self.layout)


    def open_new_entries(self):
        self.new_entries = NewEntries(self, self.user_session)  # Pass reference to the main window
        self.new_entries.show()
        self.hide()  # Hide the main window

    def open_search_existing(self):
        self.search_existing = SearchExisting(self)  # Pass reference to the main window
        self.search_existing.show()
        self.hide()