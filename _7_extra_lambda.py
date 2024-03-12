def fn(a, b):
    return a * b


(lambda a, b: a * b)(3, 4)
moje_lambda_fn = (lambda a, b: a * b)

moje_lambda_fn(5, 7)


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

def get_balance(ba):
    return ba.balance

my_list = [
    BankAccount(234),
    BankAccount(53673),
    BankAccount(235),
]
my_list.sort(key=lambda ba: ba.balance)


for ba in my_list:
    print(ba.balance)

