1) you have a dataframe like this : 

    Movies            Genre
0     Fari  horror, romance
1    Noida       adv, fight
2    Delhi           horror
3  Gurgaon             love

how will you only take the rows which doesnt have "horror" in it?

==>

>>> df1 = pd.DataFrame({'Movies':['Fari','Noida','Delhi', 'Gurgaon'], 'Genre':["horror, romance", "adv, fight", "horror", "love"]})
>>>
>>> df1
    Movies            Genre
0     Fari  horror, romance
1    Noida       adv, fight
2    Delhi           horror
3  Gurgaon             love

>>> df2 = df1[~df1.Genre.str.contains('horror')]
>>> df2
    Movies Genre
1    Noida   adv
3  Gurgaon  love

=======================================================================================================================================
2) you have a dataframe like this : 
      City  Nums
0     Fari    80
1    Noida    90
2    Delhi    70
3  Gurgaon   100

we want to sort each column without effecting the other column?
==>

-- converting the columns into list and then sorting and putting back to the dataframe
>>> df = pd.DataFrame({'City':['Fari','Noida','Delhi', 'Gurgaon'], 'Nums':[80,90,70,100]})
>>> df
      City  Nums
0     Fari    80
1    Noida    90
2    Delhi    70
3  Gurgaon   100
>>>
>>> list1 = sorted(list(df.City))
>>> list2 = sorted(list(df.Nums))[::-1]
>>>
>>> df = pd.DataFrame({'City':list1, 'Nums':list2})
>>> df
      City  Nums
0    Delhi   100
1     Fari    90
2  Gurgaon    80
3    Noida    70

>>> df['City'] = sorted(df['City'].tolist())
>>> df['Nums'] = sorted(df['Nums'].tolist())[::-1]
>>> df
      City  Nums
0    Delhi   100
1     Fari    90
2  Gurgaon    80
3    Noida    70

-- using sort_values() function

>>> df['City'] = df['City'].sort_values().values
>>> df
      City  Nums
0    Delhi    80
1     Fari    90
2  Gurgaon    70
3    Noida   100
>>> df['Nums'] = df['Nums'].sort_values(ascending = False).values
>>> df
      City  Nums
0    Delhi   100
1     Fari    90
2  Gurgaon    80
3    Noida    70
