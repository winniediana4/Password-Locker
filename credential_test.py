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


  def test_save_credential(self):
    """
    test_save_credential test case to test if the credential object is saved into
    """
    self.new_credential.save_credential()
    self.assertEqual(len(Credential.credential_list),1)


  def test_save_multiple_credential(self): 
    """
    test_save_multiple_credential to check if multiple credentials can be saved
    """
    self.new_credential.save_credential()
    test_credential = Credential("winnie","test","login","winnie")
    test_credential.save_credential()
    self.assertEqual(len(Credential.credential_list),2)


  def test_delete_credential(self):
    """
    test_delete_credential to test if we can remove a credential from our credential_list
    """
    self.new_credential.save_credential()
    test_credential = Credential("0712345678","test","login","0712345678")# new credential
    test_credential.save_credential()

    self.new_credential.delete_credential()# delete a credential object
    self.assertEqual(len(Credential.credential_list),1)


  def test_display_all_credential(self):
    """
    test_display_all_credentials to return a list of all saved credentials
    """
    self.assertEqual(Credential.display_credential(),Credential.credential_list)

  if __name__ =='__main__':
      unittest.main()
