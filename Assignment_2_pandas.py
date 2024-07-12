# -*- coding: utf-8 -*-                                               
"""
Created on Thu Aug  3 16:03:49 2023

@author: Lenovo
"""

import pandas as pd
df = pd.read_csv('loan.csv')
df = pd.read_csv('c:/2-dataset/loan.csv')
df
print(df.dtypes)
data_frame = pd.DataFrame(df)
#########
df2 = data_frame.convert_dtypes() #should convert into string
print(df2.dtypes)
########
df2 = data_frame.astype(str)
df2
cols = ['id','member_id']
df2[cols] = df2[cols].astype(float)
###########
data_frame.shape #gives the number of rows and columns(row,col)
data_frame.size  #gives the num of boxes or product or rows and columns
data_frame.columns  #gives the names of the columns
data_frame.columns.values #gives the names
data_frame.index  #gives the index of the rows (gives the index range)
data_frame.dtypes  #gives the datatype of the entities
data_frame.convert_dtypes()
data_frame.dtypes
###############
df = df.astype({'funded_amnt_inv':int},errors='raise')    
df.dtypes       
###############
df['funded_amnt_inv'] #imports the data from the column 'funded_amnt_inv'
#accessing data from two or more columns 
df[['funded_amnt_inv','id']]
###############
df2 = df[:4]
df2
################
df['id'][3] #accessing certain cell data
#############
df['id'] = df['id'] - 200 #substracting some value 
df['id']
##############
df.describe
##########
#changing column name
df.rename({'id':'A','member_id':'B'},axis=1)
###########
df2 = df.loc[:,['id']]
df2
df2 = df.loc[:,:]
df2
df2 = df.loc[:,['id','member_id']]
df2
df2 = df.loc[[1,2,3]]
df2
df2 = df.loc[1:5] #rows from 1 to 5 will be displayed
df2
df2 = df.loc[1:5:2] #1 to 5 rows with step of 2
df2
#dataframe to series (first column)
s = df.iloc[:,0]
s
df2 = df.iloc[[2,3,5]] #select rows by index list (gives all columns and this specified index rows)
df2
df2 = df.iloc[1:5]
df2
df2 = df.iloc[:1]
df2
df2 = df.iloc[:3]
df2
df2 = df.iloc[-1:]
df2
df2 = df.iloc[-3:]
df2
df2 = df.iloc[::2]
df2
df2 = df.iloc[1:2,1:3]
df2

########################################################################
########################################################################

#doing operations on another csv file

import pandas as pd
data_frame = pd.read_csv('bank_data.csv')
data_frame
print(data_frame.dtypes)
df = data_frame.convert_dtypes() #converts into best possible data type
print(df.dtypes)
######
df = data_frame.astype(str) #converts all data into object
df.dtypes
##########
#converting specific items datatype
df = data_frame.astype({'age':'string','default':'float'})
df.dtypes
cols = ['balance','loan']
data_frame[cols] = data_frame[cols].astype('double')
data_frame.dtypes
############
#generate errors and ignore errors
df = df.astype({'loan':str}, errors = 'ignore')
df.dtypes
df = df.astype({'loan':str}, errors = 'raise')
df.dtypes 
print(df.convert_dtypes())
print(df.dtypes)
###############
row_labels = [i for i in range(1,45212)]
df = pd.DataFrame(df,index=row_labels)
print(df)
df.shape #gives the number of rows and columns(row,col)
df.size  #gives the num of boxes or product or rows and columns
df.columns  #gives the names of the columns
df.columns.values #gives the names
df.index  #gives the index of the rows
df.dtypes  #gives the datatype of the entities
df.info #gives the information
#these are all the properties
df.describe()
#accessing specific column
df['default']
df[['age','default']] #When accessing two or more coulumns use double square brakets
df2 = df[:4]
df2
########
df.rename({'age':'A','default':'B'},axis=1)
#######
df2 = df.drop([0,1]) #0 and 1 gets removed / dropped
df2
##
df1 = df.drop(df.index[[1,5]]) #but if want to delete two or more rows using index use double square brackets
df1
##
df1 = df.drop(df.index[1:50]) #Rows from 2 index gets deleted till (5-1) i.e 4th row 
df1
##
df1 = df.drop([0,3]) #0th and 3rd row gets deleted. we can aslo give axis = 0 over here 
df1
##
df1 = df.drop(range(0,3)) #row from 0th index to 2nd index gets deleted
df1
######
#deleting columns
df1 = df.drop(['age'],axis=1,inplace=True)
df1
###
#ioc
df2 = df.loc[:,['default']]
df2
df2 = df.loc[:,:]
df2
df2 = df.loc[:,['age','default']]
df2
df2 = df.loc[[1,2,3]]
df2
df2 = df.loc[1:5] #rows from 1 to 5 will be displayed
df2
df2 = df.loc[1:5:2] #1 to 5 rows with step of 2
df2

