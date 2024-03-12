
import random

class Student:

    def __init__(self, id_number: int):
        self.id_number = id_number
        self.grade = random.choice([1, 2, 3, 4, 5])


chemie = [Student(i + 1) for i in range(3000)]
biologie = [Student(i + 1) for i in range(3000)]


{
    1: [1, 2],
    2: [4, 4],
}

grades = {}
all_students = chemie + biologie
len(all_students)

for student in all_students:
    if student.id_number not in grades.keys():
        grades[student.id_number] = []
        grades[student.id_number].append(student.grade)
    else:
        grades[student.id_number].append(student.grade)


from collections import defaultdict

grades = defaultdict(list)

for student in all_students:
    grades[student.id_number].append(student.grade)

grades[10]

scores = defaultdict(lambda: 0)
scores['Eliska'] += 1
scores

grades = defaultdict(lambda: [])
grades[1].append(1)

grades.default_factory


#############################################

rec1 = tuple((12, "Petr", 155))
rec1[0]
rec1[1]
rec1[2]

rec2 = {"name": "petr", "age": 12, "weight": 155}
rec2["age"]


from collections import namedtuple

DtbRecord = namedtuple("DtbRecord", "age name weight")

type(DtbRecord)
DtbRecord

rec3 = DtbRecord(12, "petr", 155)
rec3[1]
rec3.name
rec3.age

import sys

sys.getsizeof(rec1)
sys.getsizeof(rec2)
sys.getsizeof(rec3)

DtbRecord(weight=123, age=15, name="Tomas")

rec3
rec3._asdict()


from collections import Counter

my_list = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5]

my_counter = Counter(my_list)

my_counter.most_common(1)


from array import array

my_list = list(range(100_000))

my_array = array("i", my_list)

my_list
my_array

sys.getsizeof(my_list)
800

sys.getsizeof(my_array)
400





my_list.append("Krokodyl")
my_list[-3:]

my_array.append("krokodyl")



my_unsigned_array = array("I", my_list)
my_unsigned_array.append(-1)
sys.getsizeof(my_unsigned_array)

my_unsigned_array = array("H", my_list)
my_unsigned_array.append(-1)
sys.getsizeof(my_unsigned_array)


my_signed_array = array("i")
my_signed_array.append(-1)

