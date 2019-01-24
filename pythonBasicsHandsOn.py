'''to run python in command prompt, use "python", (windows :considering you have set up environment variable)
The interactive prompt runs code and echoes results as you go, but it doesn’t save your code in a file
'''

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
