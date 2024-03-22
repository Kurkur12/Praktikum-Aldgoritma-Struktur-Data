##DoniWahyuSaputro
##L200200169
##UTS

class Orang():
    def __init__(self, nama, umur, kulit):
        self.nama = nama
        self.umur = umur
        self.kulit = kulit
    def __str__(self):
        return str(self.nama)+" "+str(self.umur)+" "+str(self.kulit)

data1 = Orang("Paijo\t",30,"\tSawo Matang")
data2 = Orang("Badang\t",33,"\tKuning Langsat")
data3 = Orang("Uus\t",35,"\tPutih")
data4 = Orang("Dzoky\t",18,"\tSawo Matang")
data5 = Orang("Akbar\t",27,"\tKuning Langsat")
data6 = Orang("Doni\t",23,"\tPutih")
data7 = Orang("Tatang\t",21,"\tKuning Langsat")
data8 = Orang("Painem\t",40,"\tSawo Matang")
data9 = Orang("Yetno\t",44,"\tKuning Langsat")
data10 = Orang("Jatmiko\t",32,"\tPutih")

data = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]

##for i in data:
##    print(i)
