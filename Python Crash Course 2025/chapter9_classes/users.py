# USERS = Make a class called User. Create two attributes called first_name and 
# last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user's information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both 
# methods for each user.

class User:
# giving the class name User
    
    def __init__(self, first_name, last_name, username, email, location):
        # passing through numerous attributes
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username.strip().lower() # stripping any whitespace
        self.email = email.strip().lower() # stripping any whitespace
        self.location = location.upper()
        
    def describe_user(self): # method one
        print(f"\nName: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        
    def greet_user(self): # method two
        print(f"\nHello there {self.username}")
        
james = User('james', 'bilverstone', 'james123', 'james123@icloud.com', 'ncl')
# instance one

nicole = User('nicole', 'paton', 'nicole123', 'nicole123@icloud.com', 'aberdeen')
# instance two

woody = User('woody', 'the cat', 'woody123', 'woody@cat', 'backgarden')   
# instance three     

# CALLING BOTH METHODS FOR ALL INSTANCES
james.describe_user()
james.greet_user()

nicole.describe_user()
nicole.greet_user()

woody.describe_user()
woody.greet_user()