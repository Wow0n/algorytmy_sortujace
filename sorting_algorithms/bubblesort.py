import time


def bubble_sort(array):
    swap = True

    while swap:
        swap = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True


def begin_sorting_bubble(A):
    begin = time.time()
    bubble_sort(A)
    end = time.time()
    result = round(end - begin, 7)
    print(f"Czas wykonania: {result} s")
