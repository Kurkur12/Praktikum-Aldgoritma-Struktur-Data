#DoniWahyuSaputro
#L200200169

from soal2 import Mahasiswa

print('Program Input Data Mahasiswa')
nama = input('Masukkan Nama          : ')
nim = str(input('Masukkan NIM           : '))
kota = input('Masukkan Kota          : ')
uang = int(input('Masukkan Uang Saku     : '))

mhs = Mahasiswa(nama,nim,kota,uang)
print('\nAnda telah memasukkan data sebagai berikut : \n')
print(mhs)
