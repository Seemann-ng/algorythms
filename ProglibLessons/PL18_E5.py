class BankAccount:
    def __init__(self, balance: float, interest_rate: float):
        self.__balance = round(balance, 2)
        self.__interest_rate = interest_rate
        self.__transactions = []

    def get_balance(self):
        print(f"Available balance: ${self.__balance}")
        self.__transactions.append("Balance request")

    def deposit(self, amount: float):
        self.__balance = round(self.__balance + amount, 2)
        self.__transactions.append(f"Deposit: + ${amount}")

    def withdraw(self, amount: float):
        self.__balance = round(self.__balance - amount, 2)
        self.__transactions.append(f"Withdrawal: - ${amount}")

    def addInterest(self):
        self.__balance = round(self.__balance + (self.__balance * self.__interest_rate), 2)
        self.__transactions.append(f"Interest added: + ${round(self.__balance * self.__interest_rate, 2)}")

    def history(self):
        for operation in self.__transactions:
            print(operation)


account = BankAccount(100000, 0.05)

account.get_balance()
account.deposit(15300)
account.get_balance()
account.withdraw(7000.50)
account.get_balance()
account.addInterest()
account.get_balance()
account.deposit(18000)
account.get_balance()
account.addInterest()
account.get_balance()
account.history()
