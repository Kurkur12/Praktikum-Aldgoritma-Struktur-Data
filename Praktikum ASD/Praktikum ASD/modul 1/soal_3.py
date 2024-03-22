#DoniWahyuSaputro
#L200200169
def jumlahHurufVokal(kata):
    vokal = ['a', 'i', 'u', 'e', 'o']
    kata2 = kata.lower()
    list_kata = []
    list_kata.append(len(kata2))
    count = 0
    for i in kata2:
        if i in vokal:
            count += 1
    list_kata.append(count)
    return list_kata

def jumlahHurufKonsonan(kata):
    konsonan = ['b', 'c', 'd', 'f', 'g', 'h','j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    kata2 = kata.lower()
    list_kata = []
    list_kata.append(len(kata2))
    count = 0
    for i in kata2:
        if i in konsonan:
            count += 1
        list_kata.append(count)
        return list_kata

print(jumlahHurufVokal('Surakarta'))
print(jumlahHurufKonsonan('Surakarta'))
