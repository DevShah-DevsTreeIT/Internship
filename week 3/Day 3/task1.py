# Bank Account Class:- Create a BankAccount class with deposit, withdraw, and balance methods



class Bank_account:

    def __init__(self,name,abalance,damount,wamount):
        # self.name = name
        self.abalance = abalance
        self.name = name 
        name = input("Enter your name: ").capitalize()
        self.damount = damount
        self.wamount = wamount
    

    def deposit(self):
        # print(f"Please insert amount to deposit") 
        self.damount = int(input("Enter the amount to deposit"))
        self.abalance += self.damount 
        print(f"Avaialble balance after depost is: {self.abalance}")

    def withdraw(self):
        print(f"Enter the amount you want to withdraw")
        self.wamount = int(input("Enter the amount to withdraw"))
        self.abalance -= self.wamount 
        print(f"Avaialble balance after withdrawl is: {self.abalance}")


    def balance(self):
        print(f"Hello {self.name} Your current balance is: {self.abalance}")



p1 = Bank_account("",15000,"","")
# p1.name = input("Enter your name:")

print(f"Hello {p1.name} welcome to DevsTree bank.")
while True:
    print("Available options:")
    print("1.Balance Inquiry")
    print("2.Money Withdrawal")
    print("3.Cash Deposit")
    print("4.exit")
    choice = int(input("Enter your choioce:"))
    if choice == 1:
        p1.balance()
        break
    elif choice == 2:
        p1.withdraw()
        break
    elif choice == 3:
        p1.deposit()
        break
    elif choice == 4:
        print(f"Thanks {p1.name} for choosing our bank")
        break
    else:
        print("Please chooose a valid option")

