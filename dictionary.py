Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict{}
a={"name":"pooja","year":2026,"month":10}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 10}
type(a)
<class 'dict'>
b={"name","pooja","year",2026}
print(b)
{'year', 2026, 'name', 'pooja'}
type(b)
<class 'set'>
a={"year":2026,"month":"oct","date":31}
a.keys()
dict_keys(['year', 'month', 'date'])
a.values()
dict_values([2026, 'oct', 31])
a.items()
dict_items([('year', 2026), ('month', 'oct'), ('date', 31)])
b={1:2,3:4}
type(b)
<class 'dict'>
a.keys()
dict_keys(['year', 'month', 'date'])
b.keys()
dict_keys([1, 3])
#accessing
a={"course":"python","code":"gnan","data":"coding}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"course":"python","code":"gnan","data":"coding}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"course":"python","code":"gnan","data":"coding"}
   
a["course"]
   
'python'
a
   
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
#get
   
a.get("code")
   
'gnan'
a
   
{'course': 'python', 'code': 'gnan', 'data': 'coding'}
#update
   
a={"year":2026,"month":11}
   
a.update({"time":10})
   
a
   
{'year': 2026, 'month': 11, 'time': 10}
a.update({"hour":1},{"min":10})
   
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a.update({"hour":1},{"min":10})
TypeError: update expected at most 1 argument, got 2
a.update({"hour":1,"min":10})
   
a
   
{'year': 2026, 'month': 11, 'time': 10, 'hour': 1, 'min': 10}
#set default
   
a={"color":"black","food":"biryaani","desert":"cake"}
   
a.setdefault("place","vja")
   
'vja'
a
   
{'color': 'black', 'food': 'biryaani', 'desert': 'cake', 'place': 'vja'}
#pop
   
a.pop("colour")
   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.pop("colour")
KeyError: 'colour'
a.pop()
   
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("colour")
   
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.pop("colour")
KeyError: 'colour'
a.pop("color")
   
'black'
a
   
{'food': 'biryaani', 'desert': 'cake', 'place': 'vja'}
a.popitem()
   
('place', 'vja')
a
   
{'food': 'biryaani', 'desert': 'cake'}
#copy
   
a={"hour":10,"min":11,"sec":5}
   
a.copy()
   
{'hour': 10, 'min': 11, 'sec': 5}
b=a.copy()
   
\
b
   
{'hour': 10, 'min': 11, 'sec': 5}
a.clear()
...    
>>> a
...    
{}
>>> a={"name":"pooja","city":"vja","name":"pooja"}
...    
>>> print(a)
...    
{'name': 'pooja', 'city': 'vja'}
>>> a={"name":"pooja","city":"vja","name":"priya"}
...    
>>> print(a)
...    
{'name': 'priya', 'city': 'vja'}
>>> a={"name1":"pooja","city":"vja","name2":"pooja"}
...    
>>> a
...    
{'name1': 'pooja', 'city': 'vja', 'name2': 'pooja'}
>>> a={"idnos":[10,20,30],"names":["bhavani","chinni","chinnu"],"marks":[60,70,80]}
...    
>>> print(a)
...    
{'idnos': [10, 20, 30], 'names': ['bhavani', 'chinni', 'chinnu'], 'marks': [60, 70, 80]}
>>> type(a)
...    
<class 'dict'>
>>> a.keys()
...    
dict_keys(['idnos', 'names', 'marks'])
>>> a.vlaues()
...    
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.vlaues()
AttributeError: 'dict' object has no attribute 'vlaues'. Did you mean: 'values'?
>>> a.values()
...    
dict_values([[10, 20, 30], ['bhavani', 'chinni', 'chinnu'], [60, 70, 80]])
>>> a.items()
...    
dict_items([('idnos', [10, 20, 30]), ('names', ['bhavani', 'chinni', 'chinnu']), ('marks', [60, 70, 80])])
