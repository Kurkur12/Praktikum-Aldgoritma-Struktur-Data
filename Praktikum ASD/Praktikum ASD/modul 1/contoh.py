Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3
5
>>> 2+3*5-6/2
14.0
>>> # Menghitung dua pangkat seribu
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> radius = 4
>>> pi = 3.14159
>>> area = pi * radius * radius
>>> print(area)
50.26544
>>> x = 9
>>> print(x)
9
>>> x = 10
>>> print(x)
10
>>> a = 5
>>> b = 6.2
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> s = 'Apa"
SyntaxError: EOL while scanning string literal
>>> s = 'Apa'
>>> s
'Apa'
>>> type(s)
<class 'str'>
>>> a = 'Hai'
>>> b = 'mas'
>>> c = 'Data'
>>> d = a+b+c
>>> d
'HaimasData'
>>> g = '30'
>>> h = 23
>>> g + h
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    g + h
TypeError: can only concatenate str (not "int") to str
>>> int(g) + h
53
>>> f = 2.5
>>> g = 7
>>> d = [f, g, 3.9, 8, 'Apa kabar']
>>> d
[2.5, 7, 3.9, 8, 'Apa kabar']
>>> type(d)
<class 'list'>
>>> d[0] = 55
>>> d
[55, 7, 3.9, 8, 'Apa kabar']
>>> for i in d:
	print(i) ##disini penceet "Enter" dua kali

	
55
7
3.9
8
Apa kabar
>>> a = 'Wacana keilmuan dan keislaman'
>>> b = [43,44,45,46,47,48,49,50]
>>> a[0:6]
'Wacana'
>>> a[7:15]
'keilmuan'
>>> a[::-1]
'namalsiek nad naumliek anacaW'
>>> a[-7:-2]
'islam'
>>> a[-7:100]
'islaman'
>>> len(a)
29
>>> a[0:29]
'Wacana keilmuan dan keislaman'
>>> a[0:100]
'Wacana keilmuan dan keislaman'
>>> a[0:29:2]
'Wcn elundnkilmn'
>>> a[0:200:2]
'Wcn elundnkilmn'
>>> dd = {'nama':'joko', 'umur':21, 'asal':'surakarta'}
>>> dd['nama']
'joko'
>>> keranjang = {'apel', 'jeruk', 'apel', 'mangga', 'jeruk', 'pisang'}
>>> print(keranjang)
{'apel', 'mangga', 'jeruk', 'pisang'}
>>> 'jeruk' in keranjang
True
>>> 'rumput' in keranjang
False
>>> a = set('surakarta')
>>> b = set{'yogyakarta')
SyntaxError: invalid syntax
>>> b = set('yogyakarta')
>>> a
{'a', 'u', 'r', 'k', 's', 't'}
>>> b
{'o', 'g', 'a', 'y', 'r', 'k', 't'}
>>> a - b
{'u', 's'}
>>> 
>>> a|b
{'o', 'g', 'a', 'y', 'u', 'r', 'k', 's', 't'}
>>> a & b
{'k', 't', 'a', 'r'}
>>> a ^ b
{'o', 'g', 'y', 'u', 's'}
>>> p = 3
>>> q = 7
>>> p>q
False
>>> p<q
True
>>> p == q
False
>>> p != q
True
>>> 4<8
True
>>> 4 <=4
True
>>> 4<=5
True
>>> 4<=1
False
>>> 'UMS' > 'UGM'
True
>>> 'UMS' > 'ITB'
True
>>> 'Emas' < 'Sayur'
True
>>> 
============= RESTART: C:/Kuliah/SEMESTER 4/Praktikum ASD/modul 1/LatReview1.py ============
Nilai a = 4
Nilai b = 5
Sekarang, c = a + b= 4 + 5 = 9

Sudah selesai
>>> 