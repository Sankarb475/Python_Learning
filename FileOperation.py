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



