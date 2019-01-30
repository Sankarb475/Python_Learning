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
