#!/usr/bin/env python3
import random
import pyperclip
import time
from termcolor import colored, cprint
from getpass import getpass
from credentials import Credentials
from user import User

def create_user(login_name, pin):
    """
    Function to create a new user
    """
    new_user = User(login_name,pin)
    return new_user

def save_user(user):
    """
    Function to save user details
    """
    user.save_user()

def authenticate_user(username,password):
    return User.user_auth(username,password)

def create_credentials(platform,username,email,password):
    """
    Function to create a new credentials
    """
    new_credentials = Credentials(platform,username,email,password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials()


def delete_credential(credentials):
    """
    Function to delete credentials
    """
    credentials.delete_credentials()


def find_credentials(platform):
    """
    Function that finds a credential by platform name and returns the credentials
    """
    return Credentials.find_by_platform(platform)


def check_existing_credentials(platform):
    """
    Function that check if a credential exists with that number and return a Boolean
    """
    return Credentials.credentials_exists(platform)


def display_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credentials.display_credentials()

def copy_password(platform):
    """
    Function which copies the password of the platform
    taken as an argument
    """
    return Credentials.copy_password(platform)

def generate_password(length):
    """
    Function which generates a random password
    Args:
        the desired password length
    """
    return Credentials.generate_password(length)

def main():
    cprint("""
             
    HELLO THERE, WELCOME TO THE PASSWORD LOCKER                                         
                
        ""","blue")
    while True:
        cprint("""
        Use the following short codes to manage your account 
            'lg' - Login 
            'xx' - Close app
            ""","blue")
        print("What would you like to do?")
        code = input().lower()
        if code == "lg":
            print("Do you have an account? Y or N")
            decision = input().lower()

            if decision.startswith("n"):
                login_name = input("Enter your username: ")
                login_pin = getpass("Enter your pin: ")
                print("Loading ...")
                time.sleep(1.5)
                print("\n")
                cprint("Congratulations!!!, Your account has been created","green",attrs=['bold'])
                print("Sign into your new account")
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                save_user(create_user(login_name,login_pin))
                if authenticate_user(sign_in_name,sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    cprint("SUCCESSFULLY SIGNED IN","green",attrs=['bold'])  
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    
                    print("\n")
            else:
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                if authenticate_user(sign_in_name,sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    cprint("SUCCESSFULLY SIGNED IN","green",attrs=['bold'])  
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                   
                    print("\n")
            while True:
                if authenticate_user(sign_in_name,sign_in_pin):
                    cprint(
                        """

          WELCOME TO YOUR PASSWORD LOCKER:
    Use the following commands to navigate the application:
        'cc' - enables you to create an a credential
        'dc' - displays the credentials you have saved
        'cp' - copies the password of a given credential
        'fc' - helps you find a credential by its platform name
        'dl' - deletes a credential
        'ex' - logs you out
        'help' - helps a user around the app
                        ""","blue")
        print(f"At your service, what task would you like to perform?")
        key_word = input().lower()

        if key_word == 'cc':
                        print("Save a new credentials")
                        platform = input("Input the platform: ")
                        print("\n")
                        username = input("Input your username: ")
                        print("\n")
                        email = input("Input your email: ")
                        print("\n")
                        option = input("Would you wish to have Passwordlocker generate a password for you? Y or N ").lower()
                        if option.startswith("y"):
                            print()
                            desired_len = int(input("How long would you like your password to be? Provide number only. "))
                            password = generate_password(desired_len)
                        else:
                            print("\n")
                            password = getpass("Enter your password: ")
        
        save_credentials(create_credentials(platform,username,email,password))
        print('\n')
        cprint(f"NEW CREDENTIALS FOR {platform} CREATED!","green",attrs=['bold'])
        print("_"*50)
        print('\n')
        
    elif key_word == 'dc':

    if display_credentials():
                            print("HERE ARE YOUR CREDENTIALS")
                            print('\n')

                            for cred in display_credentials():
                                cprint(
                                 f"""
                                  --------------------------------------------------
            Platform --- {cred.platform}               
            Username --- {cred.username}               
            Email    --- {cred.email}                  
            Password --- {cred.password}               
    --------------------------------------------------
                                ""","magenta"
                                )
                                print('\n')
    else:
                            print('\n')
                            cprint("You dont seem to have any credentials saved yet","yellow")
                            print("_"*50)
                            print('\n')                            