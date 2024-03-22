#DoniWahyuSaputro
#L200200169

class Pesan(object):
    
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks),'karakter')
    def perbarui(self, sebuahString):
        self.teks = sebuahString
    def apakahTerkandung(self, word):
        if word in self.teks:
            print(True)
        else:
            print(False)
    def hitungKonsonan(self):
        count = 0
        konsonan = 'qwrtypsdfghjklzxcvbnm'
        word = str.lower(self.teks)
        for i in word:
            if i in konsonan:
                count +=1
        print(count)
    def hitungVokal(self):
        count = 0
        vokal = 'aiueo'
        word = str.lower(self.teks)
        for i in word:
            if i in vokal:
                count +=1
        print(count)
