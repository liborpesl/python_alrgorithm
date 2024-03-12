import time
import random


def a():
    print("a")
    time.sleep(random.randint(1, 2))
    if random.random() < 0.1:
        c()


def b():
    print("b")
    time.sleep(random.randint(1, 2))


def c():
    print("c")
    time.sleep(random.randint(1, 2))

    if random.random() < 0.5:
        a()


def d():
    for i in range(10):
        print(i)
        a()
        b()
        c()


if __name__ == '__main__':
    d()
