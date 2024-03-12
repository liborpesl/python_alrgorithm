import bisect

my_list = [1, 3, 6, 11, 20]

bisect.bisect_left(my_list, 2)
my_list.insert(1, 2)

my_list
[1, 2, 3, 6, 11, 20]

my_list = [1, 3, 3, 3, 3, 3, 3, 6, 11, 20]
bisect.bisect_left(my_list, 3)
bisect.bisect_right(my_list, 3)

bisect.bisect(my_list, 3)

bisect.insort_left(my_list, 11)
print(my_list)

bisect.insort_left(my_list, 40)
print(my_list)

bisect.insort_left(my_list, 4)
print(my_list)

[-100, 1, 2, 3]

-100
0


def binary_search_bisect_bad(li: list, number: int):
    ix = bisect.bisect_left(li, number)

    if li[ix] == number:
        return ix
    else:
        return None


def binary_search_bisect(li: list, number: int):
    ix = bisect.bisect_left(li, number)

    if ix != len(li) and li[ix] == number:
        return ix
    else:
        return None


print(binary_search_bisect([4, 5, 8, 9], 200))
