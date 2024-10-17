import unittest
from unittest.mock import patch, MagicMock
from passwordManager.setup import register_new_users, login_user

class TestUserFunctions(unittest.TestCase):

    @patch('passwordManager.setup.connect')
    @patch('bcrypt.checkpw')  # Mock bcrypt checkpw to return True
    #'passwordManager.setup.connect': This is the target you want to replace with a mock. Here, you are replacing the connect function used to interact with the PostgreSQL database with a mock that simulates the database connection behavior.
    #'bcrypt.checkpw': You’re replacing the bcrypt.checkpw function (which compares hashed passwords) with a mock that always returns True, simulating a successful password verification.
    def test_register_new_users(self, mock_bcrypt, mock_connect):
        # Mock the connection and cursor
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        # Call the function
        register_new_users('testuser', 'testpassword', 'test@example.com')

        # Assertions to ensure the correct SQL queries were executed
        mock_cursor.execute.assert_called_once()
        mock_connection.commit.assert_called_once()

    @patch('passwordManager.setup.connect')
    @patch('bcrypt.checkpw', return_value=True) # you want to similuate a
    def test_login_user_success(self, mock_bcrypt, mock_connect):
        # Simulate the database returning a valid hashed password
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ['$2b$12$ExampleHashHere']  # Provide a valid bcrypt hash

        # Call the function
        result = login_user('testuser', 'testpassword')

        # Assertions
        self.assertTrue(result)
        mock_cursor.execute.assert_called_once()

if __name__ == '__main__':
    unittest.main()

