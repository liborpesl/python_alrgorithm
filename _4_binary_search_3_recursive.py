
import random

my_list = [random.randint(1, 1000) for _ in range(100)]
my_list.sort()
print(my_list[:10])


def binary_search_recursive(li: list, number: int, left=None, right=None):

    if left is None:
        left = 0
    if right is None:
        right = len(li) - 1

    if (left <= right):

        middle = (left + right) // 2

        middle_value = li[middle]

        if middle_value == number:
            return middle
        elif middle_value > number:
            right = middle - 1
            return binary_search_recursive(li, number, left, right)
        else:
            left = middle + 1
            return binary_search_recursive(li, number, left, right)

    return None


print(binary_search_recursive(my_list, 100))
my_list[12]
