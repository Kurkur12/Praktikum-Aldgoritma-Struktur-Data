class Manusia(object):
    """Class ' Manusia ' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


p1 = Manusia('Kurniawan Bagaskara')
p1.ucapkanSalam()

print('Kurniawan Bagaskara')
print('L200214253')