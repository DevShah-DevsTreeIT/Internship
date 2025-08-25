import unittest
from task2 import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_initial_balance_is_zero(self):
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0)

    def test_deposit_adds_to_balance(self):
        account = BankAccount()
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw_decreases_balance(self):
        account = BankAccount()
        account.deposit(100)
        account.withdraw(40)
        self.assertEqual(account.get_balance(), 60)

    def test_cannot_withdraw_more_than_balance(self):
        account = BankAccount()
        account.deposit(50)
        with self.assertRaises(ValueError):
            account.withdraw(100)

if __name__ == '__main__':
    unittest.main()
