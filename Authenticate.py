from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QLineEdit
from secret_key import secret_key
from create_hash import verify_password
import logging
import sys

def authenticate():
    """Authenticate user with master password using a GUI popup."""
    try:
        # Create the application object; only one QApplication instance is allowed.
        app = QApplication(sys.argv)

        # Input password for authentication using QInputDialog
        passw, ok = QInputDialog.getText(None, "Authentication", "Please provide the master password:", QLineEdit.Password)

        if ok and passw:
            # Verify the plaintext password with the hashed master password

            if verify_password(secret_key, passw):
                logging.info('User authentication was successful')
                QMessageBox.information(None, "Success", "You're authenticated!")
                return True
            else:
                logging.warning('User authentication has failed')
                QMessageBox.critical(None, "Error", "Authentication failed. Wrong password.")
                return False
        else:
            QMessageBox.critical(None, "Error", "No password entered.")
            return False

    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred during authentication: {e}")
        return False


