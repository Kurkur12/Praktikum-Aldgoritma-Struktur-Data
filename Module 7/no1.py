import re

a = open('Indonesia.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"menu\w+",baca)
print(cocok)
print("(Double klik)")
print ("Kurniawan Bagaskara")
print ("L200214253")

