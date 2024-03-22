import re

a = open('Indonesia.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"di\w+",baca)
print(cocok)
print(" ")
print ("Kurniawan Bagaskara")
print ("L200214253")
