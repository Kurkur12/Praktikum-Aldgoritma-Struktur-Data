import re

a = open('KEI.html','r',encoding='latin1')
teks = a.read()
a.close()
pola4= r'(w+)</a></td>'
num4 = re.findall(pola4,teks)
print(num4)
