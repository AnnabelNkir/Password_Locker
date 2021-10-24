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
