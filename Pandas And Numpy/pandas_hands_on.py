Pandas series data structure
======================================================================================================================================
- one dimensional labeled array object (No column headers)
>>> c = pd.Series([1,2,3])
>>>
>>> c
0    1
1    2
2    3
dtype: int64
>>>
>>> c
0    1
1    2
2    3
dtype: int64
>>>
>>> c = pd.Series((1,2,3))
>>> c
0    1
1    2
2    3
dtype: int64

>>> numpy.array
<built-in function array>

>>> c = pd.Series({1:2})
>>> c
1    2
dtype: int64

We can define the row indexes as well
==============================================
>>> a = pd.Series({1:5,2:10,5:47,6:40,9:13})
>>> a
1     5
2    10
5    47
6    40
9    13
dtype: int64

We can select rows based on some indexes
=============================================
>>> a[[1,5]]
1     5
5    47
dtype: int64

>>> b = [1,5,9]
>>> a[b]
1     5
5    47
9    13
dtype: int64

Modifying/updating

Pandas series object can be processed as a dictionary
=====================================================
>>> obj = a = pd.Series([12,34], index = ['a','b'])
>>> 'a' in obj
True
>>> 'e' in obj
False

-- we can convert a python dictionary easily to a pandas series object
>>> dic = {'Ram':'Shyam', 'Jodu':'Modhu'}
>>> a = pd.Series(dic)
>>> a
Ram     Shyam
Jodu    Modhu
dtype: object

-- and the vice versa is also true
>>> back = dict(a)
>>> back
{'Ram': 'Shyam', 'Jodu': 'Modhu'}

-- checking whether the series object has any NaN/null values
using pandas "isnull" and ""notnull" method
>>> a = [1,2, float('NaN')]
>>>
>>> a
[1, 2, nan]
>>>
>>> pd.isnull(pd.Series(a))
0    False
1    False
2     True
dtype: bool
  
>>> pd.notnull(b)
0     True
1     True
2    False
dtype: bool

-- using series's notnull method
>>> b = pd.Series(a)
>>> b
0    1.0
1    2.0
2    NaN
dtype: float64
>>>
>>> b.notnull()
0     True
1     True
2    False
dtype: bool
  
-- adding up two series - will add based on the indexes of the objects (this is more like joining the series objects
where the joining the column is the index)
>>> obj1 = pd.Series([10,20,30], index = ['Utah', 'Ohio', 'Kentucky'])
>>> obj1
Utah        10
Ohio        20
Kentucky    30
dtype: int64
>>>
>>> obj2 = pd.Series([13,43,57], index = ['Utah', 'NYC', 'Ohio'])
>>> obj2
Utah    13
NYC     43
Ohio    57
dtype: int64
>>>
>>> obj1 + obj2
Kentucky     NaN
NYC          NaN
Ohio        77.0
Utah        23.0
dtype: float64

-- we can name the series index and the values

>>> obj3
Kentucky     NaN
NYC          NaN
Ohio        77.0
Utah        23.0
dtype: float64
>>> obj3.index.name = "States"
>>> obj3.name = 'Vals'
>>>
>>> obj3
States
Kentucky     NaN
NYC          NaN
Ohio        77.0
Utah        23.0
Name: Vals, dtype: float64
    
-- renaming the indexes
>>> obj3.index = ['K','N','O','U']
>>>
>>> obj3
K     NaN
N     NaN
O    77.0
U    23.0
Name: Vals, dtype: float64

Pandas DataFrame data structure
================================================================================================================================
>>> a = pd.DataFrame({'Name':['Puja', 'Sankar'], 'ID':[1,2], 'Salary':[10,20]})
>>> a
     Name  ID  Salary
0    Puja   1      10
1  Sankar   2      20

# head returns the top 5 rows in a dataframe
>>> a.head
<bound method NDFrame.head of      Name  ID  Salary Newname
0    Puja   1      10    Puja
1  Sankar   2      20  Sankar

>>> a.columns
Index(['Name', 'ID', 'Salary'], dtype='object')

>>> a.index
RangeIndex(start=0, stop=2, step=1)

# if you use one square bracket to select a column, you would get a series object while double will return a dataframe
>>> b = a['Name']
>>> b
0      Puja
1    Sankar
Name: Name, dtype: object
>>> type(b)
<class 'pandas.core.series.Series'>
>>>
>>> b = a[['Name']]
>>> b
     Name
0    Puja
1  Sankar
>>> type(b)
<class 'pandas.core.frame.DataFrame'>
>>> b = a.Name
>>> b
0      Puja
1    Sankar
Name: Name, dtype: object
>>> type(b)
<class 'pandas.core.series.Series'>
>>>
>>> a['Newname'] = a.Name
>>> a
     Name  ID  Salary Newname
0    Puja   1      10    Puja
1  Sankar   2      20  Sankar
>>>
>>> a.Name.tolist()
['Puja', 'Sankar']
 
-- deleting a column from a dataframe
>>> del frame3['pop']
>>> frame3
    state  year
0    Ohio  2000
1    Ohio  2001
2    Ohio  2002
3  Nevada  2001
4  Nevada  2002
5  Nevada  2003

>>> frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four','five', 'six'])
>>> frame2
       year   state  pop debt
one    2000    Ohio  1.5  NaN
two    2001    Ohio  1.7  NaN
three  2002    Ohio  3.6  NaN
four   2001  Nevada  2.4  NaN
five   2002  Nevada  2.9  NaN
six    2003  Nevada  3.2  NaN
>>>

-- .loc returns a series object containing rows of data (not columns)
>>> frame2.loc['three']
year     2002
state    Ohio
pop       3.6
debt      NaN
Name: three, dtype: object
>>> type(frame2.loc['three'])
<class 'pandas.core.series.Series'>

>>> frame2.loc['three'].tolist()
[2002, 'Ohio', 3.6, nan]

-- if we convert a python dataframe to a python dictionary using dict()
we will get a dictionary, the values of which will be series objects containing each column values and the keys will be the column 
names.
>>> dic = dict(frame)
>>> dic
{'state': 0      Ohio
1      Ohio
2      Ohio
3    Nevada
4    Nevada
5    Nevada
Name: state, dtype: object, 'year': 0    2000
1    2001
2    2002
3    2001
4    2002
5    2003
Name: year, dtype: int64}
>>> dic.keys()
dict_keys(['state', 'year'])

*** loc and iloc => they enable you to select a subset of the rows and columns from a dataframe
