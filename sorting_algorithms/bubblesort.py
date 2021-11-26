import time


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def begin_sorting_bubble(A):
    begin = time.time()
    bubble_sort(A)
    end = time.time()
    result = round(end - begin, 7)
    print(f"Czas wykonania: {result} s")
