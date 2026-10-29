Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #tuple
>>> a=[6,8.9,"python",2+9j,True,False)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> a=[6,8.9,"python",2+9j,True,False]
>>> print(a)
[6, 8.9, 'python', (2+9j), True, False]
>>> tpe(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tpe(a)
NameError: name 'tpe' is not defined. Did you mean: 'type'?
>>> type(a)
<class 'list'>
>>> a.index(2+9j)
3
>>> len(a)
6
