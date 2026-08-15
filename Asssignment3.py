class CreditCard:
    def pay(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            account.history.append("Paid $" + str(amount) + " using Credit Card")
            print("Payment Successful!")
        else:
            print("Insufficient Balance")


class DebitCard:
    def pay(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            account.history.append("Paid $" + str(amount) + " using Debit Card")
            print("Payment Successful!")
        else:
            print("Insufficient Balance")


class UPI:
    def pay(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            account.history.append("Paid $" + str(amount) + " using UPI")
            print("Payment Successful!")
        else:
            print("Insufficient Balance")


class Account:
    def __init__(self, balance):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append("Deposited $" + str(amount))
        print("Deposit Successful")

    def show_balance(self):
        print("Current Balance: $", self.balance)

    def show_history(self):
        if len(self.history) == 0:
            print("No Transactions")
        else:
            print("\nTransaction History")
            for i in self.history:
                print(i)


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, account, amount):
        self.strategy.pay(account, amount)


account = Account(1000)
payment = Payment(UPI())

while True:
    print("\n----- Payment System -----")
    print("1. Select Payment Method")
    print("2. Make Payment")
    print("3. Deposit Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. UPI")
        m = int(input("Choose Method: "))

        if m == 1:
            payment.set_strategy(CreditCard())
            print("Credit Card Selected")
        elif m == 2:
            payment.set_strategy(DebitCard())
            print("Debit Card Selected")
        elif m == 3:
            payment.set_strategy(UPI())
            print("UPI Selected")
        else:
            print("Invalid Choice")

    elif choice == 2:
        amt = int(input("Enter Amount: "))
        payment.pay(account, amt)

    elif choice == 3:
        amt = int(input("Enter Deposit Amount: "))
        account.deposit(amt)

    elif choice == 4:
        account.show_balance()

    elif choice == 5:
        account.show_history()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")