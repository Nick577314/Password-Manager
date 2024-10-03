from PyQt5.QtWidgets import QMainWindow , QApplication
import sys
# from Authenticate import authenticate

from passwordManager.gui_menu import PasswordManagerApp


def main():
    """Main function to start the application after authentication."""
    app = QApplication(sys.argv)
    window = PasswordManagerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
