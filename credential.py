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
