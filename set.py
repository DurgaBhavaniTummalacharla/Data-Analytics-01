Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#sets
#add()
a={4,5,6,7,8,9}
a.add(10)
a
{4, 5, 6, 7, 8, 9, 10}
#issubset()
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False
#issuperset
a={2,3,4,5,6,7,8,9}
b={6,7,8,9}
a.issuperset(b)
True
b.issuperset(a)
False
#union()
a={5,6,7,8,9,10}
b={6,7,8,9,10,11,12}
a.union(b)
{5, 6, 7, 8, 9, 10, 11, 12}
#intersection
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.intersection(b)
{8, 9, 7}
#update()
a={4,5,6,7,8,9}
b={7,8,9,10,11,12}
a.update(b)
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
a
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{7, 8, 9, 10, 11, 12}
b.update(a)
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
b
{4, 5, 6, 7, 8, 9, 10, 11, 12}
#diffrence()
a={3,4,5,6,7,8}
b={8,9,10,11,12}
a.difference(b)
{3, 4, 5, 6, 7}
b.difference(a)
{9, 10, 11, 12}
#symmetric()
a={10,11,12,13,14,15}
b={13,14,15,16,17,18}
a.symmetric_difference(b)
{10, 11, 12, 16, 17, 18}
b.symmetric_diffrence(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    b.symmetric_diffrence(a)
AttributeError: 'set' object has no attribute 'symmetric_diffrence'. Did you mean: 'symmetric_difference'?
b.symmetric_diffrence(a)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    b.symmetric_diffrence(a)
AttributeError: 'set' object has no attribute 'symmetric_diffrence'. Did you mean: 'symmetric_difference'?
b.symmetric_difference(a)
{10, 11, 12, 16, 17, 18}
a={8,9,10,11,12}
b={11,12,13,14,15}
a.intersection_update()
a
{8, 9, 10, 11, 12}
a.intersection_update(b)
a
{11, 12}
a
{11, 12}
b.intersection_update(a)
b
{11, 12}
b
{11, 12}
#difference_update()
a={10,20,30,40,50}
b={30,40,50,60,70}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)
b
{50, 70, 40, 60, 30}
#symmeteric_difference_update()
a={3,4,5,6,7,8,9}
b={1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}
#pop
a={7,8,9,10,11,12}
a.pop()
7
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a
{8, 9, 10, 11, 12}
a.remove(10)
a
{8, 9, 11, 12}
a.discard(11)
a
{8, 9, 12}
#copy()
a={10,20,30,40,50}
a.copy()
{50, 20, 40, 10, 30}
b=a.copy()
b
{50, 20, 40, 10, 30}
a.clear()
a
set()
b=set()
b.add(30)
b
{30}
#index()
a.{5,6,7,8,9,10
   
SyntaxError: invalid syntax
}a={5,6,7,8,9,10}
SyntaxError: unmatched '}'
>>> a={5,6,7,8,9,10}
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
>>> len(a)
6
>>> a.count(10)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.count(10)
AttributeError: 'set' object has no attribute 'count'
>>> a={2,3,True,False,"bhavani",4.5}
>>> type(a)
<class 'set'>
>>> #isdisjoint
>>> a={4,5,6,7,8}
>>> b={9,10,11,12}
>>> a.isdisjoint(b)
True
>>> a={3,4,5,6,7}
>>> b={9,10,11,12}
>>> a.isdisjoint(b)
True
>>> a={3,4,5,6,7}
>>> b={7,8,9,10}
>>> a.isdisjoint(b)
False
>>> a={3,6.7,"python",3,6.7,(4+7j)
... print(a)
...    
SyntaxError: '{' was never closed
>>> a={3,6.7,"python",3,6.7,(4+7j))
...    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> a={3,6.7,"python",3,6.7,(4+7j)}
...    
>>> print(a)
...    
{(4+7j), 3, 6.7, 'python'}
