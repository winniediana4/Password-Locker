import unittest
from user import User

class TestUser(unittest.TestCase):
  """
 Test class that defines test cases for the user class behaviours.
 Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  """


  def setUp(self):
    """
    set_up method to run before each test case
    """
    self.new_user = User("winnie", "diana","deinawinnie","winnie")


  def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.new_user.first_name,"winnie")
    self.assertEqual(self.new_user.last_name,"diana")
    self.assertEqual(self.new_user.user_name,"deinawinnie")
    self.assertEqual(self.new_user.password,"winnie")


  def test_save_user(self):
    """
    test_save_user test case to test if the user object is saved into
    """
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)


  def test_save_multiple_user(self): 
    """
    test_save_multiple_user to check if multiple users can be saved.
    """
    self.new_user.save_user()
    test_user = User("winnie", "diana","deinawinnie","winnie")
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)


  def tearDown(self):
    """
    tearDown method that does clean up after each test case has run.
    """
    User.user_list = []


  def test_save_multiple_user(self): 
    """
    test_save_multiple_user to check if multiple users can be saved.
    """
    self.new_user.save_user()
    test_user = User("winnie", "diana","deinawinnie","winnie")
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)


  def test_delete_user(self):
    """
    test_delete_user to test if we can remove a user from our user_list
    """
    self.new_user.save_user()
    test_user = User("winnie", "diana","deinawinnie","winnie")# new user
    test_user.save_user()

    self.new_user.delete_user()# delete a user object
    self.assertEqual(len(User.user_list),1)


  def test_display_user_by_user_name(self):
    """
    test method to check if a user can be found by user_name and display info
    """
    self.new_user.save_user()
    test_user = User("winnie", "diana","deinawinnie","winnie")# new user
    test_user.save_user()

    found_user = User.find_by_user_name("deinawinnie")
    self.assertEqual(found_user.user_name,test_user.user_name)


  def test_user_exists(self):
    """
    test to check if we can return a Boolean if user cannot be found
    """
    self.new_user.save_user()
    test_user = User("winnie", "diana","deinawinnie","winnie")# new user
    test_user.save_user()

    user_exists = User.user_exist("deinawinnie")
    self.assertTrue(user_exists)

  if __name__ =='__main__':
      unittest.main()
