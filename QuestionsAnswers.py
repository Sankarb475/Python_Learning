1) Adding two dictionary in python :: use update method

==> if you are using Python 2.x :: 

>>> def merge_two_dicts(x, y):
...     z = x.copy()
...     z.update(y) 
...     return z

>>> x
{'a': 1, 'b': 2}
>>> y
{'a': 1, 'c': 11, 'b': 2}

>>> a = merge_two_dicts(x,y)
>>> a
{'a': 1, 'c': 11, 'b': 2}

>>> a = merge_two_dicts(x,{'d':1})
>>> a
{'a': 1, 'b': 2, 'd': 1}

in python 3.5 or greater :: 

>>> x = {'a':1, 'b': 2}
>>> y = {'b':10, 'c': 11}

>>> z = {**x, **y}
>>> z
{'a': 1, 'b': 10, 'c': 11}


==============================================================================================================================
2) how to run a unix/linux command through a python script

==> with the help of this package :: import subprocess

file_name = "file_to_be_copied.txt"
file_path = "file/path"
fileDet = file_path + "/" + file_name
folderPath = "/ngs/app/odsp/AutomationScript/FinalCode/data_archival/getFiles"
shellQuery = """
             cp '{}' '{}'
             """.format(fileDet, folderPath)
subprocess.Popen([shellQuery], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)


if your shell script returns some output and you want to catch it and use it later ::

process = subprocess.Popen([shellQuery], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
output = process.stdout.read()
output1 = output.split("\n")
lines = [line for line in output1 if line.strip()]
out = lines[2:-1]

==============================================================================================================================
3) How to retry a given number of times after exception

==>
tries = 3
for i in range(tries):
    try:
        do_the_thing()
    except KeyError as e:
        if i < tries - 1: # i is zero indexed
            continue
        else:
            raise
    break

we can also use retry package to do it ::
@retry(wait_random_min=1000, wait_random_max=2000)
def wait_random_1_to_2_s():
    print("Randomly wait 1 to 2 seconds between retries")

==============================================================================================================================
4) How sleep works in Python

==> you have to import the package "time".

import time
time.sleep(10) 
==> here 10 is in seconds

==============================================================================================================================
5) what happens if method1 has try-except block but method2 which has been called inside method1 has no try-except block but
the error is getting generated inside method2, will the method1 be able to catch the exception 

==> the answer is yes

def dummy1(a):
    b = 100/a
    return b

def dummy2(a):
   try:
       out = dummy1(a)
       print(out)
   except Exception as e:
       print(e)

output = dummy2(0)

division by zero
Process finished with exit code 0

==============================================================================================================================
6) How to check whether a variable is an integer or not

==> using isinstance(<var>, int)

>>> gm = "Good Morning"
>>> isinstance(gm, str)
True

>>> isinstance(a, int)
True

>>> isinstance(a, float)
False

==============================================================================================================================
7) How to unzip "zip"er list

==> zipped_list is a list of tuples where ith tuple consists of the ith element of all the lists that has been zipped.
you can zip multiple lists.

>>> a = [1,2,3,4,5]
>>> b = [6,7,8,9,10]
>>> c = [1,3,5,7,9]
>>> zipper = zip(a,b,c)

If the length of the iterables are not equal, zip creates the list of tuples of length equal to the smallest iterable.
unzipping :: 
>>> l1, l2, l3 = zip(*zipper)
>>> l1
(1, 2, 3, 4, 5)
>>> l2
(6, 7, 8, 9, 10)
>>> l3
(1, 3, 5, 7, 9)

This zip object is an iterator. Iterators are lazily evaluated.
Lazy evaluation, or call-by-need is an evaluation strategy which delays the evaluation of an expression until its value is 
needed and which also avoids repeated evaluations.

==============================================================================================================================
8) How to check whether a file exists without exception ::

==> using import os.path

# this is for a file
>>> import os.path
>>> os.path.isfile('/Users/saa')
False

# to check whether a directory exists or not 
>>> os.path.isdir('/Users/sankar.biswas')
True

# to check whether it is a link or not 
>>> os.path.islink('https://www.microsoft.com/en-us/learning/')
False

other utilities in os.path ==> os.path.isabs(    os.path.isdir(    os.path.isfile(   os.path.islink(   os.path.ismount(  
  
==============================================================================================================================
9) how to check whether a file has any content or not
                                                                                                    
==> using os.stat
                                                                                                    
>>> os.stat("/Users/sankar.biswas/del/am.txt").st_size == 0
True
>>> os.stat("/Users/sankar.biswas/del/am2").st_size == 0
False                                                                                                    
  
==============================================================================================================================
                                                                                                    
  
  
  
  
  
  
  
  
  
  
  
  
  






  
