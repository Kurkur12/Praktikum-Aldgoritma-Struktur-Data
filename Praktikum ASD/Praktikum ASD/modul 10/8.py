import timeit
import matplotlib.pyplot as plt

def nomor_delapan(n):
    L = list(range(30))
    L = L[::-1]
    for i in range(n):
        for b in range(n):
            L.insert(i,b)


def pengujian(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = "from __main__ import nomor_delapan"
    for i in jangkauan:
        ##print('i = ',i)
        t = timeit.timeit("nomor_delapan(" + str(i) + ")", setup=siap, number=1)
        ls.append(t)
    return ls


n = 10
LS = pengujian(n)
plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
