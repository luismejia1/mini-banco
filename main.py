import random


class BankException(Exception):
    """Exception raised for custom error scenarios."""
    pass


class InsufficientFunds(BankException):
    pass


class InvalidAmount(BankException):
    pass


class Bank:
    pass


def random_n_digits(n):
    return random.randint(10**(n-1), 10**n - 1)


class Account:

    def __init__(self, name) -> None:
        self.account_number = random_n_digits(10)
        self.name = name
        self._balance = 0

    def deposit(self, amount: int):

        if amount <= 0:
            raise InvalidAmount('El monto debe ser mayor que cero')
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount: int):
        """
        Retorna el restante y la cantidad retirada
        """

        if amount <= 0:
            raise InvalidAmount('El monto debe ser mayor que cero')
        if self.get_balance() < amount:
            raise InsufficientFunds('Fondos insuficientes')

        self._balance = self.get_balance() - amount
        return {'remaining': self.get_balance(), 'withdrawal_amount': amount}


my_account = Account('Luis Mejia')

print(my_account.get_balance())
my_account.deposit(100)
my_account.deposit(100)

print(my_account.get_balance())

print(my_account.withdraw(50))
