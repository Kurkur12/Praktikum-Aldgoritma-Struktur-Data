import time
import random
import timeit
import matplotlib.pyplot as plt

def a(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2

def ujia(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import a'
    for i in jangkauan:
        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
        ls.append(t)
    return ls

n = 10
LS = ujia(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
