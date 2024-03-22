class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSaku)\
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku       
a0 = MhsTIF('Bintang', 193, 'Sragen', 240000)
a1 = MhsTIF('Agus', 195, 'Pati', 230000)
a2 = MhsTIF('Dino', 204, 'Solo', 250000)
a3 = MhsTIF('Leni', 210, 'Solo', 235000)
a4 = MhsTIF('Andi', 194, 'Semarang', 240000)
a5 = MhsTIF('Finza', 187, 'Tangerang', 250000)
a6 = MhsTIF('Bayu', 211, 'Sukoharjo', 245000)
a7 = MhsTIF('Ulin', 190, 'Salatiga', 245000)
a8 = MhsTIF('Bimo', 173, 'Boyolali', 245000)
a9 = MhsTIF('Riska', 192, 'Ngawi', 270000)
a10 = MhsTIF('Fauzan', 179, 'Kalimantan', 230000)
a11 = MhsTIF('Sendi', 188, 'Surabaya', 300000)
a0.next = a1
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
a7.next = a8
a8.next = a9
a9.next = a10
a10.next = a11
Daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]
