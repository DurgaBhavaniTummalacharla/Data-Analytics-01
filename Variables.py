Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#variables
a=2
print(a)
2
b=5
print(b)
5
x=90
print(x)
90
print(X)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
z=50
print(z)
50
print(Z)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(Z)
NameError: name 'Z' is not defined. Did you mean: 'z'?
9=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a90=20
print(a9)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(a9)
NameError: name 'a9' is not defined. Did you mean: 'a'?
print(a90)
20

9a=9
SyntaxError: invalid decimal literal
a0123456789
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a0123456789
NameError: name 'a0123456789' is not defined
a0123456789=100
print(a0123456789)
100
name="bhavani"
print(name)
bhavani
city="ijayawada"
print(city)
ijayawada
country="india"
print(country)
india
@=8
SyntaxError: invalid syntax
$=10
SyntaxError: invalid syntax
_=40
print(_)
40
_a=30
print(_a)
30
if=30
SyntaxError: invalid syntax
else=90
SyntaxError: invalid syntax
int=80
print(int)
80
a=5,b=10
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;b=10
print(a+b)
15
a=3 b=6
SyntaxError: invalid syntax
a=3
b=6
print(a+b)
9
a,b=3,4
print(a+b)
7
a=2,3,4,5,6,7,8
print(a)
(2, 3, 4, 5, 6, 7, 8)
a,b,c=3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a,b,c=3,4,5,6,7,8
ValueError: too many values to unpack (expected 3)
a,b,c=3,4,56,7,8,8
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a,b,c=3,4,56,7,8,8
ValueError: too many values to unpack (expected 3)
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
a,b,c=4,6,9
print(a,b,c)
4 6 9
first name="bhavani"
SyntaxError: invalid syntax
first_name="bhavani"
print("first_name)
      
SyntaxError: unterminated string literal (detected at line 1)
print(first_name)
      
bhavani
 fname="Durga"
      
SyntaxError: unexpected indent
fname="durga"
      
lname="bhavani"
      
print(fname+lname)
      
durgabhavani
print(fname+" "+lname)
...       
durga bhavani
>>> print(fname,lname)
...       
durga bhavani
>>> NAME="chinnari"
...       
>>> print("NAME")
...       
NAME
>>> print(NAME)
...       
chinnari
>>> name="chinnu"
...       
>>> print(name)
...       
chinnu
>>> a,b,c=100
...       
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a,b,c=100
TypeError: cannot unpack non-iterable int object
>>> a=b=c=100
...       
>>> print(a,b,c)
...       
100 100 100
>>> a=10
...       
>>> print(a)
...       
10
>>> del a
...       
>>> print(a)
...       
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: '_a'?
