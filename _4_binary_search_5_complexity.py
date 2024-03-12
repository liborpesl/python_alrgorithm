
from _4_binary_search_1_basic import linear_search
from _4_binary_search_2_iter import binary_search_iter
from _4_binary_search_3_recursive import binary_search_recursive
from _4_binary_search_4_bisect import binary_search_bisect

import random
import time

my_list1_size = 1_000
my_list2_size = 1_000_000

my_list1 = [random.randint(1, 1_000_000_000) for i in range(my_list1_size)]
my_list1.sort()

my_list2 = [random.randint(1, 1_000_000_000) for i in range(my_list2_size)]
my_list2.sort()

number_of_searches = 1000

t0 = time.time()
for i in range(number_of_searches):
    number = random.choice(my_list2)
    ix = linear_search(my_list2, number)
print("linear_search", time.time() - t0)


t0 = time.time()
for i in range(number_of_searches):
    number = random.choice(my_list2)
    ix = binary_search_iter(my_list2, number)
print("binary_search_iter", time.time() - t0)


t0 = time.time()
for i in range(number_of_searches):
    number = random.choice(my_list2)
    ix = binary_search_recursive(my_list2, number)
print("binary_search_recursive", time.time() - t0)


t0 = time.time()
for i in range(number_of_searches):
    number = random.choice(my_list2)
    ix = binary_search_bisect(my_list2, number)
print("binary_search_bisect", time.time() - t0)


# linear_search           0.02606987953186035
# binary_search_iter      0.002003908157348633
# binary_search_recursive 0.001996755599975586
# binary_search_bisect    0.001001596450805664
#
# linear_search           56.152036905288696
# binary_search_iter      0.010527372360229492
# binary_search_recursive 0.015538454055786133
# binary_search_bisect    0.00600743293762207


my_functions = [
    linear_search,
    binary_search_iter,
    binary_search_recursive,
    binary_search_bisect,
]

for func in my_functions:
    t0 = time.time()
    for i in range(number_of_searches):
        number = random.choice(my_list1)
        ix = func(my_list1, number)
    print(func.__name__, time.time() - t0)

