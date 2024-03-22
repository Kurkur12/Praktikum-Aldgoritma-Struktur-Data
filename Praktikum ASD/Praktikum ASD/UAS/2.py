class _SimpulPohonBiner(object):
    def __init__( self, data ):
        self.data = data
        self.kiri = None
        self.kanan = None

A = _SimpulPohonBiner('Doni')
B = _SimpulPohonBiner('Wahyu')
C = _SimpulPohonBiner('Saputro')

def preorderTrav( subpohon ):
    if subpohon is not None :
        print( subpohon.data )
        preorderTrav( subpohon.kiri )
        preorderTrav( subpohon.kanan )
