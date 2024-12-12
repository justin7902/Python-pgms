class Bank:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance


    def Deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.balance += amount
            print(f"Deposited: {amount}")
            print("Updated Balance", self.balance)



    def Withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive")

        elif self.balance < amount:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            print("Updated Balance", self.balance)

    def Display(self):
        print("\nAccount Details")
        print("\nAccount Number:", self.acc_no)
        print("\nName:", self.name)
        print("\nAccount Type", self.acc_type)
        print("\nBalance:", self.balance)


acc_no = int(input("Enter Account Number"))
name = input("Enter Name")
acc_type = input("Enter Account Type {Saving/Current}")
balance = int(input("Enter Initial Balance"))

account = Bank(acc_no, name, acc_type,balance)

account.Display()

deposit_amount = int(input("Enter the amount to be deposited"))
account.Deposit(deposit_amount)


withdraw_amount = int(input("Enter the amount to be withdrew"))
account.Withdraw(withdraw_amount)