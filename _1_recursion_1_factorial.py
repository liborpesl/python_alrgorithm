
import sys


# Toto bude pokracovat donekonecna
def bad_factorial(n: int):
    print("Called bad_factorial, n=", n)
    return bad_factorial(n-1)


bad_factorial(5)  # toto skonci chybou


def factorial(n: int):

    # safe guards - abychom se vyhnuli chybam
    if not isinstance(n, int):
        raise TypeError("Invalid input type, factorial defined only for integers.")

    if n < 0:
        raise ValueError("Invalid input, factorial defined for non-negative numbers only.")

    # terminating conditions - zakladni pripady ktere jsou definovane a pri kterych rekurze konci
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1

    # hezci zapis techto alternativnich pripadu
    if n in (0, 1):
        return 1

    # faktorial + rekurznivni volani
    return n * factorial(n - 1)


factorial(10)


##############################################

def indent(n) -> str:
    return " " * n


def factorial_didactic(n: int):
    global active_calls
    active_calls += 1

    if not isinstance(n, int):
        raise TypeError("Invalid input type, factorial defined only for integers.")

    if n < 0:
        raise ValueError("Invalid input, factorial defined for non-negative numbers only.")

    if n in (0, 1):
        print(f"{indent(active_calls)}Factorial of {n} is defined as 1")
        active_calls -= 1
        return 1

    print(f"{indent(active_calls)}Factorial of {n} = {n} * {n - 1}!")
    result = n * factorial_didactic(n - 1)
    print(f"{indent(active_calls)}Got result of {n - 1}!")
    active_calls -= 1
    return result


active_calls = 0
factorial_didactic(50)


sys.getrecursionlimit()

sys.setrecursionlimit(5000)
sys.getrecursionlimit()


factorial_didactic(6000)
