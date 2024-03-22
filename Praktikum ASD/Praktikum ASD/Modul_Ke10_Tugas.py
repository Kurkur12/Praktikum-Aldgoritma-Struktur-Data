####==================== Nomor 1 ====================
####Menggunakan timeit
##from timeit import timeit
##import random
##
##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1, n+1):
##        hasilnya += i
##    return hasilnya
##
##def jumlahkan_cara_2(n):
##    return (n*(n+1))/2
##
##def insertionsort(a):
##    for i in range(1, len(a)):
##        nilai = a[i]
##        pos = i
##        while pos > 0 and nilai < a[pos - 1]:
##            a[pos] = a[pos-1]
##            pos -= 1
##        a[pos] = nilai
##
##
##x = 1000
##y = [4, 5, 1, 2, 8, 5, 10, 6]
##
##def jml1():
##    jumlahkan_cara_1(x)
##def jml2():
##    jumlahkan_cara_2(x)
##def inst():
##    insertionsort(y)
##
##if __name__ == '__main__':
##    import timeit
##    print("=============== jumlahkan_cara_1 ===============")
##    print(timeit.timeit("jml1()", setup="from __main__ import jml1"))
##    print("=============== jumlahkan_cara_2 ===============")
##    print(timeit.timeit("jml2()", setup="from __main__ import jml2"))
##    print("=============== insertionSort ===============")
##    print(timeit.timeit("inst()", setup="from __main__ import inst"))


##Menggunakan Best Scenario, Average case, Worst case
##import random
##import time
##
##print("========================= jumlah cara ke 1 =========================")
##def jumlahkan_cara_1(n):
##    hasilnya = 0
##    for i in range(1, n+1):
##        hasilnya += i
##    return hasilnya
##
##print("cara ke 1", jumlahkan_cara_1(1000000))
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_1(1000000)
##    akhir = time.time()
##    print("jumlah adalah %d,memerlukan waktu %9.8f detik" % (h, akhir-awal))
##
##
##print("========================= jumlah cara ke 2 =========================")
##def jumlahkan_cara_2(n):
##    return (n * (n + 1)) / 2
##
##print("cara ke 2", jumlahkan_cara_2(1000000))
##for i in range(5):
##    awal = time.time()
##    h = jumlahkan_cara_2(1000000)
##    akhir = time.time()
##    print("jumlah adalah %d,memerlukan waktu %9.8f detik" % (h, akhir-awal))
##

##import random
##import time
##
####print("========================= Insertion Sort =========================")
##def insertionsort(a):
##    for i in range(1, len(a)):
##        nilai = a[i]
##        b = i
##        while b > 0 and nilai < a[b - 1]:
##            a[b] = a[b-1]
##            b -= 1
##        a[b] = nilai
##
##
##print("========================= Average Case =========================")
##for i in range(5):
##    L = list(range(3000))
##    random.shuffle(L)
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %
##          (len(L), akhir-awal))
##
##print("========================= Worst Case =========================")
##for i in range(5):
##    L = list(range(3000))
##    L = L[::-1]
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %
##          (len(L), akhir-awal))
##
##print("========================= Best Case =========================")
##for i in range(5):
##    L = list(range(3000))
##    awal = time.time()
##    U = insertionsort(L)
##    akhir = time.time()
##    print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %
##          (len(L), akhir-awal))


##==================== Nomor 2 ====================
import time
import random
RUN = 32
def insertionSort(arr, left, right):
    for i in range(left + 1, right+1):
        temp = arr[i]
        j = i - 1
        while j >= left and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

# merge sorted
def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []

    for i in range(0, len1):
        left.append(arr[l + i])

    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1

# timmsort
def timSort(arr, n):
    for i in range(0, n, RUN):
        insertionSort(arr, i, min((i+31), (n-1)))

    size = RUN
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))
            merge(arr, left, mid, right)
        size = 2*size


g = [6, 20, 8, 24, 17]
n = len(g)
print("g = ", g)
z = [6, 20, 8, 24, 17]
print("z = ", z)
a = [8, 7, 3, 5, 6, 8, 1]
print("a = ", a)

# timsort
timSort(g, len(g))
print("=============== timsort ===============")
print("g = ", g)

# a.sort()
print("=============== a.sort() ===============")
a.sort()
print("a = ", a)

# Sorted
z = [6, 20, 8, 24, 17]
print("=============== sorted ===============")
sorted(z)
print("z = ", z)


print("============================== Best Case Sorted ==============================")

def bestcase():
    for i in range(5):
        L = list(range(3000))
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))


bestcase()


print("============================== Average Case Sorted ==============================")

def averagecase():
    for i in range(5):
        L = list(range(3000))
        random.shuffle(L)
        awal = time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L), akhir - awal))

averagecase()


