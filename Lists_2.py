Python 3.6.3rc1 (v3.6.3rc1:d8c174a, Sep 19 2017, 16:39:51) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> #List[]
>>> 
>>> s=["Hello","Python"]
>>> print("-".join(s))
Hello-Python
>>> print("*".join(s))
Hello*Python
>>> 
>>> 
>>> s=["Hello","Python","lan"]
>>> print("-".join(s))
Hello-Python-lan
>>> 
>>> 
>>> s=['xyz', 'zara', 'PYnative']
>>> print (max(s))
zara
>>> s=['xxx', 'zara', 'PYnative']
>>> print (max(s))
zara
>>> s=['xxx', 'aara', 'PYnative']
>>> print (max(s))
xxx
>>> 
>>> 
>>> s=[10, 20, 30, 40, 50]
>>> print(s[-2])
40
>>> print(s[-4:-1])
[20, 30, 40]
>>> 
>>> 
>>> 
>>> a=[10, 20, 30, 40, 50, 60, 70, 80]
>>> print(a[2:5],a[:4],a[3:])
[30, 40, 50] [10, 20, 30, 40] [40, 50, 60, 70, 80]
>>> 
>>> 
>>> 
>>> 
>>> listOne  =  ['a', 'b', 'c', 'd']
>>> listTwo =  ['e', 'f', 'g']
>>> 
>>> newList = listOne + listTwo
>>> print(newList)
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> 
>>> 
>>> 
>>> newList = extend(listOne, listTwo)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    newList = extend(listOne, listTwo)
NameError: name 'extend' is not defined
>>> 
>>> 
>>> 
>>> newList = listOne.extend(listTwo)
>>> print(newList)
None
>>> 
>>> print(listOne.extend(listTwo))
None
>>> listOne.extend(listTwo)
>>> 
>>> 
>>> print(listOne.append(listTwo))
None
>>> 
>>> 
>>> newList.extend(listOne, listTwo)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    newList.extend(listOne, listTwo)
AttributeError: 'NoneType' object has no attribute 'extend'
>>> 
>>> 
>>> newList.extend([listOne, listTwo])
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    newList.extend([listOne, listTwo])
AttributeError: 'NoneType' object has no attribute 'extend'
>>> 
>>> 
>>> listOne.extend([listTwo])
>>> listOne
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e', 'f', 'g', 'e', 'f', 'g', ['e', 'f', 'g'], ['e', 'f', 'g']]
>>> 
>>> 
>>> 
>>> print(listOne.join(listTwo))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(listOne.join(listTwo))
AttributeError: 'list' object has no attribute 'join'
>>> 
>>> 
>>> 
>>> sampleList = [10, 20, 30, 40, 50]
>>> sampleList.append(60)
>>> print(sampleList)
[10, 20, 30, 40, 50, 60]
>>> print(sampleList.append(60))
None
>>> sampleList.append(60)
>>> print(sampleList)
[10, 20, 30, 40, 50, 60, 60, 60]
>>> 
>>> 
>>> 
>>> 
>>> aList = [4, 8, 12, 16]
>>> aList[1:4] = [20, 24, 28]
>>> print(aList)
[4, 20, 24, 28]
>>> 
>>> 
>>> 
>>> aList = [4, 8, 12, 16,829,9873,899]
>>> aList[2:5] = [20, 24, 28]
>>> print(aList)
[4, 8, 20, 24, 28, 9873, 899]
>>> 
>>> 
>>> 
>>> aList = [5, 10, 15, 25]
>>> print(aList[::-2])
[25, 10]
>>> 
>>> print(aList[:])
[5, 10, 15, 25]
>>> 
>>> print(aList[:-2])
[5, 10]
>>> 
>>> 
>>> 
>>> 
>>> sampleList = [10, 20, 30, 40]
>>> del sampleList[0:6]
>>> print(sampleList)
[]
>>> 
>>> 
>>> resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
>>> print(resList)
['Hello Dear', 'Hello Bye', 'Good Dear', 'Good Bye']
>>> 
>>> 
>>> 
>>> 
>>> s=[10,20,30,40,50]
>>> s.pop()
50
>>> s.pop(2)
30
>>> s.pop()
40
>>> s=[10,20,30,40,50]
>>> 
>>> 
>>> s.pop()
50
>>> s
[10, 20, 30, 40]
>>> 
>>> 
>>> s.pop(2)
30
>>> s.pop()
40
>>> s=[10,20,30,40,50]
>>> 
>>> s.pop()
50
>>> s
[10, 20, 30, 40]
>>> 
>>> 
>>> s.pop(2)
30
>>> s
[10, 20, 40]
>>> 
>>> 
>>> 
>>> s.pop(0:5)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> aList = ["PYnative", [4, 8, 12, 16]]
>>> 
>>> print(aList[0][1])
Y
>>> 
>>> 
>>> print(aList[1][3])
16
>>> 
>>> 
>>> 
>>> aList = [1, 2, 3, 4, 5, 6, 7]
>>> pow2 =  [2 * x for x in aList]
>>> pow2
[2, 4, 6, 8, 10, 12, 14]
>>> 
>>> 
>>> 
>>> 
>>> aList = ['a', 'b', 'c', 'd']
>>> 
>>> newList.copy(aList)
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    newList.copy(aList)
AttributeError: 'NoneType' object has no attribute 'copy'
>>> 
>>> 
>>> 
>>> newList = copy(aList)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    newList = copy(aList)
NameError: name 'copy' is not defined
>>> 
>>> 
>>> 
>>> newList = aList.copy()
>>> newList
['a', 'b', 'c', 'd']
>>> 
>>> 
>>> 
>>> newList = list(aList)
>>> newList
['a', 'b', 'c', 'd']
>>> 
>>> 
>>> 
>>> 
>>> l = [None] * 10
>>> print(len(l))
10
>>> 
>>> 
>>> 
>>> 
>>> l = [sai] * 10
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    l = [sai] * 10
NameError: name 'sai' is not defined
>>> 
>>> 
>>> l = [True] * 10
>>> print(len(l))
10
>>> 
>>> 
>>> l = ["sai"] * 10
>>> print(len(l))
10
>>> l = ["1"] * 10
>>> print(len(l))
10
>>> 
>>> 
>>> l = [for] * 10
SyntaxError: invalid syntax
>>> l = [6] * 10
>>> print(len(l))
10
>>> l = [6] * 1
>>> print(len(l))
1
>>> 
>>> 
>>> 
>>> newList = listOne.extend(listTwo)
>>> newList
>>> 
>>> 
>>> 
>>> 
>>> listOne  =  ['a', 'b', 'c', 'd']
>>> listTwo =  ['e', 'f', 'g']
>>> 
>>> newList = listOne.extend(listTwo)
>>> print(newList)
None
>>> 
