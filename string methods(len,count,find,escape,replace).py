Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("a")
1
a.count(" ")
3
a.couunt("l")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.couunt("l")
AttributeError: 'str' object has no attribute 'couunt'. Did you mean: 'count'?
a.count(l)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.count(l)
NameError: name 'l' is not defined
a.count("l")
4
print(a.count("a"))
1
a="1234"
a.count("3")
1
a=1,2,3,4,5,6
a.count(3)
1
b=3,4,5,6,3,6,7
b.count(3)
2
#find a string
a="code"
a[2]
'd'
a.find["d"]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.find["d"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.find("d")
2
b="hello"
a.find("l")
-1
b.find("l")
2
b[2:4]
'll'
b["k"]
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b["k"]
TypeError: string indices must be integers, not 'str'
>>> b.find("k")
-1
>>> a="hello world"
>>> print("java")
java
>>> print(java)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(java)
NameError: name 'java' is not defined
>>> #escspe sequences
>>> #\n->new line
>>> #\t->tab space
>>> a="name\nmobile\tmailid\ncollege\tbranch"
>>> print(a)
name
mobile	mailid
college	branch
>>> a="name:bhavani\nmobileno:234517892782\tmailid:db93@gmail.com\ncollege:vitw\tbranch:DS"
>>> print(a)
name:bhavani
mobileno:234517892782	mailid:db93@gmail.com
college:vitw	branch:DS
>>> #replace
>>> a="wait until you succeed"
>>> a.replce("wait","work")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.replce("wait","work")
AttributeError: 'str' object has no attribute 'replce'. Did you mean: 'replace'?
>>> a.replace("wait","work")
'work until you succeed'
>>> a="python java"
>>> a.replace("java","DSA")
'python DSA'
>>> a.replace("h","a")
'pytaon java'
>>> a="hi"
>>> a.replace("h","a")
'ai'
