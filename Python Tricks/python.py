How to make a class return a value when initializing it?
=>
Python constructor does not allow any return statment in its body.

>>> class Foo:
...     def __init__(self):
...         return 42
... 
>>> foo = Foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() should return None


But there is one way to return when an object is created of a class using "__str__" method.

class Car:
    def __init__(self, speed, unit):
        self.speed = speed
        self.unit = unit

    def __str__(self):
        return str("Car with the maximum speed of {0} {1}".format(self.speed, self.unit))

-- if we create an object of class Car, it will automatically call "__str__" method which will return a value.   

===================================================================================================================================
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
5) what does enumerate() do to an iterable?
==>
Enumerate() adds a counter to an iterable. So for each element in the iterable you get a tuple, the first element of that is the 
sequential counter value, the other element is the value itself. For dictionary the second value of tuple will be just the key.

>>> for item in enumerate(["a", "b", "c"]):
...     print (item)
...
(0, 'a')
(1, 'b')
(2, 'c')

>>> enumerate(b)
<enumerate object at 0x00000280BFE69630>

>>> a = [1,2,3]
>>> a = [11,22,33]
>>> for idx, val in enumerate(a):
...       print(idx, val)
...
0 11
1 22
2 33

data = {'a':1, 'b':2}
for idx, d in enumerate(data):
    print(idx, d)
    
0 a
1 b

data = {'a':1, 'b':2}
for idx, d in enumerate(data):
    print(idx, data[d])
0 1
1 2

-- by default enumerate starts counting from 0, we can give any other value as well 
>>> for item in enumerate(["a", "b", "c"], 100):
...     print (item)
...
(100, 'a')
(101, 'b')
(102, 'c')

=====================================================================================================================================
6) how to do a string filter based on "not contains" the specific value?
==>
using "~" we can do not contains in python, example below::
>>> a = ["horror, adv", "romance", "fight, action"]
>>> b = pd.DataFrame(a, columns = ["Genre"])
>>> b
           Genre
0    horror, adv
1        romance
2  fight, action
>>>
>>> c = b[ ~ b.Genre.str.contains('horror')]
>>> c
           Genre
1        romance
2  fight, action

-- another method 
>>> d = b[b.Genre.str.contains('horror')==False]
>>> d
           Genre
1        romance
2  fight, action

-- another syntax 
df[df["col"].apply(lambda x:x not in [word1,word2,word3])]
