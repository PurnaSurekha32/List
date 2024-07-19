Python 3.6.3rc1 (v3.6.3rc1:d8c174a, Sep 19 2017, 16:39:51) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=["a","s",["c",["h","p",["e","i"],"y"],"l"],"m","n"]
>>> l[3][2]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l[3][2]
IndexError: string index out of range
>>> 
>>> l[2]
['c', ['h', 'p', ['e', 'i'], 'y'], 'l']
>>> l[2][1]
['h', 'p', ['e', 'i'], 'y']
>>> l[2][3][0:2]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l[2][3][0:2]
IndexError: list index out of range
>>> 
>>> 
>>> l[2][1][2]
['e', 'i']
>>> l[2][1][3]
'y'
>>> 
