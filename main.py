class User:
    '''
    This class contains user methods and attrs
    '''
    user_info = []
    
    def __init__(self,firstName,lastName,password):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password

    def create_user(self):
        self.user_info.append(self)

class Credentials(User):
    """
    Class that holds user credentials and associated methods 
    """
    credentials_info = []
    user_credentials_info = []
    def check_user(tx,firstName,password):
        """
        check for matching user credential info
        """
        for cred in 