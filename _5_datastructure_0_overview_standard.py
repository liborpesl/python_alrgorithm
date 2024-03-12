# import random
#
#
# class Students:
#     def __init__(self, id_number: int):
#         self.id_number = id_number
#         self.grade = random.choice([1, 2, 3, 4, 5, 6])
#
#
#
#
# chemie = [Students(i+1) for i in range(100000)]
# biologie = [Students(i+1) for i in range(100000)]
#
# all_students = chemie + biologie
# print(len(all_students))

import random

list_number = [random.randint(1, 10) for i in range(50)]

print(list_number)


def find_highest_number(list_number):
    if not list_number:
        return None

    max_element = list_number[0]
    for i in list_number:
        if list_number[i] > max_element:
            max_element = list_number[i]
    return max_element


print(find_highest_number(list_number))


list = []
list.insert(0,1)
list.pop()