#task4lesson16.py


"""
 Custom exception

Create your custom exception named 'CustomException', you can inherit from base Exception class, but extend its functionality to log every error message to a file named 'logs.txt'. Tips: Use __init__ method to extend functionality for saving messages to file

'''

class CustomException(Exception):

def __init__(self, msg):

'''

'''   
"""


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_error(msg)

    def log_error(self, msg):
        with open('logs.txt', 'a') as log_file:
            log_file.write(f"{msg}\n")


def test():
    try:
        raise CustomException("This is a custom error message.")
    except CustomException as e:
        print(e)

    try:
        raise CustomException("Another custom error occurred.")
    except CustomException as e:
        print(e)

 
def read_logs():    
    with open('logs.txt', 'r') as log_file:
        return log_file.read()
    
if __name__ == "__main__":
    test()
    print(f"\nThis is result reading log file:\n{read_logs()}")
    
    