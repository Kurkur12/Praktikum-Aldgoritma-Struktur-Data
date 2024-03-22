#DoniWahyuSaputro
#L200200169

def is_prima(x):
    for i in range(2, x):
        if x % i == 0:
            return False
        
    return True

def bilangan_prima (awal, akhir):
    list_bilangan_prima = []
    
    for x in range(awal, akhir + 1):
        if is_prima(x):
            list_bilangan_prima.append(x)
          
    return list_bilangan_prima

print(bilangan_prima(2, 1000))
