Python 3.6.3rc1 (v3.6.3rc1:d8c174a, Sep 19 2017, 16:39:51) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> #LISTS
>>> 
>>> a=[1,2,3,"Sai",1+8j,True,False]
>>> a
[1, 2, 3, 'Sai', (1+8j), True, False]
>>> type(a)
<class 'list'>
>>> 
>>> 
>>> 
>>> #Lists Methods
>>> a.append(2+6j)
>>> a
[1, 2, 3, 'Sai', (1+8j), True, False, (2+6j)]
>>> 
>>> 
>>> #Extend
>>> 
>>> a.extend(["v",3+3])
>>> a
[1, 2, 3, 'Sai', (1+8j), True, False, (2+6j), 'v', 6]
>>> 
>>> 
>>> 
>>> #Insert
>>> a=[1, 2, 3, 'Sai', (1+8j), True, False, (2+6j), 'v', 6]
>>> a.insert(2,"Python")
>>> a
[1, 2, 'Python', 3, 'Sai', (1+8j), True, False, (2+6j), 'v', 6]
>>> 
>>> 
>>> 
>>> #Index
>>> a.index(2)
1
>>> 
>>> 
>>> 
>>> #Copy
>>> 
>>> a.copy()
[1, 2, 'Python', 3, 'Sai', (1+8j), True, False, (2+6j), 'v', 6]
>>> 
>>> 
>>> #Remove
>>> a.remove("Sai")
>>> a
[1, 2, 'Python', 3, (1+8j), True, False, (2+6j), 'v', 6]
>>> 
>>> 
>>> 
>>> #POP
>>> 
>>> a.pop(1)
2
>>> a
[1, 'Python', 3, (1+8j), True, False, (2+6j), 'v', 6]
>>> 
>>> 
>>> 
>>> #Reverse
>>> 
>>> a.reverse()
>>> a
[6, 'v', (2+6j), False, True, (1+8j), 3, 'Python', 1]
>>> 
>>> 
>>> 
>>> #Sort
>>> a.sort()
>>> a
['A', 'F', 'K', 'O', 'P', 'U', 'V']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Clear
>>> 
>>> a.clear()
>>> a
[]
>>> a.extend([6, 'v', (2+6j), False, True, (1+8j), 3, 'Python', 1])
>>> a
[6, 'v', (2+6j), False, True, (1+8j), 3, 'Python', 1]
>>> 
>>> 
>>> #count
>>> a.count(2)
0
>>> a.count(0)
1
>>> 
>>> 
>>> 
>>> #Len
>>> a=["V"]
>>> len(a)
1
>>> a.count("v")
0
>>> a=[6, 'v', (2+6j), False, True, (1+8j), 3, 'Python', 1]
>>> a.count("v")
1
>>> a.count(2+6j)
1
>>> a.count((2+6j))
1
>>> 
>>> 
