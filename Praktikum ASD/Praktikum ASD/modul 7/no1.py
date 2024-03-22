import re

a = open('Indonesia.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"menu\w+",baca)
print(cocok)
print("(Double Klik)")
print ("Kurniawan Bagaskara")
print ("L200214253")

