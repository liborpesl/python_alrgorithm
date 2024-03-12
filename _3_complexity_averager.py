



def average3(*numbers: int | float):
    return statistics.mean(numbers)


def average4(*numbers: int | float):
    return sum(numbers) / len(numbers)