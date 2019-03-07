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
2) how to run a unix/linux command through a python script?

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







