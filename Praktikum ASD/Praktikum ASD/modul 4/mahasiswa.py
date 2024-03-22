from manusia import Manusia

class Mahasiswa(Manusia):
    listKuliah = []
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uangSaku = us

    def __str__(self):
        return 'Nama : {} \nNIM : {} \nTinggal di : {} \nUang saku {} tiap bulannya'.format(self.nama, self.NIM, self.kota, str(self.uangSaku))

    def ambilNama(self):
        return self.nama

    def ambilNIM(self):
        return self.NIM

    def ambilUangSaku(self):
        return self.uangSaku

    def makan(self, s):
        print('Saya baru saja makan {} sambil belajar'.format(s))
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kota

    def perbaruiKotaTinggal(self, kota_baru):
        self.kota = kota_baru

    def tambahUangSaku(self, uang):
        self.uangSaku += uang

    def ambilKuliah(self, matkul):
        self.listKuliah.append(matkul)

    def hapusKuliah(self, matkul):
        if matkul not in self.listKuliah:
            print('Anda tidak mengambil mata kuliah tersebut')
        else:
            self.listKuliah.remove(matkul)
