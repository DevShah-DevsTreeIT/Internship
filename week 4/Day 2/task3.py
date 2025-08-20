# banking_system.py

# --- Custom Exceptions ---
class BankingError(Exception):
    """Base class for banking-related exceptions."""
    pass

class InsufficientFundsError(BankingError):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: Tried to withdraw {amount}, but balance is {balance}.")

class InvalidAccountError(BankingError):
    def __init__(self, account_id):
        super().__init__(f"Invalid account ID: {account_id}.")

class NegativeDepositError(BankingError):
    def __init__(self, amount):
        super().__init__(f"Cannot deposit a negative amount: {amount}.")

class TransactionLimitExceededError(BankingError):
    def __init__(self, limit):
        super().__init__(f"Transaction limit exceeded. Daily limit is {limit}.")

# --- Banking Logic ---
class BankAccount:
    def __init__(self, account_id, balance=0, daily_limit=10000):
        if not isinstance(account_id, str) or not account_id.strip():
            raise InvalidAccountError(account_id)
        self.account_id = account_id
        self.balance = balance
        self.daily_limit = daily_limit

    def deposit(self, amount):
        if amount < 0:
            raise NegativeDepositError(amount)
        self.balance += amount
        print(f" Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        if amount > self.daily_limit:
            raise TransactionLimitExceededError(self.daily_limit)
        self.balance -= amount
        print(f" Withdrew {amount}. New balance: {self.balance}")

# --- Example Usage ---
if __name__ == "__main__":
    try:
        acc = BankAccount("123XYZ", balance=5000)
        acc.deposit(2000)
        acc.withdraw(8000)  # Will raise InsufficientFundsError
    except BankingError as e:
        print(" Banking Error:", e)


