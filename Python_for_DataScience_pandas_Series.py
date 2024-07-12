# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:11:03 2023 

@author: Lenovo 
"""               

#python for data science
#libraries which we are going to study are :
#Pandas : used to work with rows and cols in a file(data frame)
#Matplotlib : used for ploting graphs
#Numpy : Array and ndarray (Numpy stands for : Numerical python)
#Seaborn : similar to matplotlib (used for visualisation) but with more efficient methods 

#Series
#Series is used to model one dimensional data
#it is similar to list in python
#The series also have some more bits of data ,including index and a name that is not there in list
#firstly import pandas
import pandas as pd
song2 = pd.Series([145,142,38,13],name = 'counts')
#it easy to inspect the index of a series
song2.index 
#this index can be string based as well,in which case pandas indicate that the datatype for the index is object(not string)
songs3 = pd.Series([145,142,38,19],name = 'count',index = ['paul','john','george','ringo'])
songs3.index #this gives the index and gives the datatype as 'object'
songs3

######################
#NaN value
#this stands for : Not a Number 
#And it is usually ignored in aithmetic operations.(similar to Null in SQL)
#if you load data from CSV file an empty value for an otherwise numeric column will become NaN
import pandas as pd
f1 = pd.read_csv('c:/1-python/age.csv')#We have given the absolute path 
f2 = pd.read_csv('age.csv') #We gave a relative path
f2
f1 
#importing an excel file
import pandas as pd
f4 = pd.read_excel('c:/1-python/Bahaman.xlsx')
f4  
#none,NaN,nan, and null are all synonyms
#the series object behaves similarly to a numpy array
#lets see difference between series and array
import numpy as np
numpy_ser = np.array([145,142,38,12]) 
songs3[1]
#ans will we 142
numpy_ser[1]
#we get similar output
#i.e they both have same methods in common(series and arrays)
songs3.mean()
numpy_ser.mean()

########################################
#panda series data structure provides support for the basic crud
#operations - create,read,update, and delete.
#creation
george = pd.Series([10,7,1,22],index=['1968','1930','1930','1980'],name='George song')
#We can also dublicate index only in series not in list or array
george

#Reading
#to read or select the data from series 
george['1968']
george['1930'] #It gives all the values having this index
#To access all the values or data use for loop
#We can iterate over series also
for item in george:
    print(item)
                                            
#Updating
#we have to use the standard index assignment operation
george['1969'] = 68
george['1969']

#Deletion
#The del statement is appears to have problem with dublicate index
s = pd.Series([2,3,4],index=[1,2,3])
del s[1]
s 

#############################################

#convert types 
#string use .astype(str)
#In summary, .astype(str) will convert the values to strings and 
#the resulting data type will be 'object'.
#numeric use pd.to_numeric
#integer use astype(int),
#note that conversion is not possible for NaN 
#datetime use pd.to_datetime
import pandas as pd
song_66 = pd.Series([3,11,None,9],index=['George','Ringo','john','paul'],name='counts')
song_66.dtypes
#dtype('float64)
pd.to_numeric(song_66.apply(str)) #there will be an error as none element is presenr in series
pd.to_numeric(song_66.apply(str),errors='coerce')#if we pass errors='coerce' we can see that it supports many formats
song_66.dtypes
'''The .apply() function in pandas is a powerful tool that allows 
you to apply a custom function to each element, row, or column of a 
DataFrame or Series. It's used to transform data in a flexible and 
customizable way. You can think of it as a way to "apply" a certain 
operation or function to all the parts of your data.
'''

#dealing with None
#the .fillna method will replace them with a given value
song_66.fillna(-1) #in parenthesis we put the value by which we want to replace by none
#NaN values can be dropped from the series by using .dropna
song_66.dropna()#the none value gets dropped

############################################

#append , combining , and joining two series
import pandas as pd
songs_69 = pd.Series([7,16,21,39],index=['ram','sham','ghansham','krishna'],name='counts')
#to append two series vertically one below other simply use .append()
songs = song_66.append(songs_69) #a different series is formed after there concatination no chnages in the original


####################################################
####################################################
#plotting series
#matplotlib : Module
#matplylib has a sub module pyplot
#lets plot two series 
#plotting line 
import matplotlib.pyplot as plt
fig = plt.figure() 
songs_69.plot()
plt.legend() 
###########################
#plotting graph 
fig = plt.figure()   
songs_69.plot(kind='bar') 
song_66.plot(kind='bar',color = 'r') 
plt.legend()
#plotting histogram
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.Series(np.random.randn(500), name = '500 random') 
fig = plt.figure()
ax = fig.add_subplot(111)
data.hist()
plt.legend()




