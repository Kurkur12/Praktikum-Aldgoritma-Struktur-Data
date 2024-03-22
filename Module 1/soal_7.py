def faktorPrima(x):
    faktor=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            faktor.append(loop)
        else:
            loop+=1
    return faktor
print('Kurniawan Bagaskara')
print('L200214253')
