#DoniWahyuSaputro
#L200200169

def formatRupiah(n):
    x = '{:,}'.format(n).replace(',', '.')
    return 'Rp ' + x
