from random import randint

quiz = randint(1, 100)

print('Saya menyimpan angka bulat antara 1 sampai 100. coba tebak')

jawab = 0
count = 1
while jawab != quiz:
    jawab = input('Masukkan tebakan ke-{}:>'.format(count))
    jawab = int(jawab)
    if jawab == quiz:
        print('Ya. Anda Benar')
    elif jawab < quiz:
        print('Itu terlalu kecil. Coba lagi')
    else:
        print('Itu terlalu besar. Coba lagi')
    count += 1
print('Kurniawan Bagaskara')
print('L200214253')