print("============================== Worst Case Sorted ==============================")

def worstcase():
    for i in range(5):
        L = list(range(3000))
        L = L[::-1]
        awal=time.time()
        U = sorted(L)
        akhir = time.time()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))
worstcase()



####==================== Nomor 3(a) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_a(n):
##    test = 0
##    for i in range(n):
##        for j in range(n):
##            test = test + i * j
##
##def uji_tiga_a(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_a"
##    for i in jangkauan:
##        t = timeit.timeit("tiga_a(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##
##n = 10
##LS = uji_tiga_a(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()





####==================== Nomor 3(b) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_b(n):
##    test = 0
##    for i in range(n):
##        for j in range(i):
##            test = test + i * j
##
##def uji_tiga_b(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_b"
##    for i in jangkauan:
##        t = timeit.timeit("tiga_b(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##
##n = 10
##LS = uji_tiga_b(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()



####==================== Nomor 3(c) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_c(n):
##    test = 0
##    for i in range(n):
##        test = test+1
##    for j in range(n):
##        test = test - 1
##
##def uji_tiga_c(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_c"
##    for i in jangkauan:
##        t = timeit.timeit("tiga_c(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = uji_tiga_c(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()





####==================== Nomor 3(d) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_d(n):
##    i = n
##    while i > 0:
##        k = 2 + 2
##        i = i // 2
##
##
##def uji_tiga_d(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_d"
##    for i in jangkauan:
##        ##print('i = ',i)
##        t = timeit.timeit("tiga_d(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##n = 1000
##LS = uji_tiga_d(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()





####==================== Nomor 3(e) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_e(n):
##    for i in range(n):
##        for j in range(n):
##            for k in range(n):
##                m = i + j + k + 2019
##
##
##def uji_tiga_e(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_e"
##    for i in jangkauan:
##        t = timeit.timeit("tiga_e(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = uji_tiga_e(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()




####==================== Nomor 3(f) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_f(n):
##    for i in range(n):
##        for j in range(i):
##            for k in range(j):
##                m = i + j + k + 2019
##
##
##def uji_tiga_f(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_f"
##    for i in jangkauan:
##        t = timeit.timeit("tiga_f(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = uji_tiga_f(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()





####==================== Nomor 3(g) ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def tiga_g(n):
##    for i in range(n):
##        if i % 3 == 0:
##            for j in range(n // 2):
##                j+=j
##        elif i % 2 == 0:
##            for j in range(5):
##                j+=j
##        else:
##            for j in range(n):
##                j+=j
##
##def uji_tiga_g(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tiga_g"
##    for i in jangkauan:
##        t = timeit.timeit("tiga_g(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = uji_tiga_g(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()



####==================== Nomor 7 ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def nomor_tujuh(n):
##    L = list(range(30))
##    L = L[::-1]
##    for i in range(n):
##        L.append(n)
##            
##
##def pengujian(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import nomor_tujuh"
##    for i in jangkauan:
##        ##print('i = ',i)
##        t = timeit.timeit("nomor_tujuh(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##
##n = 10
##LS = pengujian(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
##
####==================== Nomor 8 ====================
##import timeit
##import matplotlib.pyplot as plt
##
##def nomor_delapan(n):
##    L = list(range(30))
##    L = L[::-1]
##    for i in range(n):
##        for b in range(n):
##            L.insert(i,b)
##
##
##def pengujian(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import nomor_delapan"
##    for i in jangkauan:
##        ##print('i = ',i)
##        t = timeit.timeit("nomor_delapan(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##
##n = 10
##LS = pengujian(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()


####==================== Nomor 9 ====================
##import timeit
##import time
##import matplotlib.pyplot as plt
##
##def carilurus(wadah, target):
##    n = len(wadah)
##    for i in range(n):
##        if wadah[i] == target:
##            return True
##    return False
##
##def tim():
##    z=100
##    a = [8, 7, 2, 1, 3, 2, 10]
##    awal = time.time()
##    U = carilurus(a, z)
##    akhir=time.time()
##    print("==================== worst case ====================")
##    print("mengurutkan %d bilangan, memerlukan %8.7f detik" %(U,akhir-awal))
##
##tim()
##
##def tim_matlib(n):
##    z = 100
##    a = [9, 6, 3, 2, 4, 1, 11]
##    U = carilurus(a, n)
##
##def pengujian(n):
##    ls = []
##    jangkauan = range(1, n+1)
##    siap = "from __main__ import tim_matlib"
##    for i in jangkauan:
##        t = timeit.timeit("tim_matlib(" + str(i) + ")", setup=siap, number=1)
##        ls.append(t)
##    return ls
##
##n = 10
##LS = pengujian(n)
##plt.plot(LS)
##skala = 7700000
##plt.plot([x*x/skala for x in range(1, n+1)])
##plt.show()
