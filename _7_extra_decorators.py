import random
import time


def fn1(a):
    print(a)
    return a


fn1(123)


def fn2(funkce, x):
    print("Calling function", funkce.__name__)
    funkce(x)
    print("Called function", funkce.__name__)


fn2(fn1, 123)



def fn3():
    print("Ok, vytvorim ted nejakou dalsi funkci...")

    def fn4():

        print("Ahoj, tady fn4")
        return

    print("fn 4 vytvorena", fn4.__name__)
    return fn4

returned_function = fn3()
returned_function.__name__

returned_function()




# dekorator - funkce, ktera prijma nakou funkci a zase vraci nejakou funkci ...

def null_decorator(funkce):
    print("Vracim funkci bez jakychkoliv zmen")
    return funkce


def fn5():
    print("Ahoj, tady fn5")


fn5_dekorovana = null_decorator(fn5)



@null_decorator
def fn5():
    print("Ahoj, tady fn5")

def fn5():
    print("Ahoj, tady fn5")

fn5 = null_decorator(fn5)


def process_data(a: int, b:int) -> int:
    time.sleep(random.randint(0, 4))
    result = a * b
    return result


def process_data(a: int, b:int) -> int:
    start = time.time()
    time.sleep(random.randint(0, 4))
    result = a * b
    print("funkce trvala ", time.time() - start)
    return result


def funkce(*args, **kwargs):
    print(args)
    print(kwargs)


funkce(1,2,3, k=555)


def timer(func):

    def nova_funkce(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("ubehlo:", end-start)

        return result

    return nova_funkce
    # return nejaka funkce...


def process_data(a: int, b:int) -> int:
    time.sleep(random.randint(0, 4))
    result = a * b
    return result


timed_process_data = timer(process_data)
timed_process_data(5, 2)
process_data(5, 2)


@timer
@timer
@timer
def process_data(a: int, b:int) -> int:
    time.sleep(random.randint(0, 4))
    result = a * b
    return result


class NewClass:
    pass


process_data(6,7)

