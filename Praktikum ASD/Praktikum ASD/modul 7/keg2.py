import re
cocok = re.findall(r'eee', 'teeeh')
cocok = re.findall(r'ehs', 'teeeh')

cocok = re.findall(r'..h', 'teeeh')


cocok = re.findall(r'\d\d\d', 't123h di 2019 bulan 02')
cocok = re.findall(r'\w\w\w', '@@a*bc#def*tghh!!')

if cocok:
    print('menemukan', cocok)
else:
    print('tidak menemukan')
