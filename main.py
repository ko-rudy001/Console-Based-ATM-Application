from Transactions_History import Transaction
from Withdraw import Withdraw
from Deposit import Deposit
from Transfer import Transfer
from Quit import Quit


class ATM:

    def __init__(self, details):
        self.details = details

    def login(self):
        entered_user_id = input("Enter User ID: ")
        entered_pin = input("Enter PIN: ")

        for i in self.details:
            if entered_user_id == i and entered_pin == self.details[i][0]:
                print("Login Successfully!")
                self.menu(self.details[i][1])
            else:
                print("Login Failed. Please try again.")
                self.login()

    def menu(self, user_id):
        print("\nATM Menu:")
        print("\n1. Transactions History")
        print("\n2. Withdraw")
        print("\n3. Deposit")
        print("\n4. Transfer")
        print("\n5. Quit")

        choice = input("Select an option: ")
        if choice == "1":
            th = Transaction()
            th.History(user_id)
        elif choice == "2":
            wd = Withdraw()
            user_id = wd.withdraw(user_id)
        elif choice == "3":
            dp = Deposit()
            user_id = dp.deposit(user_id)
        elif choice == "4":
            tf = Transfer()
            user_id = tf.transfer(user_id)
        elif choice == "5":
            qt = Quit()
            qt.quit()
        else:
            print("Invalid choice. Please select a valid option.")
        self.menu(user_id)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    users = {"Rudy": ["123", [5000]]}
    obj = ATM(users)
    obj.login()
