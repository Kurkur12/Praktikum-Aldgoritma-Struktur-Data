A = [[1,2],[3,4],[5,6]]
B = [[7,8],[9,10]]
C = [[3,6],[5,2]]

#Nomor 1A
class matriks (object):
    def cetakmatriks(self, matriks):
        for i in matriks:
            print(i)
    def cekkonsisten(self, matriks):
        if len(matriks[0]) == len(matriks):
            print ("matriks konsisten")
        else:
            print ("matriks tidak konsisten")

x = matriks()
x.cetakmatriks(A)
print(x.cekkonsisten(A))

y = matriks()
y.cetakmatriks(B)
print(y.cekkonsisten(B))

#Nomor 1B
def ordo(matriks):
    return ("Ordo matriks = "+str(len(matriks))+" x "+str(len(matriks[0])))

#Nomor 1C
def jumlah(matriks1, matriks2):
    if ordo(matriks1) == ordo(matriks2):
        for x in range(0, len(matriks1)):
            for y in range(0, len(matriks1[0])):
                print (matriks1[x][y] + matriks2[x][y],' '),
            print()
    else:
        print("Matriks tidak sesuai")

#Nomor 1D
def kali(m,n):
    a = 0
    x,y = 0,0
    for i in range(len(m)):
        x += 1
        y = len(m[i])
    v,w = 0,0
    for i in range(len(n)):
        v += 1
        w = len(n[i])

    if (y == v):
        print ("Bisa Dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(m)):
            for j in range(len(n[0])):
                for k in range(len(n)):
                    vwxy[i][j] += m[i][k] * n[k][j]
        print (vwxy)
    else:
        print("Tidak memenuhi syarat")

kali(A,B)
kali(B,C)

#Nomor 1E
def determinan(p, total = 0):
    x = len(p[0])
    z = 0
    for i in range(len(p)):
        if (len(p[i]) == x):
            z += 1
    if (z == len(p)):
        if (x == len(p)):
            indices = list(range(len(p)))
            if len(p) == 2 and len(p[0]) == 2:
                val = p[0][0] * p[1][1] - p[1][0] * p[0][1]
                return val
            for fc in indices:
                pq = p
                pq = pq[1:]
                height = len(pq)
                for i in range(height):
                    pq[i] = pq[i][0:fc] + pq[i][fc+1:]
                sign = (-1) ** (fc % 2)
                sub_det = determinanHitung(pq)
                total += sign * A[0][fc] * sub_det
        else:
            return "Tidak bisa dihitung, bukan matriks bujur sangkar"
    else:
        return "Tidak bisa dihitung, bukan matriks bujur sangkar"
    return total
print('Kurniawan Bagaskara')
print('L200214253')