

import random

my_list = [random.randint(1, 1000) for _ in range(100)]
my_list.sort()
print(my_list[:10])

number = 9

#                 R  L
# [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]

# L=6
# R=7
# M = (L + R) // 2


def binary_search_iter(li: list, number: int):

    left = 0
    right = len(li) - 1

    while (left <= right):

        middle = (left + right) // 2

        middle_value = li[middle]

        if middle_value == number:
            return middle
        elif middle_value > number:
            right = middle - 1
        else:
            left = middle + 1

    return None



print(binary_search_iter(my_list, 105))

my_list[13]



def binary_search_iter_didactic(li: list, number: int):

    left = 0
    right = len(li) - 1

    while (left <= right):

        middle = (left + right) // 2
        print(f"{left=}, {right=}, {middle=}")

        middle_value = li[middle]

        if middle_value == number:
            print("found middle", middle, middle_value)
            return middle

        elif middle_value > number:
            right = middle - 1
            print("move to left")
        else:
            left = middle + 1
            print("move to right")

    print("number not there")
    return None



print(binary_search_iter_didactic(my_list, 105))

print(binary_search_iter_didactic(my_list, 105000))
