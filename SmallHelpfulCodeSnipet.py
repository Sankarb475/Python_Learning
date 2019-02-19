# creating a list of integers having same value

>>> a = [5] * 5
>>> a
[5, 5, 5, 5, 5]

>>> b = []
>>> b.append([1]*6)
>>> b
[[1, 1, 1, 1, 1, 1]]


# sorting a dictionary based on the values ::
>>> import operator
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> sorted_x = sorted(x.items(), key=operator.itemgetter(1))
>>> sorted_x
[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]


# switching keys and values in a dictionary in python
>>> my_dict = {'a':1,'b':2}
>>> my_dict2 = {y:x for x,y in my_dict.items()}
>>> my_dict2
{1: 'a', 2: 'b'}


# Convert a String representation of a Dictionary to a dictionary
>>> import ast
>>> ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
{'muffin': 'lolz', 'foo': 'kitty'}

