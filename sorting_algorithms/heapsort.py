import time


def max_heapify(A, i):
    global heapsize
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    global heapsize
    heapsize = len(A) - 1
    n = (len(A) - 1) // 2
    for i in range(n, -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    global heapsize
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        max_heapify(A, 0)


def begin_sorting_heap(A):
    begin = time.time()

    build_max_heap(A)
    heap_sort(A)
    end = time.time()

    result = round(end - begin, 9)
    print(f"Czas wykonania: {result} s")
