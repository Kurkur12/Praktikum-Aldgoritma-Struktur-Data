#DoniWahyuSaputro
#L200200169

def selesaikanABC(a, b, c):
    a=float(a)
    b=float(b)
    c=float(c)
    D=(b**2) - (4*a*c)
    if D<0:
        return 'Determinanya negatif. Persamaan tidak mempunyai akar real'
    else:
        x1=(-b + sq(D))/2*a
        x2=(-b - sq(D))/2*a
        hasil=(x1, x2)
        return hasil
