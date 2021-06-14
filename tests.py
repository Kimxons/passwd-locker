#!/usr/bin/env python3.8
# vim: set fileencoding=<utf-8> :

import unittest
from main import User, Credentials

class TestUsers(unittest.TestCase):
	"""
	Test class that defines test cases for the User behaviour
	Args:
		unittest.TestCase: Class from the unittest module to create unit tests
	"""
	
	def setUp(self):
		"""
			#Function creates a new user object
		"""
		self.new_user = User("John","Doe","john123")
		
	def test_init(self):
		"""
		#test_init test case to test if the object is the initialized properly
		"""
		
		self.assertEqual(self.new_user.first,"John")
		self.assertEqual(self.new_user.last,"Doe")
		self.assertEqual(self.new_user.password,"john123")
		
	def test_save_user(self):
		"""
		#test_save_user test case to test if the object is saved
		"""
		
		self.new_user.create_user()
		self.assertEqual(len(User.user_info),1)
		
	def tearDown(self):
		"""
		Function to Destruct functions after set up
		"""
		User.user_info = []

class TestCredentials(unittest.TestCase):
	"""
		Test class that defines test cases for the Credentials behaviour
	
		Args:
			unittest.TestCase: Class from the unittest module to create unit tests
	"""

	def test_auth_check(self):
		"""
		test_auth_check test case to test if the user provided correct information
		"""
		self.new_user = User("John","Doe","john123")
		self.new_user.create_user()
		another_user = User("Jeff","Bezos","jeff123")
		another_user.create_user()
		
		for cred in User.user_info:
			if cred.first == another_user.first and cred.password == another_user.password:
				identity = another_user.first
		return identity
		
	def test_setUp(self):
		"""
		test_setUp to create a new Credentials object to begin tests
		"""
		
		self.new_cred = Credentials("John","Doe","Twitter","john123")
	
	def test_init(self):
		"""
		test_init to check if the Credentials objects are initialized correctly
		"""
		self.new_cred = Credentials("John","Doe","Twitter","john123")
		self.assertEqual(self.new_cred.name, "John")
		self.assertEqual(self.new_cred.username, "Doe")
		self.assertEqual(self.new_cred.platform, "Twitter")
		self.assertEqual(self.new_cred.pwd, "john123")
		
	def test_save_cred(self):
		"""
		test_save_cred to check if the initialized object is saved to credentials_info
		"""
		self.new_cred = Credentials("John","Doe","Twitter","john123")
		self.new_cred.save_cred()
		self.assertEqual(len(Credentials.credentials_info),3)
		
	def tearDowm(self):
		"""
		reinitializes the credentials_info list to its empty state
		"""
		Credentials.credentials_info = []
		
	def test_show_credentials(self):
		"""
		test_show_credentials test to check if credentials saved is displayed
		"""
		self.new_cred = Credentials("John","Doe","Twitter","john123")
		self.new_cred.save_cred()
		self.another_cred = Credentials("Jeff","Bezos","Twitter","jeff123")
		self.another_cred.save_cred()
		self.assertEqual(len(Credentials.show_credentials(self.new_cred.username)),1)
		
	def test_del_cred(self):
		"""
		test_del_cred test to delete credentials from the credentials list
		"""
		Credentials.credentials_info = []
		self.new_cred = Credentials("John","Doe","Twitter","john123")
		self.new_cred.save_cred()
		Twitter = Credentials("John","Doe","Twitter","john123")
		Twitter.save_cred()
		del_item = Credentials.find_platform('Twitter')
		self.assertEqual(Credentials.del_cred(del_item),"Deleted")
    			
if __name__ == '__main__':
	unittest.main()