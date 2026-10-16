Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#int
int(2)
2
int(6.8)
6
int("bhavani")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("bhavani")
ValueError: invalid literal for int() with base 10: 'bhavani'
int(3+5j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(3+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(3)
3.0
float(4.5)
4.5
float("chinni")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("chinni")
ValueError: could not convert string to float: 'chinni'
float(3+7j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(3+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
str(2)
'2'
str(4.6)
'4.6'
str("python")
'python'
str(True)
'True'
>>> ste(False)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ste(False)
NameError: name 'ste' is not defined. Did you mean: 'str'?
>>> str(False)
'False'
>>> bool(1)
True
>>> bool(8.2)
True
>>> bool("welcome")
True
>>> bool(True)
True
>>> bool(Flase)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    bool(Flase)
NameError: name 'Flase' is not defined. Did you mean: 'False'?
>>> bool(False)
False
>>> str(4+9j)
'(4+9j)'
>>> bool(7+3j)
True
>>> complex(1)
(1+0j)
>>> complex(2.4)
(2.4+0j)
>>> complex("bhavani")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex("bhavani")
ValueError: complex() arg is a malformed string
>>> complex(3+4j)
(3+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
