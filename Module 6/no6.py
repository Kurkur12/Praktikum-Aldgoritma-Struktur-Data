from mahasiswa import *

def cetak(A):
    for i in A:
        print(i)

def quickSort(arr):
    kurang = []
    pivotList = []
    lebih = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i.ambilUangSaku() < pivot.ambilUangSaku():
                kurang.append(i)
            elif i.ambilUangSaku() > pivot.ambilUangSaku():
                lebih.append(i)
            else:
                pivotList.append(i)
        kurang = quickSort(kurang)
        lebih = quickSort(lebih)
        return kurang + pivotList + lebih

print("Sebelum diurutkan")
cetak(Daftar)
quickSort(Daftar)
print("\nSetelah diurutkan")
cetak(Daftar)

print("Kurniawan Bagaskara")
print("L200214253")
