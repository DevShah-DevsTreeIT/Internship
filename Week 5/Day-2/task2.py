#Test-Driven Development (TDD):- Test-Driven Development is a software development practice 

# where you:
# Write tests first before writing any actual code.
# Run the tests and watch them fail (since there's no implementation yet).
# Write the minimum code needed to make the tests pass.
# Refactor the code (clean it up) while ensuring tests still pass.
# Repeat!

# In short: Red → Green → Refactor

# 🧠 Why TDD?
# Ensures code does what it's supposed to do
# Helps you think through requirements clearly
# Makes your code easier to maintain and refactor




class BankAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
