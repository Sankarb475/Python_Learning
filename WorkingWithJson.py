# working and playing with JSON file 

>>> import json
>>> json1_file = open('jsonFile.json')
>>> json1_str = json1_file.read()

>>> type(json1_str)
<class 'str'>

>>> json1_data = json.loads(json1_str)
>>> type(json1_data)
<class 'dict'>

 # json1_data is a dictionary, and if your dictionary keys are storing dictionary value, it will be a dictioanry of dictionary
 # based on my input data, my json1_data is a dictionary of dictionary of a list.


