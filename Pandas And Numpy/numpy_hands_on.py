Numpy Array (Numerical Python)
===============================================
-- Fast and multi-dimensional array - can store different types of data 
-- each element is an object of type 'dtype'

>>> import numpy
>>> a = numpy.array([["a","b"], [2,3]])
>>>
>>> a
array([['a', 'b'],
       ['2', '3']], dtype='<U1')

>>> a.dtype
dtype('<U1')
>>>
>>> a[0]
array(['a', 'b'], dtype='<U1')

>>> a[0].dtype
dtype('<U1')

>>> for i in a:
...       print(i)
...
['a' 'b']
['2' '3']
