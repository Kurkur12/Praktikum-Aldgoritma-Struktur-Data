import re

a = open('Indonesia.txt', 'r')
baca = a.read()
a.close()
cocok = re.findall(r"\sdi\w+",baca)
print(cocok)
print("Double Klik")
