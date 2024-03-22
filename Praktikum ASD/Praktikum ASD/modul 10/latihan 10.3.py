import time
import random

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos -1]:
            A[pos] = A[pos -1]
            pos = pos - 1
        A[pos] = nilai


##for i in range(5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionSort(L)
##    akhir = time.time()
##    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len (L), akhir-awal))

for i in range(5):
    L = list(range(3000))
    L = L[::-1]
    awal = time.time()
    U = insertionSort(L)
    akhir = time.time()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))
