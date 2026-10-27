Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#upper
a="code"

a.upper()
'CODE'
b="python"
b.upper()
'PYTHON'
#lower()
c="HELLO"
c.lower()
'hello'
d="HI"
d.lower()
'hi'
a="python"
a.upper("p")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.upper("p")
TypeError: str.upper() takes no arguments (1 given)
a[0].upper()
'P'
#capitalize
a.capitalize
<built-in method capitalize of str object at 0x0000027D6D6D1070>
a.capitalize()
'Python'
b="python course"
b.title()
'Python Course'
c="i am in class"
c.title()
'I Am In Class'
c.capitalize()
'I am in class'
a="hello"
a.isalpha()
True
b="hello world"
b.isalpha()
False
c="helloworld"

c.isalpha()
True
a.isdigit()
False
a=12345
a.isdigit()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a="12345"
a.isdigit()
True
a="python course"
a.startswith("p")
True
a.endswith("e")
True
b="python COURSE"
b.isupper()
False
c="bhavani123"
c.isalnum()
True
#strip()
#rstrip,lstrip()
a="               bhavani          "
a.strip()
'bhavani'
a.rstrip()
'               bhavani'
a.lstrip()
'bhavani          '
#split
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']
c[1].upper()
'H'
c=b.split()
c[1].upper()
'AM'
'AM'
'AM'
#join
a="apples","banana","grapes"
"".join(a)
'applesbananagrapes'
" ".join(a)
'apples banana grapes'
"k".join(a)
'appleskbananakgrapes'
b="hello"
"k".join(b)
'hkeklklko'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a+" "+b)
python course
fname="pooja"
lname="t"
print(fname+lname)
poojat
print(fname+" "+lname)
pooja t
print(fname.title()+" "+lnmae.title())
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print(fname.title()+" "+lnmae.title())
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
print(fname.title()+" "+lname.title())
Pooja T
print((fname+" "+lname).title())
Pooja T
#formatting
a=5
b=7
>>> print(a+b)
12
>>> print("the sum is",a+b)
the sum is 12
>>> print("the sum is a+b")
the sum is a+b
>>> city="vijayawda"
>>> print("city is",vijayawada)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print("city is",vijayawada)
NameError: name 'vijayawada' is not defined
>>> print("city is",city)
city is vijayawda
>>> #format
>>> a="motu"
>>> b="patlu"
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> #fstring
>>> a="sweety"
>>> b="cuty"
>>> print(f"hello to {a}{b}")
hello to sweetycuty
>>> print(f"hello {a} [b}")
SyntaxError: f-string: single '}' is not allowed
>>> print(f"hello {a} hello {b}")
hello sweety hello cuty
>>> a=4
>>> b=5
>>> print(a+b)
9
>>> print("the product is",a*b)
the product is 20
>>> print("the {}{}".format(a,b))
the 45
>>> print(f"product {a} {b}")
product 4 5
