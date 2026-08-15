from datetime import datetime

def log_function(func):
    def wrapper():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        func()
    return wrapper


@log_function
def greet():
    print("Hello! Welcome to Python.")


greet()