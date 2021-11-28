import random
import time


def quicksort(a, p, r):
    if (r - p) < 2:
        return

    q = random.randrange(p, r - 1)
    q_new = partition(a, q, p, r)

    quicksort(a, p, q_new)
    quicksort(a, q_new + 1, r)


def partition(a, q, p, r):
    a[q], a[p] = a[p], a[q]
    pivot = a[p]
    i = p + 1
    for j in range(p + 1, r):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i = i + 1

    a[i - 1], a[p] = a[p], a[i - 1]
    return i - 1


def begin_sorting_quicksort(A):
    begin = time.time()
    quicksort(A, 0, len(A) - 1)
    end = time.time()
    result = round(end - begin, 3)
    print(f"Czas wykonania: {result} s")
