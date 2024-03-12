import random
import bisect
import sys
# my_list = [random.randint(1,100) for _ in range(100)]
# my_list.sort()
# print(my_list[:10])






# # def find_binary_search(my_list: list, n: int):
# #     left = 0
# #     right = len(my_list) - 1
# #
# #     while left <= right:
# #         mid = (left + right) // 2
# #         if my_list[mid] == n:
# #             return mid
# #         elif my_list[mid] > n:
# #             right = mid - 1
# #         else:
# #             left = mid + 1
# #
# #     return f"The value {n} was not found"
#
#
# print(find_binary_search(my_list, 20))


# list_array = [random.randint(1,100) for _ in range(10)]
#
# list_array.sort()
#
#
# print(list_array)
#
# print(bisect.bisect_left(list_array,30))
#
# print(sys.getsizeof(my_list))

my_list = {1,2,564,8,78}
my_list2 = {56,48,65,78,12}

print(my_list | my_list2)
print(my_list & my_list2)
print(my_list ^ my_list2)
print(my_list - my_list2)

my_list.copy()
