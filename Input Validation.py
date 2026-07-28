from functools import wraps


def validate_positive_integers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if not isinstance(arg, int) or isinstance(arg, bool) or arg <= 0:
                print(f"Error: Invalid argument '{arg}'. All arguments must be positive integers.")
                return None
        return func(*args, **kwargs)
    return wrapper


@validate_positive_integers
def add(a, b):
    print(f"Sum: {a + b}")


@validate_positive_integers
def multiply(a, b, c):
    print(f"Product: {a * b * c}")


# --- Demo ---
add(5, 3)          # Valid -> Sum: 8
add(-2, 4)         # Invalid -> error message
add(3.5, 2)        # Invalid (float) -> error message
multiply(2, 3, 4)  # Valid -> Product: 24
multiply(2, 0, 4)  # Invalid (zero not positive) -> error message
