import unittest
import bcrypt
from passwordManager.password_hashing import make_password, verify_password


class TestPasswordFunctions(unittest.TestCase):

    def setUp(self):
        self.plaintext_password = "super_secret"
        self.hashed_password = make_password(self.plaintext_password)

    def test_make_password(self):
        hashed_password = make_password(self.plaintext_password)
        self.assertNotEqual(self.plaintext_password,hashed_password)
        self.assertTrue(bcrypt.checkpw(self.plaintext_password.encode('utf-8'),hashed_password.encode('utf-8')))

    def test_verify_password_success(self):
        """Test that `verify_password` returns True for the correct password."""
        result = verify_password(self.hashed_password, self.plaintext_password)
        self.assertTrue(result)


    def test_verify_password_failure(self):
        """Test that `verify_password` returns False for an incorrect password."""
        wrong_password = "wrong_password"
        result = verify_password(self.hashed_password, wrong_password)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()