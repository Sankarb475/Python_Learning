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

# Getting timestamp in python
>>> import datetime

>>> datetime.datetime.now()
datetime.datetime(2019, 2, 19, 15, 55, 47, 368423)

>>> str(datetime.datetime.now())
'2019-02-19 15:55:53.691894'

# substracting current time by 5 hours and get the timestamp

>>> timesTamp = str(datetime.datetime.now() - datetime.timedelta(hours = 5))
>>> timesTamp
'2019-02-19 10:57:11.593920'

# substracting current time by 15 minutes and get the timestamp
>>> timesTamp = str(datetime.datetime.now() - datetime.timedelta(minutes = 15))
>>> timesTamp
'2019-02-19 15:43:08.448387'


