1) Adding two dictionary in python :: use update method

--if you are using Python 2.x

>>> def merge_two_dicts(x, y):
...     z = x.copy()
...     z.update(y) 
...     return z

>>> x
{'a': 1, 'b': 2}
>>> y
{'a': 1, 'c': 11, 'b': 2}

>>> a = merge_two_dicts(x,y)
>>> a
{'a': 1, 'c': 11, 'b': 2}

>>> a = merge_two_dicts(x,{'d':1})
>>> a
{'a': 1, 'b': 2, 'd': 1}

--in python 3.5 or greater

>>> x = {'a':1, 'b': 2}
>>> y = {'b':10, 'c': 11}

>>> z = {**x, **y}
>>> z
{'a': 1, 'b': 10, 'c': 11}


==============================================================================================================================
