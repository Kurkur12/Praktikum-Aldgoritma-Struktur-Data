A = [2,9,78,65,5,70]
B = [1,4,12,43,22,11,120]

def sortToC(a, b):
    c = a+b
    for i in range(1, len(c)):
        nilai = c[i]
        pos = i
        while pos > 0 and nilai < c[pos - 1]:
            c[pos] = c[pos-1]
            pos -=1
        c[pos] = nilai
    return c
print ('Kurniawan Bagaskara')
print ('L200214253')

