from LatihanOOP4 import Manusia
class Mahasiswa(Manusia):
    listKuliah = []
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
    def ambilKuliah(self, choice):
        self.listKuliah.append(choice)
    def hapusKuliah(self, choice):
        if choice not in self.listKuliah:
            print('Tidak ada mata kuliah {} di khs anda'.format(choice))
        else:
            self.listKuliah.remove(choice)
print('Kurniawan Bagaskara')
print('L200214253')