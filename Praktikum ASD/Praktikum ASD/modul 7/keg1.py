import re

s = 'sebuah contoh kata:ashiap'
cocok = re.findall(r'kata:\w{5}', s)

if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')
