#task1lesson18.py


"""
Create a class method named `validate`, which should be called from the `__init__` method to 
validate parameter email, passed to the constructor. The logic inside the `validate` method 
could be to check if the passed email parameter is a valid email string.
"""


import re

class User:
    def __init__(self, email):
        self.validate(email)
        self.email = email

    @classmethod
    def validate(cls, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email address: {email}")

    def __repr__(self):
        return f"User(email={self.email})"


if __name__ == "__main__":
    try:
        user = User("valid.email@example.com")
        print(user)  
        
        invalid_user = User("invalid-email")
    except ValueError as e:
        print(e)  