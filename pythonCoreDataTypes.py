>>> from math import sqrt
>>> sqrt(16)
4.0
>>> import math
>>> math.pi
3.141592653589793

>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod'
, 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 
'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# The math module contains more advanced numeric tools as functions, while the ran dom module performs random-number generation 
# and random selections

>>> import random
>>> random.random() 
0.7082048489415967
>>> random.choice([1, 2, 3, 4]) 
1

#numbers, strings, and tuples are immutable; lists, dictionaries, and sets are not

#List Operations
>>> L = [123, 'spam', 1.23]
>>> len(L)
3

>>> L*2
[123, 'spam', 1.23, 123, 'spam', 1.23]

>>> L[:]
[123, 'spam', 1.23]

>>> L[2:]
[1.23]
>>> L[:-1]
[123, 'spam']

>>> L.append(23)
[123, 'spam', 1.23, 23]

>>> L.pop(2)
1.23
>>> L
[123, 'spam', 23]

>>> list = [1,23,4,56,33,656,564]
>>> list.sort()
>>> list
[1, 4, 23, 33, 56, 564, 656]

#selecting a partcular column from a 2D list
>>> list2D = [[1,2,3],[4,5,6],[7,8,9]]
>>> list2D[1][2]
6
>>> col2 = [row[1] for row in list2D]   #Give me row[1] (2nd element) for each row in matrix M, in a new list.
>>> col2
[2, 5, 8]
>>> M
['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']

>>> [row[1] for row in M if row[1] % 2 == 0]      #Filter out odd items
[2, 8]

#diagonal matrix
>>> diag = [M[i][i] for i in [0, 1, 2]] >>> diag
[1, 5, 9]

# Repeat characters in a string
>>> doubles = [c * 2 for c in 'spam'] >>> doubles
['ss', 'pp', 'aa', 'mm']

>>> list(range(4)) 
[0, 1, 2, 3]

>>> a = list(range(-6,7,2))
>>> a
[-6, -4, -2, 0, 2, 4, 6]
    
>>> [[x ** 2, x **3] for x in range(4)]
[[0, 0], [1, 1], [4, 8], [9, 27]]

>>> [[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0] 
[[2, 1.0, 4], [4, 2.0, 8], [6, 3.0, 12]]

>>> [[x, int(x / 2), x * 2] for x in range(-6, 7, 2) if x > 0] 
[[2, 1, 4], [4, 2, 8], [6, 3, 12]]

>>> G = (sum(row) for row in M)
>>> G
<generator object <genexpr> at 0x105b29408>
>>> next(G)
6
>>> next(G)
15
>>> next(G)
24

'''Dictionaries :: Dictionaries, the only mapping type (not a sequence) in Python’s core objects set, are also mutable '''
>>> D = {}
>>> type(D)
<class 'dict'>
>>> D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
>>> D
{'food': 'Spam', 'quantity': 4, 'color': 'pink'}

#using dict to define a dictionary
>>> bob1 = dict(name='Bob', job='dev', age=40) 
>>> bob1
{'age': 40, 'name': 'Bob', 'job': 'dev'}

#zipping way to define dictionary
>>> bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
>>> bob2
{'name': 'Bob', 'job': 'dev', 'age': 40}

#Complex nesting of different types in python - one of the advantage of using python, complex nesting is easy to implement
>>> rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr'], 'age': 40.5}
>>> rec['jobs'][1]
'mgr'

>>> rec['name']['last']
'Smith'

>>> rec['jobs'].append('support')
>>> rec
{'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr', 'support'], 'age': 40.5}

#In Python, when we lose the last reference to the object—by assigning its variable to something else
>>> rec = 0

#Python has a feature known as garbage collection that cleans up unused memory as your program runs and frees you from having to manage such details in your code.
>>> D = {'a': 1, 'b': 2, 'c': 3}

#so now, what ".get" does is it will select the data with the key 'x' in dictionary D, if it doesnyt find it, it will return 0
>>> value = D.get('x', 0)
>>> value
0

#Sorting Keys: for Loops
>>> sorted(D)
['a', 'b', 'c']

>>> Ks = list(D.keys()) 
>>> Ks
['a', 'c', 'b']
>>> Ks.sort() 
>>> Ks
['a', 'b', 'c']

#Tuples :: tuples are sequences, like lists, but they are immutable. Functionally, they’re used to represent fixed collections of items.
>>> T = (1, 2, 3, 4, 5)
>>> len(T)
5
>>> T + (5,6)
(1, 2, 3, 4, 5, 5, 6)
>>> T
(1, 2, 3, 4, 5)
>>> T[0]
1
>>> T.index(4)
3
>>> T.count(4)
1
#tuples provide a sort of integrity constraint

'''Set :: Sets are neither mappings nor sequences; rather, they are unordered collections of unique and immutable objects
they support the usual mathematical set operations
'''
>>> X = set('spam')
>>> X
{'a', 's', 'p', 'm'}

#Set operations
>>> X, Y
({'a', 's', 'p', 'm'}, {'t', 'u', 'a', 's', 'p', 'l'})
>>> X - Y                                                                    #difference
{'m'}
>>> Y - X                                                                    #difference
{'t', 'l', 'u'}
>>> X & Y                                                                    #Intersection
{'a', 's', 'p'}
>>> X | Y                                                                    #Union
{'t', 'm', 'u', 'a', 's', 'p', 'l'}

#checking superset
>>> X > Y
False

>>> set('spam') == set('asmp')
True
>>> set('spam') - set('ham') 
{'p', 's'}

'''Decimal : fixed-precision floating-point numbers, and fraction numbers, which are rational numbers with 
both a numerator and a denominator.
'''
>>> import decimal
>>> a = (2/3) + (1/2)
>>> a
1.1666666666666665
>>> d = decimal.Decimal(a)
>>> d
Decimal('1.166666666666666518636930049979127943515777587890625')

#Fraction
>>> from fractions import Fraction
>>> f = Fraction(2, 3)
>>> f
Fraction(2, 3)
>>> f + 1
Fraction(5, 3)
>>> f + Fraction(1,3)
Fraction(1, 1)

