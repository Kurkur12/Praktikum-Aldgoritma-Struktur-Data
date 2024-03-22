import re

##a = open('menu.txt','r')
##baca = a.read()
##a.close
##cocok= re.findall(r"\sme\w+",baca)
##print(cocok)
##print("( Double Klik )")
a = open('menu.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"me\w+",baca)
print(cocok)
print(" ")
