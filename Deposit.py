class Deposit:
    def deposit(self, details):
        amount = int(input("Enter amount:"))
        last_amount = details[-1]

        details.append(last_amount + amount)
        print(f"Amount {amount} has been credited.")
        return  details
