
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, \
    QPushButton, QLineEdit, QSizePolicy, QSpacerItem

from passwordManager.gui.login_page import loginpage
from passwordManager.gui.signup_page import signuppage


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 500, 500)
        self.login_page = loginpage(self)
        self.signup_page= signuppage(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Manager")
        self.layout = QVBoxLayout()

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        self.signup_button = QPushButton("Sign Up ")
        self.signup_button.clicked.connect(self.signup)
        self.layout.addWidget(self.signup_button, alignment=Qt.AlignCenter)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)
        # Set the main widget and layout
        central_widget = QWidget(self)  # Create a central widget for the QMainWindow
        central_widget.setLayout(self.layout)

        self.setCentralWidget(central_widget)  # Set the central widget
        self.resize(300, 200)

    def login(self):
        self.login_page = loginpage(self)  # Pass reference to the main window
        self.login_page.show()
        self.close()

    def signup(self):
        self.signup_page = signuppage(self)
        self.signup_page.show()
        self.hide()










