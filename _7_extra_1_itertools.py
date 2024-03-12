
import itertools
import random
import time
from typing import Iterable

# from more_itertools import b

names = ["Petr", "Tomas", "Hanka", "Eliska"]
surnames = ["List", "Okurka", "Kopecka"]
ages = [20, 25, 15, 20]

for i in range(len(names)):
    print(names[i], surnames[i])

for name, surname in zip(names, surnames):
    print(name, surname)

for record in zip(names, surnames, ages):
    print(record)

for record in itertools.zip_longest(names, surnames, ages):
    print(record)



for i in itertools.count(1):
    print(i)
    time.sleep(0.5)


for i in itertools.cycle(["Petr", "Pepa"]):
    print("Hraje", i)
    time.sleep(0.3)



def random_generator():
    while True:
        yield random.random()

for i in random_generator():
    print(i)
    time.sleep(0.3)

# for batch in more_itertools.batched(random_generator(), 10):
#     print(batch)
#     time.sleep(1)


def my_batched(data: Iterable, n: int):
    batch = []
    for x in data:
        batch.append(x)

        if len(batch) == n:
            yield batch
            batch = []


for batch in my_batched(random_generator(), 5):
    print(batch)
    time.sleep(5)


def numbers():
    while True:
        yield random.randint(0, 10000000)

def times_two(data):
    for x in data:
        yield x * 2

def add_one(data):
    for x in data:
        yield x + 1


for batch in my_batched(add_one(times_two(numbers())), 5):
    print(batch)
    time.sleep(3)



numbers = [1, 3, 5, 7,  8]
          [1, 4, 9, 16, 24]
          [1, 3, 15, 105, 840]
          [1, '1_3', '1_3_5', '1_3_5_7', '1_3_5_7_8']
list(itertools.accumulate(numbers))

def fn(a, b):
    return f"{a}_{b}"

list(itertools.accumulate(numbers, fn))



list1 = [3124,65432,74234,234]
list2 = [1,4,7,34]
list3 = [234,6,8,2,15,7,9]

for x in list1:
    print(x)
for x in list2:
    print(x)
for x in list3:
    print(x)

for x in itertools.chain(list1, list2, list3):
    print(x)
    


