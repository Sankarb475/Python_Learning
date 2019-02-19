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