###
df2 = df.iloc[[2,3,5]] #select rows by index list (gives all columns and this specified index rows)
df2
df2 = df.iloc[1:5]
df2
df2 = df.iloc[:1]
df2
df2 = df.iloc[:3]
df2
df2 = df.iloc[-1:]
df2
df2 = df.iloc[-3:]
df2
df2 = df.iloc[::2]
df2
df2 = df.iloc[1:2,1:3]
df2
#########################################################################
#########################################################################

import pandas as pd
df = pd.read_csv('crime_data.csv')
df
df.dtypes
df2 = df.convert_dtypes()
df2.dtypes
print(df.astype(str).dtypes)
df = df2.astype({'Assault':float})
df.dtypes
cols = ['Murder','Assault']
df[cols] = df[cols].astype('double')
df.dtypes
############
#generate errors and ignore errors
df = df.astype({'Murder':str}, errors = 'ignore')
df.dtypes
df = df.astype({'Assault':str}, errors = 'raise')
df.dtypes
print(df.convert_dtypes())
print(df.dtypes)
###############

df.shape #gives the number of rows and columns(row,col)
df.size  #gives the num of boxes or product or rows and columns
df.columns  #gives the names of the columns
df.columns.values #gives the names
df.index  #gives the index of the rows
df.dtypes  #gives the datatype of the entities
df.info #gives the information
#these are all the properties
df.describe()
#accessing specific column
df['Murder']
df[['Murder','Rape']] #When accessing two or more coulumns use double square brakets
df2 = df[:4]
df2
########
df.rename({'Murder':'A','UrbanPop':'B'},axis=1)
#######
df2 = df.drop([0,1]) #0 and 1 gets removed / dropped
df2
##
df1 = df.drop(df.index[[1,5]]) #but if want to delete two or more rows using index use double square brackets
df1
##
df1 = df.drop(df.index[1:50]) #Rows from 2 index gets deleted till (5-1) i.e 4th row 
  
##
df1 = df.drop([0,3]) #0th and 3rd row gets deleted. we can aslo give axis = 0 over here 
df1
##
df1 = df.drop(range(0,3)) #row from 0th index to 2nd index gets deleted
df1
######
#deleting columns
df1 = df.drop(['age'],axis=1,inplace=True)
df1
###
#ioc
df2 = df.loc[:,['Murder']]
df2
df2 = df.loc[:,['Assault','UrbanPop']]
df2
df2 = df.loc[:,:]
df2
###
df2 = df.iloc[[2,3,5]] #select rows by index list (gives all columns and this specified index rows)
df2
df2 = df.iloc[1:5]
df2
df2 = df.iloc[:1]
df2
df2 = df.iloc[:3]
df2
df2 = df.iloc[-1:]
df2
df2 = df.iloc[-3:]
df2
df2 = df.iloc[::2]
df2
df2 = df.iloc[1:2,1:3]
df2


##########################################################################3
##########################################################################
##########################################################################


