import time

import numpy as np


def counting_sort(A, B, k):
    C = np.full(k + 1, 0)

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B


def begin_sorting_counting(A):
    begin = time.time()
    B = np.full(len(A), 0)
    counting_sort(A, B, len(A))
    end = time.time()
    result = round(end - begin, 3)
    print(f"Czas wykonania: {result} s")
