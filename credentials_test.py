
  
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

    def test_save_credentials(self):
        """
        test_save_credentials test case to test if the credentials object is saved into
            the credentials list
        """
        self.new_credentials.save_credentials()  # saving the new contact
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credentials.credentials_list = []

    def test_save_multiple_contact(self):
        """
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our credentials list
        """
        self.new_credential.save_credential()
        test_credentials = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")  # new contact
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        """
        test_delete_credentials to test if we can remove a credentials from the credentials list
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  # Deleting a contact object
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def test_find_by_platform(self):
        """
        test to check if we can find a credential by platform name and display information
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_platform("Bitbucket")

        self.assertEqual(found_credentials.platform, test_credentials.platform)

    def test_credentials_exists(self):
        """
        test to check if we can return a Boolean  if we cannot find the credential.
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
        test_credentials.save_credentials()

        self.assertTrue(Credentials.credentials_exists("Bitbucket"))
    
    def test_display_credentials(self):
        """
        method that returns a list of all saved credentials
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
    
    def test_copy_password(self):
        """
        Test to confirm that we are copying the password from a found credential
        """

        self.new_credentials.save_credentials()
        Credentials.copy_password("Github")

        self.assertEqual(self.new_credentials.password,pyperclip.paste())

    def test_generate_password(self):
        """
        Test to confirm that the password we are generating are the desired length
        """
        self.new_credentials.save_credentials()
        generated_password = Credentials.generate_password(12)
        test_credentials = Credentials("Bitbucket", "user2", "u@u.com", generated_password)
        test_credentials.save_credentials()

        self.assertEqual(len(test_credentials.password),12)

if __name__ == "__main__":
    unittest.main()