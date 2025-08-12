################### Atm simulator #####################
# Simulate a basic ATM system where a user can:

# View balance

# Deposit money

# Withdraw money

# Exit the session





class ATM:
    def __init__(self, pin=8647, balance=0):
        self.pin = pin
        self.balance = balance
        # self.deposit = deposit
        # self.withdarw = withdraw

    def check_balance(self):
        print(f"Your Avaialble Balance is: {self.balance}")

    def deposit(self,amount):
        self.balance += amount
        print(f"Amount deposited successfully. Your updated balance is {self.balance}")
    
    def withdraw(self,amount):
        if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully Withdrew the amount {amount} and your remaining balance is {self.balance} ")
        else:
                print(" Insufficient Balance :( ")


class User(ATM):
    def __init__(self):
        super().__init__()    


    def login(self):
        while True:
            epin = int(input("Enter your pin: "))
            if epin == self.pin:
                while True:
                    print("Welcome to ATM: ")
                    print("1.Check Balance")
                    print("2.Deposit")
                    print("3.Withdraw")
                    print("4.Exit")
    
                    option = int(input("Select a option:"))
                    if option == 1:
                        self.check_balance()
                    elif option == 2:
                        amount = int(input("Enter the amount to Deposit: "))
                        if amount > 0:
                            self.deposit(amount)
                    elif option == 3:
                        # print("Enter the amount you would like to Withdraw: ")
                        amount = int(input("Enter the amount to withdraw: "))
                        self.withdraw(amount)
                    elif option == 4:
                        print("Thanks,For visting our ATM 😁")     
                        break
                    else:
                        print("Please enter a valid option")
                break
            else:
                print("Wrong pin entered")
            # break

obj1 = User()
obj1.login()