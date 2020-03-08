Python Regex
=======================================================================================================================================
import re

1) findall => returns a list of all the matches
================================================
>>> re.findall('Tame', 'Tame is in tame')
['Tame']

>>> re.compile("Tame").findall("Tame is in tame")
['Tame']

>>> x = re.findall("Spain", "Spain has to be in front of Spain, no spain?", re.I)
>>> x
['Spain', 'Spain', 'spain']

multiple keyword search on the string =>
>>> l = ['Spain', 'bow']
>>> r = re.compile('|'.join([i for i in l]), re.I)
>>> r
re.compile('Spain|bow', re.IGNORECASE)
>>> word = "Spain has to bow down"
>>> r.findall(word)
['Spain', 'bow']

2) search => returns a match object if there is a match anywhere in the string
=====================================================================================
Scan through string looking for the first location where the regular expression pattern produces a match
>>> txt = "The rain in Spain"
>>> x = re.search(r"\bS\w+", txt)
>>> print(x.span())
(12, 17)
>>> x.string
'The rain in Spain'
>>> x.gro
x.group(     x.groupdict( x.groups(
>>> x.groups()
()
>>> x
<re.Match object; span=(12, 17), match='Spain'>
>>> x.groups(0)
()

3) match / fullmatch => returns a match object 
==================================================
If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding match object.

>>> re.match("spa", "Spain is spa", flags = re.I)
<re.Match object; span=(0, 3), match='Spa'>
>>>
>>> re.match("spa", "Spain is spa", flags = re.I).group()
'Spa'
>>> re.match("spa", "Spain is spa", flags = re.I).span()

>>> re.fullmatch("spa", "Spain is spa ", flags = re.I)
>>>
>>> re.fullmatch("spa", "spa", flags = re.I)
<re.Match object; span=(0, 3), match='spa'>

>>> m = re.match(r"(\w+) (\w+)(,)(\w+)", "Isaac Newton, physicist")
>>> m
>>> m = re.match(r"(\w+) (\w+)(,) (\w+)", "Isaac Newton, physicist")
>>> m
<re.Match object; span=(0, 23), match='Isaac Newton, physicist'>

4) sub => Replaces one or many matches with a string
=====================================================
>>> re.sub("\W","40", "String 123")
'String40123'

>>> re.sub("[0-9]","", "String 123")
'String '
