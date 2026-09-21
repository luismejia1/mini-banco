import random
from enum import Enum


class Operations(Enum):
    Retiro = 'Retiro'
    Deposito = 'Deposito'
    Transferencia = 'Transferencia'


class InvalidInput(Exception):
    pass


class InvalidOption(InvalidInput):
    pass


class BankException(Exception):
    """Exception raised for custom error scenarios."""
    pass


class AccountNotFound(BankException):
    pass


class InsufficientFunds(BankException):
    pass


class InvalidAmount(BankException):
    pass


def random_n_digits_str(n):
    return str(random.randint(10**(n-1), 10**n - 1))


class Bank:
    accounts = {}

    def __init__(self) -> None:
        pass

    def account_exists(self, account_number) -> bool:
        return account_number in self.accounts

    def create_account(self, name: str) -> str:
        account_number = random_n_digits_str(10)
        while self.account_exists(account_number):
            account_number = random_n_digits_str(10)

        account = Account(name=name, account_number=account_number)
        self.accounts.update({account_number: account})

        return account_number

    def transfer(self, from_account: str, to_account: str, amount: int):
        origin_account = self.get_account(from_account)
        target_account = self.get_account(to_account)
        if origin_account is None:
            raise AccountNotFound("Cuenta de origen no encontrada")
        if target_account is None:
            raise AccountNotFound("Cuenta de destino no encontrada")

        # Retiro de la cuenta origen, sino tiene fondos, lanzo exception, se que puede hacerse mejor guardando lo que recibe, pero
        # si no lanza excepcion es que tood salio ok asi que lo dejo lo as simple, usando el prnicipio KISS
        origin_account.withdraw(amount, is_transfer=True)
        target_account.deposit(amount)

    def get_account(self, account_number: str) -> Account | None:
        return self.accounts.get(account_number)


class Account:

    def __init__(self, name: str, account_number: str) -> None:
        self.account_number = account_number
        self.name = name
        self._balance = 0
        self.history = []

    def deposit(self, amount: int):

        if amount <= 0:
            raise InvalidAmount('El monto debe ser mayor que cero')
        self._balance += amount
        self.__add_to_history(amount=amount, total=self._balance,
                              operation=Operations.Deposito.value)

    def get_balance(self):
        return self._balance

    def withdraw(self, amount: int, is_transfer: bool = False):
        """
        Retorna el restante y la cantidad retirada
        """

        if amount <= 0:
            raise InvalidAmount('El monto debe ser mayor que cero')
        if self.get_balance() < amount:
            raise InsufficientFunds('Fondos insuficientes')

        self._balance = self.get_balance() - amount
        operation = Operations.Transferencia.value if is_transfer else Operations.Retiro.value
        self.__add_to_history(amount=amount, total=self._balance,
                              operation=operation)
        return {'remaining': self.get_balance(), 'withdrawal_amount': amount}

    def __add_to_history(self, amount: int, total: int, operation: str):
        self.history.append({
            'operation': operation,
            'amount': amount,
            'total': total
        })


def read_input_int(user_input: str):
    try:
        option = int(user_input)
    except ValueError:
        raise InvalidInput(f"Invalid input: {user_input!r}") from None
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
                        print(
                            f'Se ha depositado {amount} a la cuenta {account_number}')
                    except InvalidInput:
                        print('Entrada input invalida, prueba nuevamente')
                        continue
                    except BankException:
                        print('La cantidad no es valida')
                else:
                    print('No existe una cuenta con este numero')

            case 3:
                account_number = input(
                    'Ingresa el numero de cuenta de la que quieres retirar: \n')

                account = bank.get_account(account_number)
                if account is not None:
                    try:
                        amount = read_input_int(
                            input('Ingresa la cantidad de dinero que quieres retirar: \n'))
                        result = account.withdraw(amount)
                        print(
                            f'Se ha retirado {amount} de la cuenta {account_number}, el saldo restante es {result.get('remaining')}')

                    except InvalidInput:
                        print('Caracter invalido, favor prueba nuevamente')
                        continue
                    except BankException as e:
                        print(e)
                else:
                    print('No existe una cuenta con este numero')

            case 4:
                account_number = input(
                    'Ingresa el numero de cuenta a consultar: \n')

                account = bank.get_account(account_number)
                if account is not None:
                    print(account.get_balance())
                else:
                    print('No existe una cuenta con este numero')

            case 5:
                account_number = input(
                    'Ingresa el numero de cuenta de la cual deseas ver el historial: \n ')
                account = bank.get_account(account_number)

                if account is not None:
                    for index, item in enumerate(account.history):
                        print(
                            f'{index + 1} - Se ha hecho un {item.get('operation')} de {item.get('amount')} y la cuenta tiene un total de {item.get('total')}')
                else:
                    print('No existe una cuenta con este numero')

            case 6:
                origin_account_number = input(
                    'Ingresa el numero de cuenta de origen para la transferencia: \n')

                target_account_number = input(
                    'Ingresa el numero de cuenta de destino para la transferencia: \n')

                if origin_account_number == target_account_number:
                    print('No se puede hacer una transferencia a la misma cuenta')
                else:
                    try:
                        amount = read_input_int(
                            input('Ingresa la cantidad de dinero que quieres transferir: \n'))

                        bank.transfer(origin_account_number,
                                      target_account_number, amount)

                        print(
                            'Transferencia realizada correctamente')
                    except InvalidInput:
                        print('Caracter invalido, favor prueba nuevamente')
                        continue
                    except BankException as e:
                        print(e)

            case 7:
                print('Adios 👋')
                break
            case _:
                print('Favor selecciona una opcion valida')


if __name__ == "__main__":
    main()
