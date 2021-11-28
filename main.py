import sys

import numpy

from sorting_algorithms.countingsort import begin_sorting_counting
from sorting_algorithms.heapsort import begin_sorting_heap
from sorting_algorithms.mergesort import begin_sorting_merge
from sorting_algorithms.quicksort import begin_sorting_quicksort

if __name__ == '__main__':
    print("HeapSort:")
    A = numpy.load("arrays/arrayRandom.npy")
    begin_sorting_heap(A)
    A = numpy.load("arrays/arrayMinToMax.npy")
    begin_sorting_heap(A)
    A = numpy.load("arrays/arrayMaxToMin.npy")
    begin_sorting_heap(A)

    print("\nCountingSort:")
    A = numpy.load("arrays/arrayRandom.npy")
    begin_sorting_counting(A)
    A = numpy.load("arrays/arrayMinToMax.npy")
    begin_sorting_counting(A)
    A = numpy.load("arrays/arrayMaxToMin.npy")
    begin_sorting_counting(A)

    print("\nMergeSort:")
    A = numpy.load("arrays/arrayRandom.npy")
    begin_sorting_merge(A)
    A = numpy.load("arrays/arrayMinToMax.npy")
    begin_sorting_merge(A)
    A = numpy.load("arrays/arrayMaxToMin.npy")
    begin_sorting_merge(A)

    print("\nQuickSort:")
    A = numpy.load("arrays/arrayRandom.npy")
    begin_sorting_quicksort(A)
    A = numpy.load("arrays/arrayMinToMax.npy")
    begin_sorting_quicksort(A)
    A = numpy.load("arrays/arrayMaxToMin.npy")
    begin_sorting_quicksort(A)
