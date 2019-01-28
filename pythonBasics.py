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








