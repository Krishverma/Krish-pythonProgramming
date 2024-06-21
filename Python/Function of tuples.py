
>>> t1=(1,2,3,'A')
>>> t1
(1, 2, 3, 'A')
>>> m,n,l,o=t1
>>> m
1
>>> n
2
>>> l
3
>>> o
'A'
>>> o=4
>>> t1=(m,n,l,o)
>>> t1
(1, 2, 3, 4)
>>> len(t1)
4
>>> max(t1)
4
>>> 
>>> min(t1)
1
>>> t2=(a,b,c,d)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t2=(a,b,c,d)
NameError: name 'a' is not defined
>>> t2=("a","b","c","d")
>>> min(t2)
'a'
>>> t1.index(3)
2
>>> t1.index(5)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    t1.index(5)
ValueError: tuple.index(x): x not in tuple
>>> t1.coount(4)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    t1.coount(4)
AttributeError: 'tuple' object has no attribute 'coount'
>>> t1.count(4)
1
>>> t1.count(5)
0
>>> lst[3]-
SyntaxError: invalid syntax
>>> lst[3]-'A'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    lst[3]-'A'
NameError: name 'lst' is not defined
>>> lst=list(t1)
>>> lst
[1, 2, 3, 4]
>>> lst[3]-"A"
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    lst[3]-"A"
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> lst
[1, 2, 3, 4]
>>> lst[3]='A'
>>> lst
[1, 2, 3, 'A']
>>> t1=tuple(lst)
>>> t1
(1, 2, 3, 'A')
>>> t1[0]=6
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t1[0]=6
TypeError: 'tuple' object does not support item assignment
>>> a,b,c,d=t1
>>> a
1
>>> b
2
>>> c
3
>>> d
'A'
>>> a='Z'
>>> t1=(a,b,c,d)
\
>>> t1
('Z', 2, 3, 'A')
>>> lst=list(t1)
>>> t1
('Z', 2, 3, 'A')
>>> lst
['Z', 2, 3, 'A']
>>> lst[0]=100
>>> ti=tuple(lst)
>>> t1
('Z', 2, 3, 'A')
>>> t1=tuple(lst)
>>> t1
(100, 2, 3, 'A')
