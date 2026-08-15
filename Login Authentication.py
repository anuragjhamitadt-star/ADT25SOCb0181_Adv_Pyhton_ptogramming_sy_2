
logged_in = False

def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access Denied: Please log in.")
    return wrapper

@login_required
def dashboard():
    print("Welcome to your Dashboard!")


dashboard()

logged_in = True
print()

dashboard()