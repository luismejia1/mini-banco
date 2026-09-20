import random


class InvalidInput(Exception):
    pass


class InvalidOption(InvalidInput):
    pass


class BankException(Exception):
    """Exception raised for custom error scenarios."""
    pass


class ExistsAccount(BankException):
    pass


class InsufficientFunds(BankException):
    pass


class InvalidAmount(BankException):
    pass


def random_n_digits_str(n):
    return str(random.randint(10**(n-1), 10**n - 1))


"""
my_dict: dict[str, MyItem] = {
    "asas": {"name": "hello", "value": 42, "active": True},
    "other": {"name": "world", "value": 7, "active": False},
}
"""


class Bank:
    accounts = {}

    def __init__(self) -> None:
        pass

    def account_exists(self, account_number) -> bool:
        return account_number in self.accounts

    def create_account(self, name: str) -> str:
        account_number = random_n_digits_str(10)
        while self.account_exists(account_number) == True:
            account_number = random_n_digits_str(10)

        account = Account(name=name, account_number=account_number)
        self.accounts.update({account_number: account})

        return account_number

    def get_account(self, account_number: str) -> Account | None:
        return self.accounts.get(account_number)


class Account:

    def __init__(self, name: str, account_number: str) -> None:
        self.account_number = account_number
        self.name = name
        self._balance = 0

    def get_account_detail(self):
        return {self.name, self.account_number}

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


def read_input_int(input: str):
    try:
        option = int(input)
    except ValueError:
        raise InvalidInput(f"Invalid input: {input!r}") from None
    return option


def separator():
    print('============================================\n')


def show_menu():
    separator()
    print('Hola, bienvenido a Banco123, que deseas hacer?')
    print('1. Crear cuenta')
    print('2. Depositar en una cuenta')
    print('3. Retirar de una cuenta')
    print('4. Consultar saldo')
    print('5. Consultar hitorial de movimientos')
    print('6. Transferir de una cuenta a otra')
    print('7. Salir')
    separator()


def main():
    bank = Bank()
    while True:
        show_menu()
        try:
            option = read_input_int(input('Seleccione una opcion: \n'))
        except InvalidInput:
            print('Caracter invalido, favor prueba nuevamente')
            continue

        match option:

            case 1:
                print('Hola, gracias por crear una cuenta con nosotros')
                name = input('Para continuar, por favor ingrese su nombre: \n')
                if len(name) < 3:
                    print('Debes ingresar un nombre valido')

                else:
                    account_number = bank.create_account(name=name)
                    print(
                        f'Su cuenta con numero {account_number} ha sido creada correctamente')

            case 2:
                account_number = input(
                    'Ingresa el numero de cuenta a la que quieres depositar: \n')

                account = bank.get_account(account_number)
                if account is not None:

                    try:
                        amount = read_input_int(input(
                            'Ingresa la cantidad de dinero que quieres depositar: \n'))
                        account.deposit(amount=amount)
                    except InvalidInput:
                        print('Entrada invalida, prueba nuevamente')
                        continue
                    except BankException:
                        print('La cantidad no es valida')
                else:
                    print('No existe una cuenta con este numero')

            case 3:
                print('3. Retirar de una cuenta')

            case 4:
                account_number = input(
                    'Ingresa el numero de cuenta a consultar: \n')

                account = bank.get_account(account_number)
                if account is not None:
                    print(account.get_balance())
                else:
                    print('No existe una cuenta con este numero')

            case 5:
                print('5. Consultar hitorial de movimientos')

            case 6:
                print('6. Transferir de una cuenta a otra')

            case 7:
                print('Adios 👋')
                break
            case _:
                print('Favor selecciona una opcion valida')


if __name__ == "__main__":
    main()
