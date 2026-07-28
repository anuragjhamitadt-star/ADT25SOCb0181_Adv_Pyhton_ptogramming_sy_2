from functools import wraps

logged_in_user = None  # None means no one is logged in


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if logged_in_user is None:
            print("Please log in first.")
            return
        return func(*args, **kwargs)
    return wrapper


@login_required
def dashboard():
    print(f"Welcome, {logged_in_user}!")


def login(username):
    global logged_in_user
    logged_in_user = username
    print(f"{username} logged in.")


def logout():
    global logged_in_user
    logged_in_user = None
    print("Logged out.")


# --- Demo ---
dashboard()        # Please log in first.
login("Alice")
dashboard()        # Welcome, Alice!
logout()
dashboard()        # Please log in first.
