Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list
a=[2,4.5,"python",8+9j,True,False)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a=[2,4.5,"python",8+9j,True,False]
print(a)
[2, 4.5, 'python', (8+9j), True, False]
type(a)
<class 'list'>
b=4.6
4
4
type(b)
<class 'float'>
type(c)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
c-[4.6]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c-[4.6]
NameError: name 'c' is not defined
c=[4.6]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("ai")
a
['python', 'java', 'c', 'c++', 'ai']
a.append
<built-in method append of list object at 0x000001276E4EC580>
(
a.append("ml","dsa")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.append("ml","dsa")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","dsa"])
a
['python', 'java', 'c', 'c++', 'ai', ['ml', 'dsa']]
#extend
a=["dsa","ai","ml"]
a.extend(["python","java"])
a
['dsa', 'ai', 'ml', 'python', 'java']
#insert()
b=["black","white"]
b.insert(1,"red")
b
['black', 'red', 'white']
a=["apple","mango","kiwi"]
a.index("mango")
1
a.copy()
['apple', 'mango', 'kiwi']
b=a.copy()
b
['apple', 'mango', 'kiwi']
#pop()
a=["vja","vzg","hyd"]
a.pop()
'hyd'
a
['vja', 'vzg']
>>> a.pop(1)
'vzg'
>>> a
['vja']
>>> a.pop["vja")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> a.pop("vja")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.pop("vja")
TypeError: 'str' object cannot be interpreted as an integer
>>> a
['vja']
>>> a.pop(0)
'vja'
>>> #remove()
>>> a=["hi","hello","how"]
>>> a.remove("how")
>>> a
['hi', 'hello']
>>> a.remove(1)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list
>>> #clear()
>>> a=["java","ai","ml"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("pooja")
>>> b
['pooja']
>>> #sort()
>>> a=["banana","grapes","apples","mango","kiwi"]
>>> a.sort()
>>> a
['apples', 'banana', 'grapes', 'kiwi', 'mango']
>>> b=[7,0,2,5,10,8,1]
>>> b.sort()
>>> b
[0, 1, 2, 5, 7, 8, 10]
c=[5+9j,2+4j,6+9j]
c.sort()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
d=[6,8,9,"pooja","hello",6+9j]
d.sort()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
c=[4.5,8.9,2.4]
c.sort()
c
[2.4, 4.5, 8.9]
d=[True,False,True]
d.sort()
d
[False, True, True]
#reverse()
a=["black","red","white"]
a.reverse()
a
['white', 'red', 'black']
b=[5,8,0,1,6,9]
b.reverse()
b
[9, 6, 1, 0, 8, 5]
#length()
a=["java","ai","ml"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
len(a)
3
a=["java","ai","ml"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
len(a)
3
a=["java","ai","ml"]
len(a)
3
b="java"
len(b)
4
c=["java"]
len(c)
1
a.count("ai")
1
a.count("a")
0
b=["java","ai","a","ml"]
b.count("a")
1
