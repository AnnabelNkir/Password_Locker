
  
import unittest
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the contact class behaviours.
    Args:
        unittest.TestCase: Inherits the testCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("Github", "user101", "user101@email", "QwerY23")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.platform, "Github")
        self.assertEqual(self.new_credentials.username, "user101")
        self.assertEqual(self.new_credentials.email, "user101@email")
        self.assertEqual(self.new_credentials.password, "QwerY23")
    