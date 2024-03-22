#DoniWahyuSaputro
#L200200169
#UTS

def LuasPersegi():
    print("Program menghitung luas Persegi")
    sisi = int(input("Masukkan sisi = >? "))
    luas = sisi**2
    return "Luas persegi = sisi x sisi. Maka Luasnya = "+str(luas)+" satuan luas"
def LuasLingkaran():
    from math import pi
    print("Program menghitung luas Lingakaran")
    r = int(input("Masukkan jari-jari = >? "))
    luas = (pi*r*r)
    return "Luas Lingkaran = phi x r x r. Maka Luasnya = "+'{:.2f}'.format(luas)+" satuan luas"
def LuasSegitigaSamaSisi():
    print("Program menghitung luas Segitiga Sama Sisi")
    sisi = int(input("Masukkan sisi = >? "))
    luas = (sisi**2)/2
    return "Luas Segitiga = 1/2 x sisi x sisi. Maka Luasnya = "+str(luas)+" satuan luas"
def LuasBelahKetupat():    
    print("Program menghitung luas Belah Ketupat")
    d1 = int(input("Masukkan d1 = >? "))
    d2 = int(input("Masukkan d2 = >? "))
    luas = (d1*d2)/2
    return "Luas Belah Ketupat = 1/2 x d1 x d2. Maka Luasnya = "+str(luas)+" satuan luas"

