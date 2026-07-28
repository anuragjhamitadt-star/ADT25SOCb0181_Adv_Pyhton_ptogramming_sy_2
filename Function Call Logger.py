from functools import wraps
from datetime import datetime


def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG] '{func.__name__}' called at {now}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def greet(name):
    print(f"Hello, {name}!")


@log_call
def add(a, b):
    print(f"Sum: {a + b}")


# --- Demo ---
greet("Alice")
add(5, 3)
