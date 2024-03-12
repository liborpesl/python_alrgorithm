
import random
import heapq
import time


my_list = [random.randint(0, 999) for i in range(100)]

my_list

heapq.heapify(my_list)

my_list[:10]

heapq.nsmallest(5, my_list)
heapq.nlargest(5, my_list)


def get_n_smallest(n: int, li: list):
    li_copy = li[:]
    list_of_smallest = []

    for x in range(n):
        list_of_smallest.append(li_copy[x])

    return list_of_smallest


def get_n_smallest(n: int, li: list):
    li_copy = li[:]
    li_copy.sort()
    return li_copy[:n]


t0 = time.time()
for i in range(10):
    my_list = [random.randint(0, 999) for i in range(1_000_000)]
    get_n_smallest(random.randint(1, 20), my_list)
print("elapsed:", time.time() - t0)


t0 = time.time()
for i in range(10):
    my_list = [random.randint(0, 999) for i in range(1_000_000)]
    heapq.nsmallest(random.randint(1, 20), my_list)
print("elapsed:", time.time() - t0)


get_n_smallest(10, my_list) == heapq.nsmallest(10, my_list)