#All pandas operations on dataframes
import pandas as pd
import numpy as np
df = pd.read_csv('Seeds_data.csv') #Converting csv file to Dataframe
df
df = pd.DataFrame(df) #Converting csv file to Dataframe
df
#Pandas Queries
df2 = df.query("Area == 15.26")  #ONly rows having area = 15.26 will be displayed
df2
#####
df2 = df.query("Area != 15.26") #Rows exept area = 15.26 will be displayes
df2
##########################
#adding column to the dataframe
numbers = [i for i in range(1,211)]
df2 = df.assign(Numbers=numbers)
df2
###########
#Adding column to the specific position
df.insert(0,'Num',numbers) # Num will be inserted to the zeroth position column
df
##########
df2 = df.assign(Area_meter = lambda x:x.Area*100)
df2
##########
#finding number of rows and columns
row_count = len(df.axes[0])
print("The number of rows in the given dataframe are: " +str(row_count))
column_count = len(df.axes[1])
print("The number of columns in the given dataframe are :" +str(column_count))
#############
#Other operations to be performed
#chnaging datatypes
print(df.dtypes)
df2 = df.convert_dtypes()
df2.dtypes
df2 = df.astype(str) #converts all data into object
df2.dtypes
df2 = df2.convert_dtypes() #converts object into string
df2.dtypes
#chnaging indivitual data type
df2 =df.apply(pd.to_numeric)
df2.dtypes
##############
df.shape #gives the number of rows and columns(row,col)
df.size  #gives the num of boxes or product or rows and columns
df.columns  #gives the names of the columns
df.columns.values #gives the names
df.index  #gives the index of the rows
df.dtypes  #gives the datatype of the entities
df.info #gives the information
#these are all the properties so no need of parenthesis()
df.describe()
#############################
#accessing elements 
df['length'] #this columns will be displayed
df[['Num','Area']]
df2 = df[:3]  #0 to # index rows will be displayed excluding 3
df2
df2 = df[3:5] #3 to 5 rows will be displayed excluding 5
df2
df['Area'][5] #asseccing specific elements/cell
#Substracting or adding some values to the existing value of the column
df['Area'] = df['Area'] - 20
df
df['Area'] = df['Area'] + 30
df
#Renaming
#Renaming column names
df.columns=['NUM','AREA','PERIMETER','COMPACTNESS','LENGTH','WIDTH','ASSYMETRY_COEFF','LEN_KER_GROVE','TYPE']
df
#we can also use rename() function
df2 = df.rename({'NUM':'A','AREA':'B'},axis=1) #axis=1 is mandatory to be written
df2
#######################

#Deleting/dropping items from the dataframe
#using drop method
#deleting rows
df2 = df.drop([1])
df2
df1 = df.drop(df.index[[1,3]]) #but if want to delete two or more rows using index use double square brackets
df1
#Delete rows by index range
df1 = df.drop(df.index[2:5]) #Rows from 2 index gets deleted till (5-1) i.e 4th row 
df1
#When you have default indexs for rows
df = pd.DataFrame(df)
df1 = df.drop(0) #0th index row will get deleted
df1
#deleting more rows using indexing
df = pd.DataFrame(df)
df1 = df.drop([0,3]) #0th and 3rd row gets deleted. we can aslo give axis = 0 over here 
df1
df = pd.DataFrame(df)
df1 = df.drop(range(0,3)) #row from 0th index to 2nd index gets deleted
df1
############
#deleting columns
df2 = df.drop(['Fee'],axis = 1) #fees column gets deleted
df2
#We can aslo delete explicitly using parameter name 'lable'
df2 = df.drop(labels = ['Fee'],axis = 1) #fees column gets deleted
df2
#Alternatively you can also use columns instead of labels
df2 = df.drop(columns = ['Fee'],axis = 1) #fees column gets deleted
df2
#dropping column by index
print(df.drop(df.columns[3],axis=1)) #will delete 3rd index number column if started from 0
#############
#when working on original dataframe and you want to make changes in it use (inplace=True)
#When deleting rows or columns of original detaframe use this
df.drop(df.columns[3],axis=1,inplace=True)
df
df2 = df.drop(df.columns[[0,1]],axis = 1) #0th and 1st index position columns get deleted
df2
liscol = ['PERIMETER','LENGTH'] 
df2 = df.drop(liscol,axis=1) #this colums get deleted 
df2
######################

#loc and iloc
#used to access specific columns and rows 
#loc: need row_lables and column names
#iloc: need index
df3 = df.iloc[1:2,1:3]
df3
df2 = df.iloc[2] #select row by index (gives series)
df2
df2 = df.iloc[[2,3,5]] #select rows by index list (gives all columns and this specified index rows)
df2
df2 = df.iloc[1:5] #select rows by integer index range
df2
df2 = df.iloc[:1] #select first row
df2
df2 = df.iloc[:3] #select 3 rows (rows from 0th index to 3 (excluding 3) will be displayed)
df2
df2 = df.iloc[-1:] #select last row
df2
df2 = df.iloc[-3:] #select last 3 row
df2
df2 = df.iloc[::2] #select alternate rows 
df2
#################33

