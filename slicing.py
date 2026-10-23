Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="work until you succeed"
>>> a[15:22]
'succeed'
>>> a[5:10]
'until'
>>> a[0:4]
'work'
>>> a[5:10]
'until'
>>> b="simple is better than complex"
>>> b[11:17]
'etter '
>>> b[10:15]
'bette'
>>> b[10:16]
'better'
>>> b[0:6]
'simple'
>>> b[22:29]
'complex'
>>> b[7:9]
'is'
>>> #negitive silicing
>>> a="python is easy to learn"
>>> a[-13:-9]
'easy'
>>> a[-23:-17]
'python'
>>> b[-5:0]
''
b[-5:-1]
'mple'
b[-5:]
'mplex'
a[-5:0]
''
a[-5:]
'learn'
b="God is great"
b[-5:]
'great'
b[12:9]
''
b[-12:-9]
'God'
b[-8:-6]
'is'
a[--8:-6]
's easy to'
b[--8:-6]
''
