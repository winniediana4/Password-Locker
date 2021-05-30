class User:
  """
  Class that generates new User instances
  """
  user_list = []
  def __init__(self,user_name,password):

    self.user_name = user_name
    self.password = password

  def save_user(self):
    """
    save_user method saves user objects into user_list
    """
    User.user_list.append(self)

  @classmethod
  def find_by_user_name(cls,user_name):
    """
    Method that takes in a user_name and returns a user that matches that user_name
    """