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








