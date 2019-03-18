Addition of data structures ::
    
#List
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a + b
[1, 2, 3, 4, 5, 6]

#Set
>>> a = {1,2,3}
>>> b = {4,5,6}
>>> a|b
{1, 2, 3, 4, 5, 6}

>>> a = {1,2,3}
>>> b = {4,5,6}
>>> a.update(b)
>>> a
{1, 2, 3, 4, 5, 6}

>>> z = a.copy()
>>> z.update(b)
>>> z
{1, 2, 3, 4, 5, 6}

#Tuple
>>> a = (1,2,3)
>>> b = (4,5,6)
>>> a + b
(1, 2, 3, 4, 5, 6)

#Dictionary
after python 3
>>> a = {1:2,2:3}
>>> b = {3:4,4:5}
>>> {**a,**b}
{1: 2, 2: 3, 3: 4, 4: 5}

or you can make use of copy and then update statement

Subtraction of data structures ::

#List
>>> a = [1,2,3,4,5]
>>> b = [3,4,5,6,7]
>>> l3 = [x for x in a if x not in b]
>>> l3
[1, 2]

>>> set(a) - set(b)
{1, 2}

If you just want to have the elements that are not common in both the list ::
>>> c = set(a) - set(b)
>>> d = (set(a) | set(b)) - c
>>> d
{3, 4, 5, 6, 7}

#Set 
>>> set(a) - set(b)
{1, 2}

#Tuple 
>>> set(a) - set(b)
{1, 2, 3}

Comparing data structures ::
>>> a
{1: 2}
>>> b
{2: 3, 4: 5}
>>> 
>>> a == b
False
>>> b = {1:2}
>>> a == b
True


Data type conversion ::

#List to String
>>> a = ['l','i','f','e']
>>> ''.join(a)
'life'

>>> ','.join(a)
'l,i,f,e'

#String to List
>>> a = 'Beautiful'
>>> b = list(a)
>>> b
['B', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l']

#List to Set
>>> a = [1,2,1]
>>> b = set(a)
>>> b
{1, 2}

#Set to List
>>> c = list(b)
>>> c
[1, 2]

#String to Set
>>> a = 'virtualization'
>>> b = set(a)
>>> b
{'t', 'o', 'u', 'r', 'i', 'v', 'a', 'l', 'z', 'n'}


#converting a list of string to a list of integers in python 3
>>> a = ['1','2']
>>> a = list(map(int,a))
>>> a
[1, 2]


#Tuple to list
>>> a = (1,2,3)
>>> b = list(a)
>>> b
[1, 2, 3]


#List to Tuple
>>> b
[1, 2, 3]
>>> d = tuple(b)
>>> d
(1, 2, 3)








