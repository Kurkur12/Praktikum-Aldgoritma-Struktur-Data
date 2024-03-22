from LatihanOOP4 import Manusia

class SiswaSMA(Manusia):
    def __init__(self, nama, kota, jurusan):
        Manusia.__init__(self, nama)
        self.kota = kota
        self.jurusan = jurusan
    def __str__(self):
        point = 'Nama : {}, Tempat tinggal di {}. Masuk Jurusan {}'.format(self.nama, self.kota, self.jurusan)
        return point
    def showNama(self):
        return self.nama
    def showKota(self):
        return self.kota
    def showJurusan(self):
        return self.jurusan
    def makanSiang(self, eating):
        print('Siang ini {} sedang kelaparan lalu dia makan {}'.format(self.nama, eating))
        self.keadaan = 'kenyang'
    def jamPelajaran(self, study):
        print('Saat ini {} sedang belajar {}'.format(self.nama, study))
        self.keadaan = 'lapar'
print('Kurniawan Bagaskara')
print('L200214253')