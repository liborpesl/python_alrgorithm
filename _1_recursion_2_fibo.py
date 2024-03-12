import time


# pocita n-te cislo ve fibonacciho posloupnosti
def fibo(nth: int) -> int:
    if nth <= 0:
        raise ValueError("fibo defined for positive numbers")

    if nth == 1:
        return 0
    if nth == 2:
        return 1
    else:
        return fibo(nth - 1) + fibo(nth - 2)  # rekurze zde roste geometrickou radou - funkce je velmi neefektivni


# pri i>35 pozorujeme vyrazne zpomaleni
for i in range(1, 37):
    t0 = time.time()
    result = fibo(i)
    duration = time.time() - t0
    print(f"Fibo({i}) = {result}, Duration: {duration}")
