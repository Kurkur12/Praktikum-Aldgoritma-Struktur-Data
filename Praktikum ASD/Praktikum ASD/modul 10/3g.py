import time
import random
import timeit
import matplotlib.pyplot as plt

def a(n):
    for i in range(n):
        if i % 3 == 0:
            for j in range(n // 2):
                j+=j
        elif i % 2 == 0:
            for j in range(5):
                j+=j
        else:
            for j in range(n):
                j+=j

def ujia(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import a'
    for i in jangkauan:
        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
        ls.append(t)
    return ls

n = 100
LS = ujia(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()
