'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
'''

def is_isogram(a) :
    b = set(list(a.lower()))
    if(len(b) == len(a)):
        return True
    return False


print(is_isogram("PujaA"))
