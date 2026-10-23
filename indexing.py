Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#indexing
a="vijayawada"
a[4]
'y'
a[0]
'v'
a[0],a[1]
('v', 'i')
a[0,4]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a[0,4]
TypeError: string indices must be integers, not 'tuple'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[5]+a[6]
'in'
a[2]+a[3]
'am'
a[0]
'i'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a=I am learning python full stack
SyntaxError: invalid syntax
a="I am learning python full stack"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[5]+a[6]+a[7]+a[8]+a[9}+a[10]+a[11]+a[12]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[5]+a[6]+a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'learning'
>>> a[2}+a[3]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[2]+a[3]
'am'
>>> a[21]+a[22]+a[23]+a[24]
'full'
>>> a[5]+a[6]+a[7]+a[8}+a[9]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
>>> b="Time is very precious"
>>> b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]
'precious'
>>> b[8]+b[9]+b[10]+b[11]
'very'
>>> b[0]+b[1]+b[2]+b[3]
'Time'
>>> #negitive indexing
>>> a="vijayawada is a royal city"
>>> a[-6]+aa[-7]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a[-6]+aa[-7]
NameError: name 'aa' is not defined. Did you mean: 'a'?
>>> a[-6]+a[-7]+a[-8]+a[-9]+a[-10]
'layor'
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'city'
>>> a[-15]+a[-14]
'is'
>>> b="vizag is a city of Destiny"
>>> b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'Destiny'
>>> b[-15]+b[-14]+b[-13]+b[-12]
'city'
>>> b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'vizag'
