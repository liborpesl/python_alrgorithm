
# 3 * 5 = 5 + 5 + 5
# 3 * 5 = 3 + 3 + 3 + 3 + 3

# 3 * 5 = 5 + 5 + 5
# 3 * 5 = 5 + (2*5)
#
# 1 * n = n
# 0 * n = 0

def multiply_positive(x, y):
    if x == 0 or y == 0:
        return 0

    return y + multiply_positive(x -1, y)



multiply_positive(10, 10)
multiply_positive(0, 10)
multiply_positive(10, 0)
multiply_positive(0, 0)
multiply_positive(3, 7)
multiply_positive(7, 3)
multiply_positive(10, 10)


def multiply(x: int, y: int):
    if x == 0 or y == 0:
        return 0

    if x > 0:
        return y + multiply(x - 1, y)
    else:
        return -y + multiply(x + 1, y)


multiply(10, 10)
multiply(0, 10)
multiply(10, 0)
multiply(0, 0)
multiply(3, 7)
multiply(7, 3)
multiply(10, 10)

multiply(-10, 0)
multiply(-0, 0)
multiply(-3, 7)
multiply(-7, 3)
multiply(-10, 10)

multiply(-3, -7)
multiply(-7, -3)
multiply(-10, -10)
