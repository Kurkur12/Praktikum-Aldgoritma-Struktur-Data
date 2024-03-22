from timeit import timeit
import random

print("====Insertion Sort===")

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos -1]:
            A[pos] = A[pos -1]
            pos = pos - 1
        A[pos] = nilai

for i in range(5):
    siap = "from __main__ import insertionSort,L"
    L = list(range(3000))
    t = timeit("insertionSort(L)", setup=siap, number=1)
    print("Jumlah adalah %d bilangan, memerlukan %9.7f detik" % (len(L), t))
