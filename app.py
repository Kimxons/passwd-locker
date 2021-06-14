#!/usr/bin/env python3.8
# vim: set fileencoding=<utf-8> :

from main import *

def create_user(first,last,pwd):
    '''
    Creates a new user account
    '''
    user_new = User(first,last,pwd)
    return user_new

def register_user(user):
    '''
    Saves the created user's account 
    '''
    User.create_user(user)
    
def user_check(first,pwd):
    '''
    Checks whether user exists before creating any new credentials
    '''
    return Credentials.user_check(first,pwd)

def create_cred(name,username,platform,pwd):
    '''
    Creates credentials to be saved
    '''
    create_instance = Credentials(name,username,platform,pwd)
    return create_instance
    
def save_cred(cred):
    '''
    Saves created user credentials
    '''
    Credentials.save_cred(cred)

def password_gen(size):
    '''
    Generates a random password_gen
    '''
    random = Credentials.password_gen(size)
    return random

def show_cred(username):
    '''
    Displays saved credentials
    '''
    return Credentials.show_credentials(username)
        
def main():
    print()
    print("PASSWORD LOCKER APP")
    while True:
        print()
        print("=*=*=*=*"*10)
        print()
        print("Usage \n 1 - Register(To register a fresh) \n 2 - Login (To login to the password locker app) \n 3 - Logout(To logout from the app)")
        print()
        user_input = input("Your Selection : ")

        if user_input == '1':
            print()
            print("User registration. Kindly enter your registration details below")
            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            pwd = input("Enter your desired password: ")
            register_user(create_user(fname, lname, pwd))
            print(f"Your account has been registered as follows:\n First Name: {fname}\n LastName: {lname}\n Password: {pwd} is your password")
            
        elif user_input == '2':
            print("Enter your first name and password to log in to your account\n")
            username = input("Enter your username here:     ")
            password = input("Enter your password here:     ")
            if user_check(username, password) == username:
                print(f"Welcome {username}. Logged on successful")
                
                while True:
                    print("=*=*=*=*"*10)
                    print()
                    print("Usage")
                    user_input = input("cc - Save new credentials\n ccp - Create new credentials with Generated Password\n dc - Display credentials\n del - Delete credentials\n ex - Exit")
                    
                    if user_input == 'cc':
                        print("Enter the account details you want saved below")
                        username = input("Enter your username:      ")
                        platform = input("Enter the platform:       ")
                        pwd = input("Enter your password:       ")
                        create_cred(fname,username,platform,pwd)
                        print(f"Your credentials for site:\n {platform}, with username: {username} and password: {pwd} has been saved!")
                    
                    elif user_input == 'ccp':
                        print("Enter the account details you want saved below")
                        username = input("Enter your username:      ")
                        platform = input("Enter the platform:       ")
                        len = input("Enter the length of your desired password (Numbers Only):      ")
                        pwd = password_gen(int(len))
                        create_cred(fname,username,platform,pwd)
                        print(f"Your credentials for account:\n {platform}, with username: {username} and password: {pwd} have been saved!")
                        
                    elif user_input == 'dc':
                        print("Your saved credentials are as shown below")
                        show_cred(username)
                         
                    elif user_input == 'del':
                        print("Enter the account name and username whose credentials you want to delete below")
                        platform = input("Enter the name of the account here eg IG:     ")
                        username = input("Enter the username here:          ")
                        show_cred(username)
                        print("Your credentials have been deleted!")
                        
                    elif user_input == 'ex':
                        print("Exiting!")
                        break
    
        elif user_input == '3':
            print("You have been logged out successfully!")
            break
            
        else:
            print("Wrong Input! Kindly select again")
    
if __name__ == '__main__':
    main()      