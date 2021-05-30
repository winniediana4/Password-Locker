class Credential:
   """
   Class that generates new instances of a user's credentials
   """

   credential_list=[]

   def __init__(self,view_password,user,login,password):
       self.view_password = view_password
       self.user = user
       self.login = login
       self.password = password

   def save_credential(self):
     """
     save_credential method saves objects into the credential_list
     """  
     Credential.credential_list.append(self)


   @classmethod
   def display_credential(cls):
      """
      display_credential method displays the credential_list
      """

   def delete_credential(self):
      """
      delete_credential method deletes saved objects from the credential_list
      """
      Credential.credential_list.remove(self)


   @classmethod
   def find_user_name(cls,user):
      """
      find_user_name method returns a credential that matches the user_name
      """
      return cls.credential_list