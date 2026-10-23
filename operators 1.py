Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a>b or b>a
True
a<=b or b>=a
True
not true
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#identify operator
a=3
type(a) is not int
False
type(a) is int
True
a="python"
type(a) is str
True
b=6+7j
type(b) is cpmplex
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    type(b) is cpmplex
NameError: name 'cpmplex' is not defined. Did you mean: 'complex'?
NameError: name 'cpmplex' is not defined. Did you mean: 'complex'?
SyntaxError: invalid syntax
type(b) is complex
True
#membership operators
a=2,3,4,5,6,7,8,9
9 in a
True
10 in a
False
10 not in a
True
>>> #bitwise operator
>>> a=4
>>> b=8
>>> a|b
12
>>> a=3
>>> b=8
>>> a|b
11
>>> a=5
>>> ~a
-6
>>> b=-4
>>> ~b
3
>>> -(b+1)
3
>>> -(a+1)
-6
>>> a=4
>>> b=9
>>> a^b
13
>>> a=5
>>> b=10
>>> a^b
15
>>> a=3
>>> a<<2
12
>>> a=6
>>> a<<2
24
>>> a=6
>>> a<<2
24
>>> a>>3
0
>>> a=8
>>> a>>2
2
