
def validate_positive(func):
    def wrapper(*args):
        for i in args:
            if not isinstance(i, int) or i <= 0:
                print("Error: All arguments must be positive integers.")
                return
        func(*args)
    return wrapper


@validate_positive
def multiply(a, b):
    print("Product =", a * b)


multiply(5, 4)

multiply(5, -2)

multiply(5, 3.5)