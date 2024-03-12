import json


class BankAccount:

    def __init__(self, owner, balance, currency: str):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def deposit(self, value):
        # if password is valid:
        if True:
            self.balance += value

    @staticmethod
    def convert_to_czk(value_in_eur: float | int) -> float | int:
        return 25 * value_in_eur

    @classmethod
    def from_json_file(cls, file_path: str):
        with open(file_path, "r", encoding="utf8") as file:
            for row in file:
                data = json.loads(row)
                break
        # name = data['name']
        # balance = data['balance']
        return cls(**data)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner}, balance={self.balance}({self.currency}))"

    def __gt__(self, other) -> bool:
        # >
        self_balance_czk = self.balance * 25 if self.currency == "EUR" else self.balance
        other_balance_czk = other.balance * 25 if other.currency == "EUR" else other.balance
        return self_balance_czk > other_balance_czk

    def __ge__(self, other):
        # >=
        pass

    def __eq__(self, other):
        # ==
        pass

    def __lt__(self, other):
        # <
        pass

    def __le__(self, other):
        # <=
        pass

    def __add__(self, other):
        pass


ba = BankAccount("Tomas", 5_000_000, "EUR")
ba.balance += 500_000

ba.deposit()
print(ba)

ba.convert_to_czk(50)

ba.deposit(500)
type(ba)
BankAccount.deposit(ba, value=500)

ba2 = BankAccount("Veronika", 50_000_000, "CZK")

# ba + ba2
ba >= ba2
ba > ba2

ba
ba2

dir("petr")

"petr".capitalize()

dir(ba)

ba.__dict__

ba.novej_attr = 123
ba.novej_attr

ba.__dict__

(3).__eq__(3)
(3).__dict__
3 == 3

with open("ba.json", "r", encoding="utf8") as file:
    for row in file:
        data = json.loads(row)
        break

ba_petr = BankAccount.from_json_file("ba.json")

ba_petr
