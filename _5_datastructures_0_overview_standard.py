import random
import sys
import time

list
tuple
set
dict

# list
my_list = [1, 2, 3]
my_list[1] = 200
print(my_list)

print(my_list)
my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list)

print(my_list)
my_list.append(4)
my_list.append(5)
print(my_list)

print(my_list)
my_list.pop(2)
print(my_list)

my_list[1]

my_list2 = my_list[:]
my_list2 == my_list
my_list2
my_list

my_list2 is my_list

my_list = []
my_list2 = my_list

my_list
my_list2

my_list.append(123)
print(my_list)
print(my_list2)


class A:
    pass


a = A()

my_list = [1, 1.1, True, None, "asdf", [123, 456], print, A, a]
print(my_list)

my_list = [str.upper, str.title, str.lower, str.strip]
my_string = "    petr    "

for method in my_list:
    print(method, '->>', method(my_string))

my_list = [1, 2, 3]
if my_list == [3, 2, 1]:
    print("stejne")
else:
    print("jine")

sys.getsizeof([1, 2, 3, 4, 5, 6])

my_list = []
print(len(my_list), sys.getsizeof(my_list))
for x in range(20):
    my_list.append(x)
    print(len(my_list), sys.getsizeof(my_list))

my_list = [1, 2, 3, [4, 5, 6, [7, 8, 9]]]
my_list

my_list = [1, 2, 3]
my_list.append(my_list)
my_list[-1][-1][-1][-1]

my_list[-1] is my_list

my_list = [1, 2, 3]
hash(my_list)

print({my_list: 123})

print({tuple(my_list): 123})

my_list = list(range(1_000_000))
my_list[:10]
random.shuffle(my_list)
my_list[:10]

t0 = time.time()
for i in range(100):
    number = random.randint(1, 9_999_999)
    print(number, number in my_list)
print("total time: ", time.time() - t0)

t0 = time.time()
my_set = set(my_list)
for i in range(100):
    number = random.randint(1, 9_999_999)
    print(number, number in my_set)
print("total time: ", time.time() - t0)

# total time:  13.31482481956482
# total time:  12.73851752281189
#
# total time:  0.360302209854126


sys.getsizeof(my_list)
8000056 / 1024 / 1024

sys.getsizeof(my_set)

33554648 / 1024 / 1024

my_set.add([1, 2, 3])

set(["Banan"] * 10)

my_set1 = set(list(range(10)))
my_set2 = set(list(range(2, 16, 2)))

my_set1
my_set2

print(my_set1, "\n", my_set2)

my_set1.intersection(my_set2)
my_set1 & my_set2

my_set1.difference(my_set2)
my_set1 - my_set2
my_set2 - my_set1

my_set1.union(my_set2)
my_set1 | my_set2

my_set1 + my_set2

my_set1.symmetric_difference(my_set2)
my_set1 ^ my_set2

my_dict1 = {1: 1, 2: 2, 3: 3}
my_dict2 = {2: 2, 4: 4, 3: 3}

for key in my_dict1.keys():
    print(key)

for value in my_dict1.values():
    print(value)

for key, value in my_dict1.items():
    print(key, value)

my_dict2.keys() & my_dict1.keys()
my_dict2.keys() | my_dict1.keys()

my_dict2.keys() - my_dict1.keys()
my_dict1.keys() - my_dict2.keys()

my_dict2.keys() ^ my_dict1.keys()


class Student:

    def __init__(self, id_number: int):
        self.id_number = id_number
        self.grade = random.choice([1, 2, 3, 4, 5])



student = Student(1)
student.grade

my_set = set()
my_set.add(student)


chemie = [Student(i + 1) for i in range(10000)]
biologie = [Student(i + 1) for i in range(10000)]

random.shuffle(chemie)
random.shuffle(biologie)

chemie[0].id_number
biologie[0].id_number

t0 = time.time()
for student_bio in biologie:
    for student_chem in chemie:
        if student_bio.id_number == student_chem.id_number:
            print(student_bio.id_number, student_bio.grade, student_chem.grade)
            break
print(time.time() - t0)

N = 3000
0.50
0.5721228122711182

N = 1000
7.580715894699097
6.903454542160034



t0 = time.time()

chemie_dict = {}
for student_chem in chemie:
    chemie_dict[student_chem.id_number] = student_chem

# chemie_dict = {student_chem.id_number: student_chem for student_chem in chemie}

for student_bio in biologie:
    student_chem = chemie_dict[student_bio.id_number]
    print(student_bio.id_number, student_bio.grade, student_chem.grade)
print(time.time() - t0)

## NESTED FOR LOOPS
N = 3000
0.50
0.5721228122711182

N = 10000
7.580715894699097
6.9

# DICT - AS DTB
N = 3000
0.0646510124206543
0.19266414642333984

N = 10000


# LIST
# N: 3000 -> 10000
# t: -> 13.8x

# DICT
# N: 3000 -> 10000 | 3.3x
# t: -> 3x


