
# smallest - largest

[10, 29, 31, 23, 6]  # start
[6, 10, 23, 29, 31]  # ocekavany vysledek

# algoritmus
[[10, 29], 31, 23, 6]
[10, [29, 31], 23, 6]

[10, 29, [31, 23], 6]
[10, 29, [23, 31], 6]

[10, 29, 23, [31, 6]]
[10, 29, 23, [6, 31]]

[10, 29, 23, 6, 31]


def bubble_sort(array: list):
    n = len(array)

    for i in range(n):
        already_sorted = True

        # print(f"{i=}")

        for j in range(n -1 -i):  # i je cislo vnejsi iterace, po dobehle prvni iteraci je nejvetsi element uplne nejvic vpravo = vlastnost bubble...
            # print(f"{j=}")
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

                already_sorted = False

        if already_sorted:
            return array

    return array


if __name__ == '__main__':

    bubble_sort([10, 29, 31, 23, 6])

    bubble_sort([6, 19, 23, 29, 31])

