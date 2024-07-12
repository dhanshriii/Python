# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:05:25 2023

@author: Lenovo
"""

#write  python program to create one series
import pandas as pd
ser = pd.Series([2,4,6,8,10])
ser

#########################################

#write a python program to convert a panda module series to a python  list and its type
import pandas as pd
ser = pd.Series([2,4,6,8,10])
print("pandas series and types")
print(ser)
print(type(ser))
print("convert pandas series to python list:")
print(ser.tolist())  #Converts series to list 
print(type(ser.tolist()))

############################################

#write a pandas program to add, substract,multiply and divide
#sample series: [2,4,6,8,10] , [1,3,5,7,9]
ser1 = pd.Series([2,4,6,8,10])
ser2 = pd.Series([1,3,5,7,9])
ser = ser1 + ser2
print("Addition of two series:")
ser
ser = ser1 - ser2
print("Substraction of two series:")
ser
ser = ser1 * ser2
print("Multiplication of two series:")
ser 
ser = ser1 / ser2
print("Division of series is:")
ser

##############################################

#Write a python program to compare the elements of the series
#sample series:  [2,4,6,8,10] , [1,3,5,7,9]
import pandas as pd
ser1 = pd.Series([2,4,6,8,10])
ser2 = pd.Series([1,3,5,7,9])
print("series1: ")
print(ser1)
print("Series2: ")
print(ser2)
print("Compare the elements of said series: ")
print("Equals")
print(ser1 == ser2)
print("Greater then: ")
print(ser1 > ser2)
print("Less then: ")
print(ser1 < ser2)

###########################################

#write a pandas program to convert a dictionary to a pandas series
#Original dictionary : {'a' : 100,'b':200,'c':300,'d':400,'e':800}
import pandas as pd
dic1 = {'a' : 100,'b':200,'c':300,'d':400,'e':800} #the keys act as index of the series element
print("Original dictionary:")
print(dic1)
ser_dic = pd.Series(dic1)
print("New series:")
print(ser_dic)

###############################################################

#write a pandaa program to convert numpy array to pandas series
import numpy as np
import pandas as pd
n_p = np.array([10,20,30,40,50])
print("Numpy array: ")
n_p
ser_np = pd.Series(n_p)
print("Converted series: ")
ser_np

#######################################################

#write a pandas program to change the data types of given a column or a series
import pandas as pd
s1 = pd.Series(['100','200','python','300.5','400'])
print("Original data series")
s1 
s1.dtypes
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1,errors='coerce')
s2
s2.dtypes
####################################################

#write a pandas program to convert the first column of a dataframe as a series
import pandas as pd
d = {
     'col1': [1,2,3,4,5],
     'col2': [6,7,8,9,10],
     'col3': [11,12,13,14,15]
     }
df = pd.DataFrame(data=d)
print("Original dataframe")
print(df)
s1 = df.iloc[:,0]
print("First column as series:")
s1

##############################################################

#stacking of series /list
#using stack() whoch is present in pandas module
#it is used to stack the prescribed levels from columns to index
#returns a reshaped dataframe or series having multi-level index 

import pandas as pd
s = pd.Series([
    ['Red','Green','White'],
    ['Red','Black'],
    ['Yellow']
    ])
print("original series of list: ")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True) #this converts the set of series in a single series
print("One series")
print(s)
#the similar code can also be written as
s = s.apply(pd.Series)
s
s1 = s.stack()
s1
s2 = s1.reset_index(drop=True)
s2
 
############################################3

#sort the series
import pandas as pd
s = pd.Series(['300.5','200','python','100','400'])
print("Original data series: ")
print(s)
new_s = pd.Series(s).sort_values() #will sort the values of series in accending order
print(new_s)

#Write a pandas program to add some data to an existing series
import pandas as pd
s = pd.Series(['100','200','python','300.5','400'])
print("Original data series: ")
print(s)
print("Data series after adding some data: ")
new_s = pd.concat([s,pd.Series([500,'php'])],ignore_index=True) #will add the elements in the series
print(new_s)

###############################################

#write a pandas program to change the order of index of given series
#to rearrange the index of the series with it values use reindex()
import pandas as pd
s = pd.Series(data=[1,2,3,4,5],index = ['A','B','C','D','E'])
print("Original data series: ")
print(s)
s = s.reindex(index = ['B','A','C','D','E']) #will the change the sequence of the series according to this index
print("Data series after changeing the index of the series: ")
print(s)

#####################################################
















