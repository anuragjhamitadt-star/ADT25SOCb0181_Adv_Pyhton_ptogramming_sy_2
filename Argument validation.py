from functools import wraps


def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"'{func.__name__}' has been called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


@count_calls
def greet(name):
    print(f"Hello, {name}!")


@count_calls
def add(a, b):
    print(f"Sum: {a + b}")


# --- Demo ---
greet("Alice")
greet("Bob")
add(2, 3)
greet("Charlie")
