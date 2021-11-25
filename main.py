import sys

from functions.read_integers import read_integers
from sorting_algorithms.bubblesort import begin_sorting_bubble
from sorting_algorithms.countingsort import begin_sorting_counting
from sorting_algorithms.heapsort import begin_sorting_heap
from sorting_algorithms.quicksort import begin_sorting_quicksort

if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 6)

    print("QuickSort:")
    A = read_integers("arrays/arrayRandom.txt")
    begin_sorting_quicksort(A)
    A = read_integers("arrays/arrayMinToMax.txt")
    begin_sorting_quicksort(A)
    A = read_integers("arrays/arrayMaxToMin.txt")
    begin_sorting_quicksort(A)

    print("\nHeapSort:")
    A = read_integers("arrays/arrayRandom.txt")
    begin_sorting_heap(A)
    A = read_integers("arrays/arrayMinToMax.txt")
    begin_sorting_heap(A)
    A = read_integers("arrays/arrayMaxToMin.txt")
    begin_sorting_heap(A)

    print("\nCountingSort:")
    A = read_integers("arrays/arrayRandom.txt")
    begin_sorting_counting(A)
    A = read_integers("arrays/arrayMinToMax.txt")
    begin_sorting_counting(A)
    A = read_integers("arrays/arrayMaxToMin.txt")
    begin_sorting_counting(A)

    print("\nBubbleSort:")
    A = read_integers("arrays/arrayRandom.txt")
    begin_sorting_bubble(A)
    A = read_integers("arrays/arrayMinToMax.txt")
    begin_sorting_bubble(A)
    A = read_integers("arrays/arrayMaxToMin.txt")
    begin_sorting_bubble(A)
