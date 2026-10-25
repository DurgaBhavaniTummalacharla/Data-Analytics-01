Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #negitive striding
>>> a="python course"
>>> a[-1:8:-2]
'er'
>>> a[-1:-8:-2]
'ero '
>>> a[-2:-10:-3]
'son'
>>> a[-3:-13:-4]
'r t'
>>> a[-1:-12:-6]
'e '
>>> a[-4:-9:-2]
'ucn'
>>> 9a[5:9:2]
SyntaxError: invalid decimal literal
>>> a[5:9:2]
'nc'
>>> a[-10:-6:-2]
''
>>> a[-6:-10:-2]
'cn'
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
