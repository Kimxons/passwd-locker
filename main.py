#!/usr/bin/env python3.8
# vim: set fileencoding=<utf-8> :

import string
import random

class User:

    '''
        This Class contains user methods and attrs
    '''
    
    user_info = []
    
    def __init__(self,firstName,lastName,password):
        """
            Information needed to create a password saving object
        """
        self.first = firstName
        self.last = lastName
        self.password = password
    
    def create_user(self):
        """
            Create an instance of a new user
        """
        
        self.user_info.append(self)

class Credentials(User):
    """
        Class that holds credential information and associated methods eg. add, remove and view creadentials
    """
    
    credentials_info = []
    user_cred_info = []
    
    @classmethod
    def user_check(cls,firstName,password):
        """
            Checks for matching credentials in user_info
        """
        
        for cred in cls.user_info:
            if cred.firstName == firstName and cred.password == password:
                identity = cred.firstName
        return identity
    
    def __init__(self,name,username,platform,pwd):
        """
            Initialize new Credentials object
        """
        
        self.name = name
        self.username = username
        self.platform = platform
        self.pwd = pwd
        
    def save_cred(self):
        """
            Saves credentials in credentials_info list
        """
        Credentials.credentials_info.append(self)
        
    def password_gen(size):
        """
            Generate a random string of letters and digits 
        """
        lettersAndNumbers = string.ascii_letters + string.digits
        password = ''.join(random.choice(lettersAndNumbers) for i in range(int(size)))
        return password
    
    @classmethod
    def show_credentials(cls,username):
        """
            Shows the saved credentials
        """
    
        for cred in cls.credentials_info:
            if cred.username == username:
                cls.user_cred_info.append(cred)
            return cls.user_cred_info   
    
    @classmethod
    def find_platform(cls,platform):
        """
            Finds the platform's credentials
        """
        
        for cred in cls.credentials_info:
            if cred.platform == platform:
                return cred
                
    @classmethod
    def del_cred(cls,cred):
        """
            Deletes credentials saved, and used together with the find platform method
        """
        
        for credential in cls.credentials_info:
            if credential == cred:
                del credential
                return "Deleted"