from PyQt5.QtWidgets import QMainWindow , QApplication
import sys
from Authenticate import authenticate
from PyQt5.QtGui import QIcon

from passwordManager.gui_menu import PasswordManagerApp


def main():
    """Main function to start the application after authentication."""
    # Authenticate the user
    if not authenticate():
        exit()

    # If authentication is successful, start the GUI application
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
