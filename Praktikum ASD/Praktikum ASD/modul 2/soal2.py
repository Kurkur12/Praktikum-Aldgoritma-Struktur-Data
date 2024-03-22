#DoniWahyuSaputro
#L200200169

from LatOOP4 import Manusia
class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM '+ str(self.NIM) \
            + '. Tinggal di '+ self.kotaTinggal \
            + '. Uang saku Rp '+ str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar")
        self.keadaan = 'kenyang'
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, changeword):
        self.kotaTinggal = changeword
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self, upmoney):
        self.uangSaku = self.uangSaku + upmoney
