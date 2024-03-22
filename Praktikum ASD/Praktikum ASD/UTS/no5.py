##DoniWahyuSaputro
##L200200169
##UTS

from no3 import*
def urutkanUmur(data):
    for tujuan in range(len(data)-1,0,-1):
        maks = 0
        for x in range(1,tujuan+1):
            maks_sem = data[maks].umur
            if maks_sem < data[x].umur:
                maks = x
            data[maks],data[tujuan] = data[tujuan],data[maks]
    return data

print("--------Sebelum----------")
for i in data:
    print(i.umur, i.nama)
urutkanUmur(data)
print("--------Sesudah----------")
for i in data:
    print(i.umur, i.nama)
