class _SimpulPohonBiner(object):
    def __init__( self, data ):
        self.data = data
        self.kiri = None
        self.kanan = None
            
#Membuat simpul-simpul dan mengisi data
A = _SimpulPohonBiner(1)
B = _SimpulPohonBiner(2)
C = _SimpulPohonBiner(3)
D = _SimpulPohonBiner(4)
E = _SimpulPohonBiner(5)
F = _SimpulPohonBiner(6)
G = _SimpulPohonBiner(7)
H = _SimpulPohonBiner(8)
I = _SimpulPohonBiner(9)
J = _SimpulPohonBiner(10)

#Menghubungkan simpul ortu-anak
A.kiri = B; A.kanan = D
D.kiri = C; D.kanan = E
E.kanan = H
H.kiri = F; H.kanan = J

#Kiri,Tengah,Kanan
def inorderTrav( subpohon ):
    if subpohon is not None:
        inorderTrav( subpohon.kiri )
        print( subpohon.data )
        inorderTrav( subpohon.kanan )

#preorder traversal
#Kiri,Kanan,Tengah
def postorderTrav( subpohon ):
    if subpohon is not None :
        postorderTrav( subpohon.kiri )
        postorderTrav( subpohon.kanan )
        print( subpohon.data )

        
#Tengah,Kiri,kanan
def preorderTrav( subpohon ):
    if subpohon is not None :
        print( subpohon.data )
        preorderTrav( subpohon.kiri )
        preorderTrav( subpohon.kanan )
