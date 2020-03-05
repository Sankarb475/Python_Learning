Pandas series data structure
==================================================
- one dimensional labeled array object (No column headers)
>>> c = pd.Series([1,2,3])
>>>
>>> c
0    1
1    2
2    3
dtype: int64
>>>
>>> c
0    1
1    2
2    3
dtype: int64
>>>
>>> c = pd.Series((1,2,3))
>>> c
0    1
1    2
2    3
dtype: int64

>>> numpy.array
<built-in function array>

>>> c = pd.Series({1:2})
>>> c
1    2
dtype: int64

We can define the row indexes as well
==============================================
>>> a = pd.Series({1:5,2:10,5:47,6:40,9:13})
>>> a
1     5
2    10
5    47
6    40
9    13
dtype: int64

We can select rows based on some indexes
=============================================
>>> a[[1,5]]
1     5
5    47
dtype: int64

>>> b = [1,5,9]
>>> a[b]
1     5
5    47
9    13
dtype: int64

Modifying/updating
