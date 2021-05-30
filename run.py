#!/usr/bin/env python3.9
from credential import Credential
from user import User
import random

def create_credential(view_password,account,login_name,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(view_password,account,login_name,password)
    return new_credential

def create_user_account(view_password,account,login_name,password):
    """
    Function to create a new account
    """
    new_user = User(view_password,account,login_name,password)
    return new_user   

def save_credential(credential):
    """
    Function to save credentials
    """
    credential.save_credential()

def save_user_account(user):
    """
    Function to save user accounts
    """
    user.save_user()  

def delete_credential(credential):
    """
    Function to delete a credential
    """
    credential.delete_credential()

def del_user_account(user):
    """
    Function to delete a user account
    """
    user.delete_user()

def find_credential(number):
    '''
    Function that finds a credential by number and returns the credential
    '''
    return Credential.find_by_number(number)

def find_user_account(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.user_account(number)

def check_existing_credentials(number):
    '''
    Function that check if a credential exists with that number and return a Boolean
    '''
    return Credential.credential_exist(number)

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(number)

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credential()

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()                             


def main():
    print("Hello Welcome to the Password Locker. What is your name?")
    usr_name = input()

    print(f"Hello {usr_name}. what would you like to do?")
    print("\n")

    while True:
        print("*" * 30)
        print("Use these short codes : ca - create account, cc - create credentials, cp -create password, dc - display credentials, gp - generate password, rc - delete credentials, ex - exit password locker")

        short_code = input().lower()

        if short_code == 'ca':
            print("New account")
            print("*"*20)

            print ("User name ....")
            print("*"*20)
            user_name = input()

            print("Password ...")
            print("*"*20)
            pass_word = input()

            save_user_account(create_user_account(user_name,pass_word))

            print("\n")
            print(f"New Account **{user_name}** created.\n")

        elif short_code == 'cc':  
            print("Login to account")
            print("*"*20)
            print ("User name?")
            print("*"*20)
            username_input = input()
            print("Password?")
            print("*"*20)
            user_password_input= input()
            view_password = user_password_input  


            if check_existing_users(user_password_input):
                print("\nWelcome back!")
                print("New credential")
                print("*"*20)

                print("\nWhich account do the credentials belong to?")
                print("*"*40)
                account = input()

                print("\nEnter account login name")
                print("*"*40)
                login_name = input()

                print("\n")
                print("*"*40)
                login_name = input()

           