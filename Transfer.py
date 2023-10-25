class Transfer:
    def transfer(self, details):
        amount = int(input("Enter amount:"))
        last_amount = details[-1]

        if amount <= last_amount:
            details.append(last_amount - amount)
            print(f"Amount {amount} has been transferred.")
        else:
            print("Insufficient balance.")
        return  details
