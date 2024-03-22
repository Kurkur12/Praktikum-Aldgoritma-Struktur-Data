from LatOOP3 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi diclass Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM)\
            + '. Tinggal di ' + self.kotaTinggal\
            + '. Uang Saku Rp ' + str(self.uangSaku)\
            + '. tiap bulan.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalai makan sambil belajar."""
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'
