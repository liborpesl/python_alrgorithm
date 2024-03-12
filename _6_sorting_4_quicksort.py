
import random
[8, 5, 6, 4, 2 ,6,6]

pivot = 6

small = [5, 4, 2]
same = [6,6,6]
large = [8]


# return recursive_call(small) + same + recursive_call(large)


def quick_sort(array: list) -> list:
    """
    chci rozdelit list na 3 sub listy,
    small - mensi hodnoty,
    same - stejne hodnoty,
    large - vetsi hodnoty

    a na ne dal aplikovat stejny postup rozdelovani
    ... az se stane ze list je prazdny nebo jednoclenny - potom vim, ze je serazeny a muzu zacit vracet vysledek
    vysledek = small + same + large
    """


    if len(array) < 2:  # ukoncovaci podminka rekurze
        return array

    pivot = random.choice(array)  # pivot muze byt nahodne zvoleny (je to rychlejsi nez pocitat treba median)

    # distribuce hodnot do listu small, same, large...
    small, same, large = [], [], []

    for element in array:
        if element == pivot:
            same.append(element)
        elif element < pivot:
            small.append(element)
        else:
            large.append(element)

    # print(f"{small=}")
    # print(f"{same=}")
    # print(f"{large=}")
    # return a rekurzivni volani
    return quick_sort(small) + same + quick_sort(large)


if __name__ == '__main__':

    my_list = [random.randint(0, 999) for i in range(100)]
    print(my_list)
    print(quick_sort(my_list))
    print(my_list)
