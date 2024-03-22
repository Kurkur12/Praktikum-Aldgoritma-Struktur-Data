##DoniWahyuSaputro
##L200200169
##UTS

from no3 import*
def cetakKulit(data, warna):
    for i in data:
        if i.kulit == warna:
            print(i.nama, "warna kulit", i.kulit)
    return True

cetakKulit(data, "\tSawo Matang")