df2 = df.loc[1] #gives series
df2
df2 = df.loc[5] #select row by label(gives the series)
df2
df2 = df.loc[[6,7,8]] #select multiple rows using labels
df2
df2 = df.loc[50:100] #select rows by label in this range from r1 to r5(including r5)
df2
df2 = df.loc[30:100:2] #select alternate rows 
df2

df2 = df.loc[:,['LENGTH','TYPE','WIDTH']] #Only these columns gets displayed
df2
df2 = df.loc[:,'PERIMETER':'TYPE'] #columns from fees to discount will be displayed including Discount
df2
df2 = df.loc[:,'WIDTH'] #Only Duration will be displayed
df2

##########################################################################
#####################################################################
######################################################################
'''
      All operations on a csv file by importing it to a dataframe

'''
import pandas as pd
df = pd.read_csv('iris.csv') #accessing using relative path
df
df = pd.read_csv('c:/2-dataset/iris.csv') #accessing using absolute path
df
############
#Converting datatypes within the dataframe
df.dtypes
df2 = df.convert_dtypes() #converts object into string
df2.dtypes
#Converting all data items into object
df2 = df.astype(str)
df2.dtypes
#changing data type of indivitual column
df2 = df2.astype({'Id':float,'SepalLengthCm':int},errors='ignore')
df2.dtypes
################
#basic operations on dataframes
#giving row lables starting from 1
row_lables = [i for i in range(1,151)]
df = pd.DataFrame(df,index = row_lables)
df
###################
df.shape #gives number of rows and columns
df.columns #Gives the names of the rows
df.columns.values #gives the names of the columns in the form of array
df.info #gives the information of dataframe
df.index #gives all index of the dataframe
df.dtypes #gives all the datatypes of the columns 
df.size #Gives the product of numer of rows and columns that is number of boxes present in the dataframe
################3
#accessing columns 
df['Id'] #gives the series
#accessing multiple columns 
#use '[[]]'
df[['Id','SepalLengthCm']] #this columns will be accessed 
#accessing certain rows or columns and accesing it to another dataframe
df2 = df[:3] #rows from 0 to 2 index will be displayed
df2
#accessing specific cell
df['Id'][3] #first column and then row mandetorily
######################3
#renaming columns
#use rename()
df2 = df.rename({'Id':'ID','SepalLengthCm':'LENGTH_CM'},axis=1) #compulsorily write axis =1
df2
#Deleting/dropping items from the dataframe
#using drop method
#deleting rows
df2 = df.drop([1])
df2
df1 = df.drop(df.index[[1,3]]) #but if want to delete two or more rows using index use double square brackets
df1
#Delete rows by index range
df1 = df.drop(df.index[2:5]) #Rows from 2 index gets deleted till (5-1) i.e 4th row 
df1
#When you have default indexs for rows
df = pd.DataFrame(df)
df1 = df.drop(0) #0th index row will get deleted
df1
#deleting more rows using indexing
df = pd.DataFrame(df)
df1 = df.drop([0,3]) #0th and 3rd row gets deleted. we can aslo give axis = 0 over here 
df1
df = pd.DataFrame(df)
df1 = df.drop(range(0,3)) #row from 0th index to 2nd index gets deleted
df1
############
#deleting columns
df2 = df.drop(['Id'],axis = 1) #fees column gets deleted 
df2
#We can aslo delete explicitly using parameter name 'lable'
df2 = df.drop(labels = ['Id'],axis = 1) #fees column gets deleted
df2
#Alternatively you can also use columns instead of labels
df2 = df.drop(columns = ['Id'],axis = 1) #fees column gets deleted
df2
#dropping column by index
print(df.drop(df.columns[3],axis=1)) #will delete 3rd index number column if started from 0
#############
#when working on original dataframe and you want to make changes in it use (inplace=True)
#When deleting rows or columns of original detaframe use this
df.drop(df.columns[3],axis=1,inplace=True)
df
df2 = df.drop(df.columns[[0,1]],axis = 1) #0th and 1st index position columns get deleted
df2
liscol = ['Id','SepalLengthCm'] 
df2 = df.drop(liscol,axis=1) #this colums get deleted 
df2
######################

