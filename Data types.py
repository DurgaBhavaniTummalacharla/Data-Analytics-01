Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
b=5.7
type(b)
<class 'float'>
c="python"
type(c)
<class 'str'>
d="bhavani"
tyoe(d)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tyoe(d)
NameError: name 'tyoe' is not defined. Did you mean: 'type'?
type(d)
<class 'str'>
e='''course'''
>>> print(e)
course
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=2+9j
>>> type(g)
<class 'complex'>
>>> x=2j
>>> type(x)
<class 'complex'>
>>> y=4 j=7
SyntaxError: invalid syntax
>>> y=4j+7
>>> type(y)
<class 'complex'>
>>> a=2+8i
SyntaxError: invalid decimal literal
>>> b=j
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> c=True
>>> type(c)
<class 'bool'>
>>> v=False
>>> type(v)
<class 'bool'>
>>> b=yes
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b=yes
NameError: name 'yes' is not defined
>>> b=Yes
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b=Yes
NameError: name 'Yes' is not defined
