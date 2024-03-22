##DoniWahyuSaputro
##L200200169
##UTS

##2ab
matrik1 = [2,3]
matrik2 = [[3,4,5],[2,3,4]]
def kalikanMatrik(matrik1, matrik2):
    hasil = []
    jumlah = 0
    for indek in range(len(matrik2[0])):
        for i in range(len(matrik1)):
            jumlah += matrik1[i]*matrik2[i][indek]
        hasil.append(jumlah)
        jumlah = 0
    return hasil
print("2ab")
print(matrik1, "1x2")
print(matrik2, "2x3")
print("Kalikan")
print(kalikanMatrik(matrik1, matrik2), "1x3")
print("----------------------")
##2c
def buatIdentitas7():
    matrik = [[1 if y==x else 0 for y in range(7)] for x in range(7)]
    return matrik
print("2c")
print("Buat Matrik identitas 7x7")
print(buatIdentitas7())
