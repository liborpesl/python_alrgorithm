import statistics
import time
import random


def average1(a: int | float, b: int | float):
    return (a + b) / 2


def average2(a: int | float, b: int | float):
    return statistics.mean([a, b])


def average3(*numbers: int | float):
    return statistics.mean(numbers)


def average4(*numbers: int | float):
    return sum(numbers) / len(numbers)


average1(4, 8)
average1(1, 2)

average2(4, 8)
average2(1, 2)

average4(4, 346, 7, 3, 452)
average3(4, 346, 7, 3, 452)

t0 = time.time()

for i in range(5000):
    numbers = [random.randint(1, 1000)
               for i in range(random.randint(10, 1000))]
    average = average3(*numbers)

print(time.time() - t0)

### average3 N = 5000 t=4.409686326980591
### average4 N = 5000 t=2.7052879333496094


t0 = time.time()

for i in range(5000):
    numbers = [random.randint(1, 1000)
               for i in range(random.randint(10, 1000))]
    average = average4(*numbers)

print(time.time() - t0)
