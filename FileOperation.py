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

#File reading and writing 

'''
Before you can read or write a file, you have to open it using Python's built-in open() function. This function creates 
a file object, which would be utilized to call other support methods associated with it.
'''

file object = open(file_name [, access_mode][, buffering])

'''
where file_name = The file_name argument is a string value that contains the name of the file that you want to access, it 
                  includes path as well
                  
access_mode = The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc.

buffering = If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is 
performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action 
is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).

'''

#Different access mode :::

# r => Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.


# rb => Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
       

# r+ => Opens a file for both reading and writing. The file pointer placed at the beginning of the file.


# rb+ => Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.


# w => Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.


# wb => Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.


# w+ => Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.


# wb+ => Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

	
# a => Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

	
# ab => Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

	
# a+ => Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

	
# ab+ => Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.










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





