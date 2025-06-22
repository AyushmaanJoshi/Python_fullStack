# banking.py
class BankAccount:
    total_accounts = 0

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float):
        if amount < 0 or amount > self.__balance:
            raise ValueError("Invalid withdrawal amount")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance: float):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = new_balance

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance:.2f})"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance:.2f})"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        new_owner = f"{self.owner} & {other.owner}"
        new_balance = self.__balance + other.__balance
        return BankAccount(new_owner, new_balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self.balance + self._overdraft_limit:
            raise ValueError("Invalid withdrawal amount or overdraft limit exceeded")
        self._BankAccount__balance -= amount

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value: float):
        if value < 0:
            raise ValueError("Overdraft limit must be non-negative")
        self._overdraft_limit = value


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []

    def add_account(self, account: BankAccount):
        self.accounts.append(account)

    def total_balance(self):
        return sum(account.balance for account in self.accounts)

    def transfer(self, from_acc: BankAccount, to_acc: BankAccount, amount: float):
        from_acc.withdraw(amount)
        to_acc.deposit(amount)


def print_account_summary(obj):
    try:
        print(f"Owner: {obj.owner}, Balance: {obj.balance}")
    except AttributeError:
        print("Object does not conform to required interface")


# demo.py

if __name__ == "__main__":
    a1 = SavingsAccount("Ayushmaan", 1000, 0.05)
    a2 = CheckingAccount("Madhav", 500, 200)

    a1.apply_interest()
    a2.withdraw(600)

    a3 = a1 + a2

    print(a1)
    print(a2)
    print(repr(a3))

    customer = Customer("Raghav")
    customer.add_account(a1)
    customer.add_account(a2)
    print(f"Total balance for {customer.name}: {customer.total_balance()}")

    customer.transfer(a1, a2, 100)

    print_account_summary(a1)
    print_account_summary(a2)
    print_account_summary(a3)

    accounts = [a1, a2]
    for acc in accounts:
        print(acc)
        acc.deposit(50)
        try:
            acc.apply_interest()
        except AttributeError:
            pass
