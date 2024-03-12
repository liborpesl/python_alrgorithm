[658, 925, 342, 886, 126, 697, 334, 474, 447, 312]
[658, 925, 342, 886, 126]
[697, 334, 474, 447, 312]

[1, 3, 5, 7]
[2, 4, 6, 8]

[1, 2, 3, 4, 5, 6, 7, 8]


def merge(left: list, right: list ) -> list:
    """
    funkce, ktera umi spojit dva serazene listy do jednoho noveho a taky serazeneho listu

    """
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    output = []
    ix_left, ix_right = 0, 0

    # dokud je output kratsi nez vstupni listy
    while len(output) < len(left) + len(right):

        # porovnavam itemy na pozicich ix_left a ix_right v listech left a right, ten mensi vezmu (a musim zvysit index)
        if left[ix_left] < right[ix_right]:
            output.append(left[ix_left])
            ix_left += 1
        else:
            output.append(right[ix_right])
            ix_right += 1

        # az se stane, ze list vycerpam, muzu pridat zbytek toho druheho listu
        if ix_left == len(left):
            return output + right[ix_right:]

        if ix_right == len(right):
            return output + left[ix_left:]

    # return output


merge([], [2, 4, 6, 8])


def merge_sort(array: list) -> list:
    """
    rekurzivni funkce, ktera rozdeluje list na levou a pravou cast
    a kterou nasledne rozdeluje a spojuje pomoci rekurzivniho volani sebe sama a volani funkce merge
    """

    if len(array) < 2:
        return array

    ix_middle = len(array) // 2

    return merge(left=merge_sort(array[:ix_middle]),
                 right=merge_sort(array[ix_middle:])
                 )


# print(my_list)
# print(merge_sort(my_list))

# merge_sort(my_list)
