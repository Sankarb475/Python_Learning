1) how to check whether a variable is of a certain type?
=>
isinstance() function can help us find it out.

# for list
>>> m
[5]
>>> isinstance(m, list)
True

#for dictionary
>>> m = {'a':1}
>>> isinstance(m,dict)
True

===================================================================================================================================
2) What does the star(*) operator mean, in a function call? [duplicate]
=>
The single star * unpacks the sequence/collection into positional arguments.
>>> def add(a,b):
...       print(a+b)

>>> values = [1,2]
>>> add(*values)
3

The double star is when you have named parameters, like a dictionary
>>> def funct1(tom, tommy):
...       print(tom + tommy)

>>> a = {"tom":5, "tommy":5}
>>> funct1(**a)
10

>>> a = {"tommy":5, "tom":5}
>>> funct1(**a)
10

>>> a = {"tom":5, "jerry":5}
# throws errro because it doesnt have tommy parameter rather it has "jerry"
>>> funct1(**a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: funct1() got an unexpected keyword argument 'jerry'

===================================================================================================================================
3) Arbitary argument list / varied number of arguments?
=>
we can push varied number of arguments in a function call using "*".

>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'

>>> val = ("Puja","Atrayee","Trina")
>>> concat(*val)
'Puja/Atrayee/Trina'
===================================================================================================================================
