def mergeSort(A):
    #print("Membelah", A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]
        
        mergeSort(separuhkiri)
        mergeSort(separuhkanan)
        
        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1
            
        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1
            
        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1         
    #print("Menggabungkan", A)
def quickSort(A):
    quickSortBantu (A, 0, len(A)-1)

def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah-1)
        quickSortBantu(A, titikBelah+1, akhir)

def partisi(A, awal, akhir):
    nilaipivot = A[awal]
    penandakiri = awal + 1
    penandakanan = akhir
    
    selesai = False
    while not selesai:
        
        while penandakiri <= penandakanan and A[penandakiri] <= nilaipivot:
            penandakiri = penandakiri + 1
            
        while penandakanan >= penandakiri and A[penandakanan] >= nilaipivot:
            penandakanan = penandakanan - 1
            
        if penandakanan < penandakiri:
            selesai = True
        else:
            temp = A[penandakiri]
            A[penandakiri] = A[penandakanan]
            A[penandakanan] = temp
            
    temp = A[awal]
    A[awal] = A[penandakanan]
    A[penandakanan] = temp
    
    return penandakanan
