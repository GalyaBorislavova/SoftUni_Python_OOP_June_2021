class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._balance = amount
        self._transactions = []

    @property
    def balance(self):
        return self._balance

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._balance += amount
        self._transactions.append(amount)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account._balance + amount_to_add <= 0:
            raise ValueError("sorry cannot go in debt!")
        account.amount += amount_to_add
        account._transactions.append(amount_to_add)
        return f"New balance: {account.amount}"

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.amount})"

    def __gt__(self, other):
        return self._balance > other._balance

    def __ge__(self, other):
        return self._balance >= other._balance

    def __eq__(self, other):
        return self._balance == other._balance

    def __getitem__(self, index):
        return self._transactions[index]

    def __add__(self, other):
        total_amount = self.amount + other.amount
        new_account = Account(f"{self.owner}&{other.owner}", total_amount)
        new_account._transactions = self._transactions + other._transactions
        return new_account

    def __reversed__(self):
        return reversed(self._transactions)


if __name__ == "__main__":
    acc = Account('bob', 10)
    acc2 = Account('john')
    print(acc)
    print(repr(acc))
    acc.add_transaction(20)
    acc.add_transaction(-20)
    acc.add_transaction(30)
    print(acc.balance)
    print(len(acc))
    for transaction in acc:
        print(transaction)
    print(acc[1])
    print(list(reversed(acc)))
    acc2.add_transaction(10)
    acc2.add_transaction(60)
    print(acc > acc2)
    print(acc >= acc2)
    print(acc < acc2)
    print(acc <= acc2)
    print(acc == acc2)
    print(acc != acc2)
    acc3 = acc + acc2
    print(acc3)
    print(acc3._transactions)
