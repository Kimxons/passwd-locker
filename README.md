#An application for managing passwords and even generating new passwords for us.

## General information
This Python application will help you to manage your passwords and even generate new passwords. On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts. It becomes really hard to remember all those passwords and even create new ones. As a user, you will be able to create a password locker account with your details, a login username and password, store already existing account credentials in the application, store already existing account username and password in the application, create new account credentials, create a credentials account and the application generates a password for you to use when you sign up for an account, have the option of putting in a password that you want to use for the new credential account, view various account credentials and their passwords in the application and delete a credentials account that you no longer need in the application.

## User Stories
These are the behaviours/features that the application implements for use by a user.
As a user, you will be able to:
- To create an account with your details - log in and password
- Store your existing login credentials
- Generate a password for a new credential/account
- Copy your credentials to the clipboard


## Cloning
In your terminal/CLI:
-   $ git clone https://github.com/Kimxons/passwd-locker.git/
-   $ cd passwd-locker

## Running the Application

```
  $ chmod +x ./run.py //To make the file executable in your machine
  then 
  $ ./app.py

  You can also do python3 <filename>
  i.e python3 app.py 
  ```
  
### Technologies Used

- [Python3.6](https://www.python.org)
- [Pyperclip module](https://pypi.org/project/pyperclip/)


### Tests
Test Driven Approach has been used in this application.
```
    python3 tests.py
```

### Test & Behaviour Driven Development(TDD && BDD)

| Behaviour                                   | Input                              | Output                                                                                                |
|---------------------------------------------|------------------------------------|-------------------------------------------------------------------------------------------------------|
| Display codes for navigation                | In terminal: $./app.py | Welcome, choose an option: ca-Create Account, 2-Log In, ex-Exit                                      |
| Display prompt for creating an account      | Enter: hi                          | Enter your first name, last name and password                                                         |
| Display prompt for login in                 | Enter: 2                          | Enter your account name and password                                                                  |
| Display codes for navigation                | Successful login                   | Choose an option: cc - Create Credential, dc - Display Credentials, del - Delete Credential, ex - exit |
| Display prompt for creating a credential    | Enter: cc                          | Enter the site name, your username and password                                                       |
| Display a list of credentials               | Enter: dc                          | Prints a list of saved credentials                                                                    |
| Display prompt for which credential to copy | Enter: cp                        | Enter the site name of the credential you wish to copy.                                               |
| Exit application                            | Enter: ex                          | Exit the current navigation stage                                                                     |


##Licence information 
Link: https://github.com/Kimxons/passwd-locker/blob/main/LICENSE