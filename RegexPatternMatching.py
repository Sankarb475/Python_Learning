# removing multiple spaces from a sentence in python.

>>> import re
>>> re.sub(' +', ' ', 'The     quick brown    fox')
'The quick brown fox'
