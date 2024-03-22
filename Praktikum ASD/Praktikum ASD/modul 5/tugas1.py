#DoniWahyuSaputro
#L200200169

class MhsTIF(object):
    listKuliah = []
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

c0 = MhsTIF('Ika',153,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',120,'Sragen', 230000)
c2 = MhsTIF('Ali',22,'Surakarta', 250000)
c3 = MhsTIF('Caca',180,'Surakarta', 235000)
c4 = MhsTIF('Eka',47,'Boyolali', 240000)
c5 = MhsTIF('Kamidi',131,'Salatiga', 250000)
c6 = MhsTIF('Deni',132,'Klaten', 245000)
c7 = MhsTIF('Ngatiyem',50,'Wonogiri', 245000)
c8 = MhsTIF('Sumanto',23,'Klaten', 245000)
c9 = MhsTIF('Hamid',64,'Karanganyar', 270000)
c10 = MhsTIF('Yetno',70,'Purwodadi', 265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

#Nomor 1
def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def sortNIM(daftar):
    n = len(daftar)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftar[j].NIM > daftar[j+1].NIM:
                swap(daftar, j, j+1)

def checkNIM(a):
    n = len(a)
    for i in a :
        print('NIM : {} \nNama : {} \nKota Tinggal : {}\n'.format(i.NIM, i.nama, i.kotaTinggal))

