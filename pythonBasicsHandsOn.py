# Python Decorators
-- A design pattern to in python - takes in a function, adds some functionality and returns it.
-- This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


>>> ordinary()
I am ordinary

>>> # let's decorate this ordinary function
>>> pretty = make_pretty(ordinary)
>>> pretty()
I got decorated
I am ordinary
  
 
#Python Serialization
===============================================
Pickling is the process whereby a Python object hierarchy is converted into a byte stream (usually not human readable) to be written to a file, 
this is also known as Serialization. Unpickling is the reverse operation, whereby a byte stream is converted back into a working Python object hierarchy.

import pickle
# serializes
pickle.dump()

#deserializes
pickle.load()
 
 

'''to run python in command prompt, use "python", (windows :considering you have set up environment variable)
The interactive prompt runs code and echoes results as you go, but it doesn’t save your code in a file
'''

# enumerate() in python ==> it will give you the index numbers while iterating

>>> for n,i in enumerate(arr):
...       print(n,i)
...
0 6
1 4
2 2
3 1
4 3
5 5
6 7
>>> arr
[6, 4, 2, 1, 3, 5, 7]


#to get current working directory
>>> import os
>>> os.getcwd()
'/Users/sankar.biswas'

#changing current direcctory 
>>> os.chdir('/Users/sankar.biswas/Desktop/Python/coding')
>>> os.getcwd()
'/Users/sankar.biswas/Desktop/Python/coding'

# to run a python script from command prompt
python file1.py

#saving the output in a file 
python script1.py > saveit.txt

# "dir" - you can use it to fetch a list of all the names available inside a module
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', 
 '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework', '_getframe', '_git', 
 '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 
 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 
 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 
 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 
 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 
 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_asyncgen_hooks', 
 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']

 # the " exec(open('module.py').read())" built-in function call is another way to launch files from the interactive prompt without having to import and later reload

 #you can also find out the functions you can apply on a variable using "dir"
 >>> a = 234
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', 
 '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', 
 '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__'
 , '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', 
 '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
 '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# this will help you get a knowledge on the functionality of the function, dial 'q' to escape
>>> help(a.__abs__)

# Pattern Matching
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
>>> match
<re.Match object; span=(0, 18), match='Hello Python world'>
>>> match.group(1)
'Python '

>>> match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack') 
>>> match.groups()
('usr', 'home', 'lumberjack')
>>> re.split('[/:]', '/usr/home/lumberjack') 
['', 'usr', 'home', 'lumberjack']

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

#adding multiple elements to an existing list
>>> L
[123, 'abc', 1.23, {}]
>>> L.extend([5,6,7])
>>> L
[123, 'abc', 1.23, {}, 5, 6, 7]

#deleting all the elements
>>> L.clear()
>>> L
[]

#deleting a single element by index
>>> L = [123, 'abc', 1.23, {}]
>>> del L[0]
>>> L
['abc', 1.23, {}]

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


#String slicing, so the last number is the gap of skipping, that is 1,3,5,... will be skipped
>>> S = "I a m s a d"
>>> S[::2]
'Iamsad'

#the third index if given negative will reverse the selection
>>> S[::-2]
'dasmaI'

>>> S
'I evol being alone'
>>> S[5:1:-1]
'love'
>>> 
>>> S[::-1]
'enola gnieb love I'

#converting whatever we have into string
>>> repr(42)
'42'

#converting into ASCII 
>>> ord('A')
65

#converting integer to binary
>>> bin(13)
'0b1101'

#converting binary to integer
>>> int('1101', 2)
13





