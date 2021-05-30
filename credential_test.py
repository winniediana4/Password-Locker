import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
  """
 Test class that defines test cases for the credential class behaviours.
  """

  def setUp(self):
    """
    set_up method to run before each test case
    """
    self.new_credential = Credential("winnie", "facebook","deinawinnie","winnie")

  def tearDown(self):
    """
    tearDown method that does clean up after each test case has run
    """
    Credential.credential_list = []

  def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_credential.view_password,"winnie")
    self.assertEqual(self.new_credential.account,"facebook")
    self.assertEqual(self.new_credential.login,"deinawinnie")
    self.assertEqual(self.new_credential.password,"winnie")