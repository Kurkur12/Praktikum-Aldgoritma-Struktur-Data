import re
string = 'Doni Wahyu Saputro, doniwahyu56@gmail.com'
nama = re.findall(r'[\w\.-]+@[\w\.-]+', string)
for email in nama:
    print(email)
