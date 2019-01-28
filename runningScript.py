#different ways we can run our code saved in a script
cat script1.py
a = 2
b = 2**10
print(b)

#1st way - from command line
python script1.py 
1024

#2nd Way 
>>> import script1
1024

#3rd way
>>> from script1 import b
>>> b
1024

#4th way
>>> exec(open('script1.py').read())
1024
