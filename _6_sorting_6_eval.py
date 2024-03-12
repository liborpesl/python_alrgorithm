
import random
import time

from _6_sorting_2_bubble import bubble_sort
from _6_sorting_3_insertion import insert_sort
from _6_sorting_4_quicksort import quick_sort
from _6_sorting_5_merge import merge_sort


REPETITION = 5
BATCH_SIZE = 10_000

# sorting_function = bubble_sort


list_of_sorting_functions = [bubble_sort, insert_sort, quick_sort, merge_sort]
list_of_sorting_functions = [quick_sort, merge_sort, insert_sort, bubble_sort]


for sorting_function in list_of_sorting_functions:

    random.seed(777)
    t0 = time.time()
    for i in range(REPETITION):
        my_list = [random.randint(0, 999_999_999) for i in range(BATCH_SIZE)]
        my_list = sorting_function(my_list)
    print(sorting_function.__name__, "elapsed time:",time.time() - t0, "N:", BATCH_SIZE)


bubble_sort 4.159661054611206
insert_sort 1.4223015308380127
quick_sort 0.10286712646484375
merge_sort 0.1780390739440918



quick_sort elapsed time: 0.0010008811950683594 N: 100
quick_sort elapsed time: 0.31240081787109375 N: 10000

merge_sort elapsed time: 0.0019969940185546875 N: 100
merge_sort elapsed time: 0.5261168479919434 N: 10000

insert_sort elapsed time: 0.002516031265258789 N: 100
insert_sort elapsed time: 28.966516256332397 N: 10000

bubble_sort elapsed time: 0.00402379035949707 N: 100
bubble_sort elapsed time: 70.46047592163086 N: 10000
