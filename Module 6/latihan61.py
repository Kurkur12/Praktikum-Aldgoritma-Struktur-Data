def gabungkanDuaListUrut(A, B):
    la = len(A); lb = len(B)
    C = list()
    i = 0; j = 0

    #Gabungkan keduanya sampai salah satu kosong
    while i < la and j < lb:
        if A[i] <B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < la:       #Jika A mempunyai sisa
        C.append(A[i])  #   tumpukan ke list baru itu
        i += 1          #   satu demi satu

    while j <lb:        #Jika B mempunyai sisa
        C.append(B[j])  #   tumpukkan ke list baru itu
        j += 1          #   satu demi sati

    return C
        

P = [2,  8, 15, 23, 37]
Q = [4, 6, 15, 20]
R = gabungkanDuaListUrut(P, Q)
print(R)
