
import datetime


class BankAccount:

    def __init__(self, name, acc_no, pin, balance):
        self.name = name
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.history = []


    def login(self):

        entered_pin = int(input("Enter PIN: "))

        if entered_pin == self.pin:
            print("\nLogin Successful")
            return True

        else:
            print("Wrong PIN")
            return False


    def deposit(self):

        amount = int(input("Enter deposit amount: ₹"))

        if amount > 0:
            self.balance += amount

            self.history.append(
                f"Deposited ₹{amount} - {datetime.datetime.now()}"
            )

            print("Amount Deposited Successfully")

        else:
            print("Invalid Amount")


    def withdraw(self):

        amount = int(input("Enter withdrawal amount: ₹"))

        if amount > self.balance:
            print("Insufficient Balance")

        elif amount <= 0:
            print("Invalid Amount")

        else:
            self.balance -= amount

            self.history.append(
                f"Withdraw ₹{amount} - {datetime.datetime.now()}"
            )

            print("Collect your cash")
            print("Withdrawal Successful")


    def balance_check(self):

        print("\nAccount Holder:", self.name)
        print("Account Number:", self.acc_no)
        print("Current Balance: ₹", self.balance)


    def show_history(self):

        print("\nTransaction History")

        if len(self.history) == 0:
            print("No Transactions")

        else:
            for item in self.history:
                print(item)



account = BankAccount(
    "Aayush",
    101,
    1234,
    10000
)


print("======================")
print("   BANKING SYSTEM")
print("======================")


if account.login():

    while True:

        print("\n------ MENU ------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Check")
        print("4. Transaction History")
        print("5. Exit")


        choice = int(input("Enter choice: "))


        if choice == 1:
            account.deposit()


        elif choice == 2:
            account.withdraw()


        elif choice == 3:
            account.balance_check()


        elif choice == 4:
            account.show_history()


        elif choice == 5:
            print("\nThank you for banking with us")
            print("Visit Again")
            break


        else:
            print("Invalid Choice")