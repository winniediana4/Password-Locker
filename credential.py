class Credential:
   """
   Class that generates new instances of a user's credentials
   """

   credential_list=[]

   def __init__(self,view_password,account,login,password):
       self.view_password = view_password
       self.account = account
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
   def find_by_account_name(cls,account):
      """
      Method that takes in a number and returns a credential that matches the account_name
      Args:
          account: Account name to search for
      Returns:
          Credential of account that matches the account name  
      """

      for credential in cls.credential_list:
        if credential.account == account:
            return credential

   @classmethod                    
   def credential_exist(cls,account):
      """
      Method that checks if a credential exists from the credential_list.
      Args:
          account: Account name to search if it exists
      Returns :
          Boolean: True or false dependent on if the credential exists
      """

      for credential in cls.credential_list:
        if credential.account == account:
            return True

