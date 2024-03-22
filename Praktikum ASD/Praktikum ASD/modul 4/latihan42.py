from mhstif import*    
c0 = MhsTIF('Ika',10,'Sukoharjo', 240000)
c1 = MhsTIF('Budi',51,'Sragen', 230000)
c2 = MhsTIF('Ahmad',2,'Surakarta', 250000)
c3 = MhsTIF('Chandra',18,'Surakarta', 235000)
c4 = MhsTIF('Eka',4,'Boyolali', 240000)
c5 = MhsTIF('Fandi',31,'Salatiga', 250000)
c6 = MhsTIF('Deni',13,'Klaten', 245000)
c7 = MhsTIF('Galuh',5,'Wonogiri', 245000)
c8 = MhsTIF('Janto',23,'Klaten', 245000)
c9 = MhsTIF('Hasan',64,'Karanganyar', 270000)
c10 = MhsTIF('Khalid',29,'Purwodadi', 265000)
##
##Lalu kita membuat daftar mahasiswa dalam bentuk list seperti ini:
##
Daftar = [c0, c1, c2, c3, c4, c5, c5, c6, c7, c8, c9, c10]

target = 'Klaten'
for i in Daftar:
    if i.kota == target:
        print(i.nama + ' tinggal di ' + target)
