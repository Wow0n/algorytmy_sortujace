import time


def mergesort(array):
    if len(array) > 1:

        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def begin_sorting_merge(A):
    begin = time.time()
    mergesort(A)
    end = time.time()
    result = round(end - begin, 3)
    print(f"Czas wykonania: {result} s")
