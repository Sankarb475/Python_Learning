''' Why python?

==> object-oriented scripting language which has functional programming capability.

software quality ==> readble, coherence, software quality, reusable, maintainability 

Developer productivity ==> lines of code is much less in volume with respect to C++ or Java that is less to type, debug and 
easy maintainability

Program portability ==> with respect to version or OS (linux and windows) doesnt trouble us much when importing the code from
one OS to another

Support libraries ==> self-explanatory 

Downside ==> a bit slower than other low level language like C or C++

---a general-purpose language, Python’s roles are virtually unlimited: you can use it for everything from website development 
and gaming to robotics and spacecraft control

'''

'''Interpreter ==>
An interpreter is a kind of program that executes other programs. When you write a Python program, the Python interpreter reads 
your program and carries out the instructions it contains. In effect, the interpreter is a layer of software logic between your 
code and the computer hardware on your machine.
'''


'''Running python code :: 
python file_name.py

when you execute a program Python first compiles your source code (the statements in your file) into a format known as byte code
Compilation is simply a translation step, and byte code is a lower-level, platform-independent representation of your source code
This byte code translation is performed to speed execution —byte code can be run much more quickly than the original source code 
statements in your text file. .pyc extension for the byte code.
__pycache__ ==> this file stores these byte codes.

Once your program has been compiled to byte code (or the byte code has been loaded from existing .pyc files), it is shipped off 
for execution to something generally known as the Python Virtual Machine. The PVM is the runtime engine of Python; it’s always 
present as part of the Python system, and it’s the component that truly runs your scripts. Technically, it’s just the last step
of what is called the “Python interpreter.”
'''


'''
Jython
The Jython system (originally known as JPython) is an alternative implementation of the Python language, targeted for integration 
with the Java programming language. Jython consists of Java classes that compile Python source code to Java byte code and then 
route the resulting byte code to the Java Virtual Machine (JVM). Programmers still code Python statements in .py text 
files as usual; the Jython system essentially just replaces the rightmost two bubbles in Figure 2-2 with Java-based equivalents
'''


#Python Module
'''
every file of Python source code whose name ends in a .py extension is a module. Every file of Python source code whose name ends 
in a .py extension is a module. Other files can access the items a module defines by importing that module —import operations 
essentially load another file and grant access to that file’s contents.
If you have imported one module,

import script1

now you made some changes over that module and you reimport it again just to make sure your recent changes are reflecting. 
But it wouldnt do that, because imports are too expensive an operation to repeat more than once per file. So to have it 
reflected you got to restart the session or you can follow the below steps ::

import script1
from imp import reload
reload(script1)

a module is mostly just a package of variable names, known as a namespace, and the names within that package are called attributes. 
An attribute is simply a variable name that is attached to a specific object (like a module)
'''


#Python structures
'''
1. Programs are composed of modules. 
2. Modules contain statements.
3. Statements contain expressions.
4. Expressions create and process objects.

'''

#the plus sign (+) means different things for different objects: addition for numbers, and concatenation for strings. 
#This is a general property of Python that we’ll call polymorphism.

'''
1. Name four of Python’s core data types.
2. Why are they called “core” data types?
3. What is “polymorphism?

1) => List, Tuple, Dictionary, String.
2) => because they are effectively built into the Python language—that is, there is specific expression syntax for 
      generating most of them.
3) => plus sign (+) means different things for different objects: addition for numbers, and concatenation for strings. 
This is a general property of Python that we’ll call polymorphism.
'''
# A “sequence” is a positionally ordered collection of objects. Strings,lists,andtuples are all sequences in Python. 
#They share common sequence operations, such as indexing, concatenation, and slicing, but also have type-specific method calls



'''
The Dynamic Typing
python dynamically assigns data type to varibales.
>>> a = 3
Python does these three things when the above statement is executed.
1. Create an object to represent the value 
2. Create the variable a, if it does not yet exist. 
3. Link the variable a to the new object 3.

Names        reference       object

a             ====>           3



Variable a becomes a reference to the object 3. Internally, the variable is really a pointer to the object’s memory space 
created by running the literal expression 3.

• Variables are entries in a system table, with spaces for links to objects.
• Objects are pieces of allocated memory, with enough space to represent the values
  for which they stand.
• References are automatically followed pointers from variables to objects.

objects have more structure than just enough space to represent their values. Each object also has two standard header fields: a type 
designator used to mark the type of the object, and a reference counter used to determine when it’s OK to reclaim the object.

types are associated with objects in Python, not with variables.

>>> a = 3                                 # It's an integer
>>> a = 'spam'                            # Now it's a string
>>> a = 1.23                              # Now it's a floating point

so 'a' is a variable and it has no data type, so when we assign it to 3, python creates an object with header as "integer" and
value is 3, and creates a reference from variable name 'a' to object '3'. Then when we are assigning it to 'spam', pytohn again
creates another object 'spam' with header as 'string' and references 'a' to 'spam' and so on.

whenever a name is assigned to a new object, the space held by the prior object is reclaimed if it is not referenced by any 
other name or object. This automatic reclamation of objects’ space is known as garbage collection. so the object space '3' gets
reclaimed when 'a' started pointing to 'spam'.
'''

#Shared References
>>> a = 3 
>>> b = a

#variable a and b both will be refering to the same object '3'

>>> a = 'spam'

#another object 'spam' will be created and a will be pointing to that and b will be pointing to '3' only

>>> a = a+2 

#another object '5' will be created and 'a' will be pointing to that


'''
in-place object chage, that is when we have an mutable data type like list, it doesnt always create different object all over.

>>> l1 = [1,2,3]

l1 is referring a collectinon of objects, each object can be pointed out using l1[index], so whenever one element/object is 
getting changed of l1, we just need to create another object and place it in position.
'''

>>> l1 = [1,2,3]
>>> l2 = l1
>>> l2
[1, 2, 3]
>>> l1.append(4)
>>> l1
[1, 2, 3, 4]
>>> l2
[1, 2, 3, 4]

# l2 gets changed as well,

>>> L1 = [2, 3, 4] 
>>> L2 = L1[:]
>>> L1[0] = 24
>>> L1 [24, 3, 4] 
>>> L2
[2, 3, 4]

#here L1 and L2 refers to two different pieces of memory

#there is a way to check whether two variable are pointing to the same piece of memory.

>>> L1 = [2, 3, 4] 
>>> L2 = L1[:]
>>> L2 == L1
True
>>> L2 is L1
False

# this means L2 and L1 are not pointing to the same memory but they are identical.
# copying one object to another

>>> import copy 
>>> X = (1,2,3)
>>> Y = copy.copy(X)
>>> Y
(1, 2, 3)
>>> X is Y
True

'''you can always ask Python how many references there are to an object: the getrefcount function in the standard sys module 
returns the object’s reference count.
'''
>>> import sys 
>>> sys.getrefcount(L1)
2
>>> L3 = L1
>>> sys.getrefcount(L1)
3

# so L1 has been used 3 times

>>> a = 1
>>> b = 1
>>> c = 1
>>> sys.getrefcount(1)
208
>>> d = 1
>>> sys.getrefcount(1)
209

# 1 has been used 209 times 

# dynamic typing is also the root of Python’s polymor- phism







