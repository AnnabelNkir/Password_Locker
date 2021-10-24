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