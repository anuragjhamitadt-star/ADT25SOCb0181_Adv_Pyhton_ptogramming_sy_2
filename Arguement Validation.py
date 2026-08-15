
def count_calls(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Function called", count, "time(s)")
        func()

    return wrapper

@count_calls
def greet():
    print("Hello, User!")

# Function calls
greet()
greet()
greet()