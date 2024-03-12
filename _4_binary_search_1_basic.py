
my_list = [1, 3, 4, 6, 7, 8, 10, 13, 14, 18, 19, 21, 24, 37, 40, 45, 71]

searched_number = 50

for ix, number in enumerate(my_list):
    if searched_number == number:
        print(f"Je to tam na pozici {ix}")


len(my_list)


def linear_search(list_of_elements: list, searched_element):
    for ix, element in enumerate(list_of_elements):
        if searched_element == element:
            return ix

    return None
