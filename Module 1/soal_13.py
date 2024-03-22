def katakan(angka):
    di_bawah20 = ['Nol', 'Satu', 'Dua', 'Tiga', 'Empat', 'Lima', 'Enam', 'Tujuh', 'Delapan',
                      'Sembilan', 'Sepuluh', 'Sebelas', 'Dua belas', 'Tiga belas', 'Empat belas', 'Lima belas',
                      'Enam belas', 'Tujuh belas', 'Delapan belas', 'Sembilan belas']
    puluhan = ['Dua puluh', 'Tiga puluh', 'Empat puluh', 'Lima puluh', 'Enam puluh', 'Tujuh puluh',
               'Delapan puluh', 'Sembilan puluh']
    di_atas100 = {
        100 : 'ratus',
        1000 : 'ribu',
        1000000 : 'juta',
    }

    assert angka >= 0
    assert angka < 1000000000

    if angka < 20:
        return di_bawah20[angka]

    if angka < 100:
        return puluhan[(int)(angka/10)-2] + ('' if angka % 10==0 else ' ' + di_bawah20[angka % 10])

    pivot = max([key for key in di_atas100.keys() if key <= angka])

    #Recursion
    hasil = katakan((int)(angka/pivot)) + ' ' + di_atas100[pivot] + ('' if angka % pivot==0 else ' ' + katakan(angka % pivot))

    if 'Satu ratus' in hasil:
        hasil = hasil.replace('Satu ', 'Se')

    return hasil.capitalize()
print('Kurniawan Bagaskara')
print('L200214253')