#DoniWahyuSaputro
#L200200169

string = ''
bar = 1

x = int(input('Masukkan  angka:'))

#Looping baris
while bar <= x:
    kol = bar

    #Looping kolom
    while kol > 0:
        string = string + '*'
        kol = kol - 1

    string = string + '\n'
    bar = bar + 1
print(string)
    
