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

# here we are sending named varied number of variables  
  def sum(*values, **options):
    s = 0
    for i in values:
        s = s + i
    if "neg" in options:
        if options["neg"]:
            s = -s
    return s

s = sum(1, 2, 3, 4, 5)            # returns 15
s = sum(1, 2, 3, 4, 5, neg=True)  # returns -15
s = sum(1, 2, 3, 4, 5, neg=False) # returns 15
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
4) what does "yield" keyword do in Python? what are iterators and generators in Python?
==>
Iterators are those data structures in python on which you can use "for i in x" operation as many number of times as you want. but you 
store all the values in memory and this is not always what you want when you have a lot of values.

Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they 
generate the values on the fly:
  
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4

It is just the same except you used () instead of []. BUT, you cannot perform for i in mygenerator a second time since generators can 
only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

===================================================================================================================================
5) 
