#DoniWahyuSaputro
#L200200169
import statistics

def rerata(x):
    hasil = float(sum(x)) / max(len(x), 1)
    return hasil

def hitungVariance(x):
    hasil = statistics.variance(x)
    return hasil

def hitungStDev(x):
    hasil = statistics.stdev(x)
    return hasil

print(rerata([1,2,3,4,5]))
g = [3,4,5,4,3,4,5,2,2,10,11,23]
print(rerata(g))
print(hitungVariance(g))
print(hitungStDev(g))
