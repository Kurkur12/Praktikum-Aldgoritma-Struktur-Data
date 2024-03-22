import timeit
import matplotlib.pyplot as plt

def nomor_tujuh(n):
    L = list(range(30))
    L = L[::-1]
    for i in range(n):
        L.append(n)
            

def pengujian(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import nomor_tujuh"
    for i in jangkauan:
        ##print('i = ',i)
        t = timeit.timeit("nomor_tujuh(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls


n = 10
LS = pengujian(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
