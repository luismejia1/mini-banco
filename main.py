import random
"""
account_number {
    name
    balance
    history : [
        {
            to:
            amount:
        }
    ]
}
"""


def random_n_digits(n):
    return random.randint(10**(n-1), 10**n - 1)


class Account:

    def __init__(self, name) -> None:
        self.account_number = random_n_digits(10)
        self.name = name
        self._balance = 0

    def deposit(self, amount: int):
        self._balance = + amount

    def get_balance(self):
        return self._balance


my_account = Account('Luis Mejia')

print(my_account.get_balance())
my_account.deposit(100)
print(my_account.get_balance())
