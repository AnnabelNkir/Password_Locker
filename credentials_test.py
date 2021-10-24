
  
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
