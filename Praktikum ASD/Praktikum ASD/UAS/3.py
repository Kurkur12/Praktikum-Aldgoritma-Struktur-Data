import timeit

def kalangBersusuh(n):
    for i in range(n):
        for j in range(n):

            i+j

def ujiKalangBersusuh(n):
    ls=[]
    jangkauan = range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        print('i=',i)
        t=timeit.timeit("kalangBersusuh("+str(i)+")", setup=siap, number=10)
        ls.append(t)
    return ls

n = 1500000
LS = ujiKalangBersusuh(n)

