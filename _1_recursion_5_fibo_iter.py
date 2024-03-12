
def fibo(nth: int):
    if nth <= 0:
        raise ValueError("fibo defined for positive numbers only")

    fibo_values = [0, 1]
    while len(fibo_values) < nth:
        next_fibo_element = fibo_values[-1] + fibo_values[-2]
        fibo_values.append(next_fibo_element)

    print(fibo_values)
    # return fibo_values[nth - 1]
    return fibo_values[-1]
