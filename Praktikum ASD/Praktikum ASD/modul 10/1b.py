from timeit import timeit
import random

print("====Jumlah Cara 2===")

def jumlahkan_cara_2(n):
    return (n*(n+1))/2

for i in range(5):
    siap = "from __main__ import jumlahkan_cara_2"
    h = jumlahkan_cara_2(1000000)
    t = timeit("jumlahkan_cara_2(1000000)", setup=siap, number=1)
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, t))
