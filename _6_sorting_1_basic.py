

import random

random.seed(575)  # toto zpusobi, ze hodnoty vygenerovane "nahodne" budou pokazde stejne sekvence nahodnych cisel
my_list = [random.randint(1, 999) for i in range(100)]

# funkce sorted vytvori novy, serazeny list, puvodni list zustane neserazeny
print(my_list)
my_sorted_list = sorted(my_list)
print(my_list)
print(my_sorted_list)


random.seed(575)
my_list = [random.randint(1,999) for i in range(100)]

# metoda list.sort seradi list, na kterem je pouzita
print(my_list)
my_list.sort()
print(my_list)


my_dict = {"Xavier": 1, "Petr": 5, "Honza": 10, "Eliska": 50}

sorted(my_dict)
sorted(my_dict, key=my_dict.get)

min(my_dict, key=my_dict.get)
max(my_dict, key=my_dict.get)


# timsort - algoritmus, ktery je v pythonu pouzit pro sorting
# kompozitni algoritmus
# vyuziva toho, ze v datech realneho sveta casto byvaji "ostruvky" - sekvence cisel - ktere jsou uz serazene


