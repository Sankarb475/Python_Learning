'''
Python provides two built-in functions to read a line of text from standard input, which by default comes from the keyboard. 
These functions are −

1) raw_input
2) input
'''

#The raw_input([prompt]) function reads one line from standard input and returns it as a string (removing the trailing newline).
# raw_input doesnt work after Python 3.0

>>> str = raw_input("Enter your input: ");
>>> print "Received input is : ", str

#input([prompt]) function is equivalent to raw_input, except that it assumes the input is a valid Python expression and 
#returns the evaluated result to you before python 3.0
#after python 3.0 raw_input has been renamed to input()

#writing something to a file

>>> dataFile = open('/Users/sankar.biswas/Desktop/data.txt', 'w')
>>> dataFile.write("I am in Love")
12
>>> dataFile.close()

#reading and printing a file
>>> reading = open('/Users/sankar.biswas/Desktop/data.txt', 'r')
>>> data = reading.read()
>>> print(data)
I am in Love
>>> data.split(' ')
['I', 'am', 'in', 'Love']





