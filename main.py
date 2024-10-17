from PyQt5.QtWidgets import QApplication
import sys
from passwordManager.gui.main_page import MainPage

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.exit()
    print("Uncaught exception:", exc_value)

def main():
    """Main function to start the application after authentication."""
    app = QApplication(sys.argv)

    # Optionally set the exception hook here if not already set in the global scope
    sys.excepthook = handle_exception

    window = MainPage()  # Adjust this if necessary based on your login flow
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