#loc and iloc
#used to access specific columns and rows 
#loc: need row_lables and column names
#iloc: need index
df3 = df.iloc[1:2,1:3] #this specific rows and columns get printed
df3
df2 = df.iloc[2] #select row by index (gives series)
df2
df2 = df.iloc[[2,3,5]] #select rows by index list (gives all columns and this specified index rows)
df2
df2 = df.iloc[1:5] #select rows by integer index range
df2
df2 = df.iloc[:1] #select first row
df2
df2 = df.iloc[:3] #select 3 rows (rows from 0th index to 3 (excluding 3) will be displayed)
df2
df2 = df.iloc[-1:] #select last row
df2
df2 = df.iloc[-3:] #select last 3 row
df2
df2 = df.iloc[::2] #select alternate rows 
df2
#################

df2 = df.loc[1] #gives series
df2
df2 = df.loc[5] #select row by label(gives the series)
df2
df2 = df.loc[[6,7,8]] #select multiple rows using labels
df2
df2 = df.loc[50:100] #select rows by label in this range from r1 to r5(including r5)
df2
df2 = df.loc[30:100:2] #select alternate rows 
df2 

df2 = df.loc[:,['Id','SepalLengthCm','SepalWidthCm']] #Only these columns gets displayed
df2
df2 = df.loc[:,'SepalLengthCm':'Species'] #columns from SepalLengthCm to Species will be displayed including Discount
df2
df2 = df.loc[:,'SepalLengthCm'] #Only SepalLengthCm will be displayed
df2

#Pandas Queries
df2 = df.query("SepalLengthCm == 5.1")  #ONly rows having SepalLengthCm = 5.1 will be displayed
df2
#####
df2 = df.query("SepalLengthCm != 5.1") #Rows exept SepalLengthCm = 5.1  will be displayes
df2
##########################
#adding column to the dataframe
numbers = [i for i in range(1,211)]
df2 = df.assign(Numbers=numbers)
df2
###########
#Adding column to the specific position
df.insert(0,'Num',numbers) # Num will be inserted to the zeroth position column
df
##########
df2 = df.assign(Area_meter = lambda x:x.Area*100)
df2
##########
#finding number of rows and columns
row_count = len(df.axes[0])
print("The number of rows in the given dataframe are: " +str(row_count))
column_count = len(df.axes[1])
print("The number of columns in the given dataframe are :" +str(column_count))
#############
#putting condition while printing 
print(df[df['Id']<20])
df2 = df.loc[df.SepalLengthCm < 5]
df2
df2 = df[df['SepalLengthCm'].isnull()]
df2
#################
df2 = df[df['Id'].between(15, 20)]
df2
#####Appending new row
df.loc['K'] = [8, 45, 2, 4,6,7]
df
########################
#adding column to the dataframe
color = [i for i in range(1,151)]
df['color'] = color #this column gets added to the dtataframe
df
########################
#itering over rows
for index,row in df.iterrows():
    print(row['Id'],row['SepalLengthCm'])
##################
#Replacing any value
df['Id'] = df['Id'].replace(1,10) #1 gets replaced by 10
df
#################
#using map()
df['PetalWidthCm'] = df['PetalWidthCm'].map({0.2:10})
df #All the 0.2 values in PetalWidthCm gets replaced by 10
####################
#using groupby
df2 = df.groupby('Id').sum()
df2
df2 = df.groupby('Id').sum().reset_index()
df2
######################
#taking square of all the elements in that specific column
df['Id'] = np.square(df['Id'])
df['Id'] 
######################

df.dtypes
df2 = df.astype({'Species':float})
df2.dtypes
df2 = df.drop(['Species'],axis = 1)
df2
############################
#adding 2 to all  the elements in the columns and rows
def add_2(x):
    return x+2
df2 = df2.transform(add_2)   
df2
###########################
df2 = df2.apply(lambda x:x+3) #3 gets added to all the columns
df2
###############################





