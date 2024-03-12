

# 5! = 5 * 4 * 3 * 2 * 1
# 0! = 1

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative N not allowed")

    values = range(1, n+1)

    result = 1

    for value in values:
        # result = result * value
        result *= value

    return result



