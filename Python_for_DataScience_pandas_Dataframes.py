# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 09:14:25 2023

@author: Lenovo
"""

#Pandas dataframes
#pandas dataframe is two dimentional data structure,heterogenous tabular
#firstly upgrade pandas to latest version

#to check the version of pandas on spyder
import pandas as pd
pd.__version__

########################################

#create dataframe from list
import pandas as pd
technologies = [['spark',20000,'30days'],['pandas',20000,'30days']]
df = pd.DataFrame(technologies)
df
#we can see that we have not given names and indexes to column and rows so datsaframes by default assigns that
#incremental sequence numbers as labels to both rows and columns,these are called index

#how to add column and rows lables to the dataframes
column_names = ['courses','fees','duration']
row_lable = ['a','b'] 
df = pd.DataFrame(technologies,columns=column_names,index=row_lable)     
df
#######
df.dtypes #used to check the data types of the entities in the DataFrame

#########################################################

#creating dataframes using dictionaries
#you can assign custom datatypes to columns
#set custom types to Dataframes
#very common technique to create data sets
import pandas as pd
technologies = {
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,21000,20000,230000],
    'Duration':['30days','35days','40days','30days','50days','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]}
df = pd.DataFrame(technologies,index=[1,2,3,4,5,6])
print(df.dtypes)
###############################################
#converting all types to best possible types
#imp : converting objects to strings .convert_dtypes()
df2 = df.convert_dtypes() 
print(df2.dtypes)
#chnage all columns to same type
df2 = df.astype(str)#'str' is used to converts it into object                           
print(df2.dtypes)
#chnage type for one or multiple columns (need to pass a dictionary)
df = df.astype({'Fee':int,'Discount':float})
print(df.dtypes)
#convert data type for All columns in a list
df = pd.DataFrame(technologies)
df.dtypes
cols = ['Fee','Discount']
df[cols] = df[cols].astype('float')
df.dtypes
#Ignores errors
df = df.astype({'courses':int},errors='ignore')
df.dtypes
#generate errors
df = df.astype({'courses':int},errors='raise')    
df.dtypes                                                                                                                     
#convert feed column to numeric type

############################
#create dataframe from dictionary
import pandas as pd
technologies = {
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,21000,20000,230000],
    'Duration':['30days','35days','40days','30days','50days','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]}
df = pd.DataFrame(technologies)
#######3
#convert dataframe into csv
df.to_csv('c:/1-python/data_file2.csv')#this csv file gets created in the working directory
df.to_excel()
#creating dataframe from csv
df1 = pd.read_csv('data_file.csv')
df1
############################
#pandas dataframe Basic operations
#create dataframe with none/null value to work with examples
import pandas as pd
import numpy as np 
technologies = ({
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,np.nan,20000,230000],
    'Duration':['30days','35days','40days','30days','','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
row_labels = ['r0','r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=row_labels)
print(df)
##########################
#Dataframe properties
df.shape #gives the number of rows and columns(row,col)
df.size  #gives the num of boxes or product or rows and columns
df.columns  #gives the names of the columns
df.columns.values #gives the names
df.index  #gives the index of the rows
df.dtypes  #gives the datatype of the entities
df.info #gives the information
#these are all the properties so no need of parenthesis()
#############
#Accesssing one column contents 
df['Fee']
#gives the content present in fees column
#Accesssing two column contents 
df[['Fee','Duration']]
#note : use two square brackets for accessing two or more column contents
#select certain rows or columns and assign it to another dataframe
df2 = df[4:]
df2
#accessing certain cell from column 'duration': 
df['Duration'][3]
#substraction specific value from a column
df['Fee'] = df['Fee'] - 500
df['Fee'] -=500  #can also be used              
df['Fee'] #substracts 500 from each content from the column 'Fee'
##########################
 
#pandas to manipulate Dataframes
#Describe dataframes
#descriebe dataframe from for all numeric column
df.describe() #it is a function
#it will give 5 number summary
##########################################
# Rename() : Renames pandas dataframe columns names
df = pd.DataFrame(technologies,index=row_labels) 
#Assign new headerby setting new column names.
df.columns=['A','B','C','D']
df 
###########
#rename column names using rename() method
df = pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2 = df.rename({'A':'c1','B':'c2'},axis=1) #pass dictionary in rename(dictionary,axis=0/1)
df2
#for accessing content of rows use axis=0 and for columns use axis=1
df2 = df.rename({'C':'c3','D':'c4'},axis='columns')
df2
df2= df.rename(columns={'A':'C1','B':'C2'})
df2

############################

#Drop rows by labels
df2 = df.drop(['r1','r2']) #r1 and r2 gets removed / dropped
df2
#delete rows by position/index
df1 = df.drop(df.index[1]) #if want to delete single index use sigle square bracket 
df1
df1 = df.drop(df.index[[1,3]]) #but if want to delete two or more rows using index use double sqaue brackets
df1
#Delete rows by index range
df1 = df.drop(df.index[2:5]) #Rows from 2 index gets deleted till (5-1) i.e 4th row 
df1 
#When you have default indexs for rows
df = pd.DataFrame(technologies) 
df1 = df.drop(0) #0th index row will get deleted
df1 
#deleting more rows using indexing
df = pd.DataFrame(technologies) 
df1 = df.drop([0,3]) #0th and 3rd row gets deleted. we can aslo give axis = 0 over here 
df1
df = pd.DataFrame(technologies)
df1 = df.drop(range(0,3)) #row from 0th index to 2nd index gets deleted
df1
###########################

#drop columns/ deleting columns
#note that it is compulsory to give axis = 1 while deleting columns and it is not mandetory in deleting rows
import pandas as pd
import numpy as np
technologies = ({
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,np.nan,20000,230000],
    'Duration':['30days','35days','40days','30days','','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
df = pd.DataFrame(technologies)
df
#drop column by name
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
#drop two or more volumns using lables
df = pd.DataFrame(technologies)
df2 = df.drop(['courses','Fee'],axis=1) #course and fees columns get deleted
df2
#drop two or more columns using index
df = pd.DataFrame(technologies)
df2 = df.drop(df.columns[[0,1]],axis = 1) #0th and 1st index position columns get deleted
df2
###############/      
#drop columns from list of columns
df = pd.DataFrame(technologies)
df
liscol = ['courses','Fee']
df2 = df.drop(liscol,axis=1) #this colums get deleted
df2

###########
###################

#iloc and loc
import pandas as pd
import numpy as np
technologies = ({
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,np.nan,20000,230000],
    'Duration':['30days','35days','40days','30days','','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
row_labels = ['r0','r1','r2','r3','r4','r5']
df = pd.DataFrame(technologies,index=row_labels)
print(df)

#df.iloc[startrow:endrow, startcol:endcol]
#examples on it;
df2 = df.iloc[:,0:2] #only ':' specifies that we want all the rows
df2
#this lines uses slicing operator to get dataframe
#items by index
##the first slice [:] indicates to returns all the rows
#the second slice specifies that only columns between 0 to 2 (excluding 2)should be returned
df2 = df.iloc[0:2,:]
df2
#This code displays all the columns but the rows only from 0 to 2 (excluding 2)
########
#Slicing specific rows and specific columns
df3 = df.iloc[1:2,1:3]
df3
###
df2 = df.iloc[2] #select row by index
df2
#It gives the series of first row and column name as its index

#exaples
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
#####################
#loc[]
#select rows by index lables
df2 = df.loc['r2'] #select row by label(gives the series)
df2
df2 = df.loc[['r2','r3','r4']] #select multiple rows using labels
df2
df2 = df.loc['r1':'r5'] #select rows by label in this range from r1 to r5(including r5)
df2
df2 = df.loc['r1':'r5':2] #select alternate rows 
df2
###########
#using loc[] for slice of columns 
import pandas as pd
import numpy as np
technologies = ({
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,np.nan,20000,230000],
    'Duration':['30days','35days','40days','30days','','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
df = pd.DataFrame(technologies)
df
df2 = df.loc[:,['courses','Fee','Duration']] #Only these columns gets displayed
df2
df2 = df.loc[:,['courses','Fee','Discount']] #selecting random coloumns
df2
df2 = df.loc[:,'Fee':'Discount'] #columns from fees to discount will be displayed including Discount
df2
df2 = df.loc[:,'Duration'] #Only Duration will be displayed
df2

##################################

#Pandas query()
#pandas.DataFrame.query()
#Query all rows with coureses = spark
#Used to filter the dataframes 
#example:
import pandas as pd
import numpy as np
technologies = ({
    'courses':['spark','pySpark','Hadoop','pandas','oracle','java'],
    'Fee':[20000,22000,23000,np.nan,20000,230000],
    'Duration':['30days','35days','40days','30days','','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
df = pd.DataFrame(technologies)
df
df2 = df.query("courses == 'spark'") #only spark row will be displayed
df2
#Not equals condition
df2 = df.query("courses != 'spark'") #all rows except spark will be displayed
df2
###################################
#Pandas adding columns to dataframs
tutor = ['ram','sham','priya','archie','raj','dhanshri']
df2 = df.assign(TutorsAssigned = tutor) #'TutorsAssigned' is the columns name 
print(df2)
#adding multiple columns
MNCCompanies = ['TATA','HCL','Infosys','Google','Amazon','Citi']
df2 = df.assign(MNC_Companies = MNCCompanies,Tutor_assign = tutor)
df2
#############333
#DErive new column from exisitng column
#You will have to use lambda fuction
df = pd.DataFrame(technologies)
df2= df.assign(Discount_percent = lambda x:x.Fee*x.Discount/100) #use dot operator(.) to access indivitual entities
df2
##############
#another way to add new columns to the existing dataframe
df = pd.DataFrame(technologies)
df["MNCCompanies"] = MNCCompanies
df 
#supervised learning:when you are giving lables
#adding new columns at specific location or position
df = pd.DataFrame(technologies)
df.insert(0, 'Tutors', tutor) #We are not giving inplace = True as well as axis = 1 not neccesary to give
df #the tutors will be added at the zeroth position
######################
#Finding the number of columns in the dataframe
rows_count = len(df.index)
rows_count
rows_count = len(df.axes[0])
rows_count
#finding column count
column_count = len(df.axes[1])
column_count
#Another way to find is usind shape[]
row_count = df.shape[0]
column_count = df.shape[1]
row_count
column_count

##########################################################

#pandas apply function on column
#use DataFrame.apply()
import pandas as pd
import numpy as np
#column operations
data = {
        'A':[1,2,3,4],
        'B':[5,6,7,8],
        'C':[9,10,11,12]
        }
df = pd.DataFrame(data) #Convert into dataframe
df 
def add_3(x):
    return x+3
df2 = df.apply(add_3) #3 gets added in all the columns
df2

#for adding only to the specific column we can also do it as
df2 = ((df.A).apply(add_3)) #it will become a series and only display that specific column
df2 

#apply function on single column
df['B'] = df['B'].apply(add_3)
df['B']
df

#Apply on multiple columns
def add_4(x):
    return x+4
df[['A','B']] = df[['A','B']].apply(add_4)
df

#We can aslo do the same thing using lambda fuction
df2 = df.apply(lambda x:x+3) #3 gets added to all the columns
df2

#instead of apply() we can also use pandas.dataframe.transform() to apply any function on the dataframe
def add_2(x):
    return x+2
df = df.transform(add_2)   
df                                                               

#using pandas.DataFrame.map() to single column
df['A'] = df['A'].map(lambda x:x/2) #All the elements in A columns get divided by 2
df['A']
######################3
#There are verious methods in numpy module too
#Which we can apply on dataframe of pandas
#example
import numpy as np
df['A'] = df['A'].apply(np.square) 
df
#another way to use it
df['A'] = np.square(df['A'])
df['A']
############################################################

#pandas groupby()
#use it when you have repeted entities in the specific column
data = ({
    'courses':['spark','pySpark','spark','pandas','pandas','java'],
    'Fee':[20000,22000,23000,25000,20000,230000],
    'Duration':['30days','35days','40days','30days','50days','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
df = pd.DataFrame(data)
df
df2 = df.groupby(['courses']).sum()
print(df2)

#using groupby() on multiple columns
df2 = df.groupby(['courses','Duration']).sum().reset_index()  #the changes will only if the dataframe is eligible to do soo do it one by one
df2

#######################################   
#pandas get column name from dataframe
import pandas as pd
import numpy as np
data = ({
    'courses':['spark','pySpark','spark','pandas','pandas','java'],
    'Fee':[20000,22000,23000,25000,20000,230000],
    'Duration':['30days','35days','40days','30days','50days','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
df = pd.DataFrame(data)
df
df.columns #Gives the list of column names
column_headers = list(df.columns.values)
print("The column Headers :",column_headers) 
##################################

#pandas shuffle dataframe rows
import pandas as pd
import numpy as np
data = ({
    'courses':['spark','pySpark','spark','pandas','pandas','java'],
    'Fee':[20000,22000,23000,25000,20000,230000],
    'Duration':['30days','35days','40days','30days','50days','45days'],
    'Discount':[10.2,3.4,67,12.5,30.4,5.6]})
df = pd.DataFrame(data)
df
#shuffle the dataframe rows and return all
df1=df.sample(frac=1) #100% rows will be shuffled i.e all rows will be shuffled
df1
df1 =df.sample(frac=0.5) #50% rows will be shuffled i.e all rows will be shuffled
df1
#shuffeling and creating new index starting from zero
df1=df.sample(frac=1).reset_index() #a new column with original index values gets created
df1 
df1=df.sample(frac=1).reset_index(drop=True) #a new column with original index values gets created
df1                                                                                                                                                                                                                                                                                                                                                         
#########################

#joins
data = ({
    'courses':['spark','pySpark','pandas','java'],
    'Fee':[20000,22000,23000,25000],
    'Duration':['30days','35days','40days','30days'],
    })
row_lable = ['r1','r2','r3','r4']
df1 = pd.DataFrame(data,index = row_lable)
df1

data_2 = ({
    'courses':['spark','C','Python','java'],
    'Discount':[2000,2200,2300,2500],
    })
index_lable = ['r1','r2','r3','r4']
df2 = pd.DataFrame(data_2,index = index_lable)
df2
#pandas inner join is mostly used to join
#it is used to join two dataframes on indexes
##when the indexes does not match the rows gets dropped from both the tables
#pandas join ,by default it will join the table left join
df3 = df1.join(df2, lsuffix="_left",rsuffix="_right")
df3
###########################################################

data = ({
    'courses':['spark','pySpark','pandas','java'],
    'Fee':[20000,22000,23000,25000],
    'Duration':['30days','35days','40days','30days'],
    })
row_lable = ['r1','r2','r3','r4']
df1 = pd.DataFrame(data,index = row_lable)
df1

data_2 = ({
    'courses':['spark','C','Python','java'],
    'Discount':[2000,2200,2300,2500],
    })
index_lable = ['r1','r6','r3','r4']
df2 = pd.DataFrame(data_2,index = index_lable)
df2
df3 = df1.join(df2, lsuffix="_left",rsuffix="_right")
df3
######################

#inner join
df3 = df1.join(df2, lsuffix="_left",rsuffix="_right",how='inner')
df3
 
#pandas left join dataframe
df3 = df1.join(df2, lsuffix="_left",rsuffix="_right",how='left') #Left table will be displayed fully and for right table only common entities will be displayed
df3

#pandas right join dataframe
df3 = df1.join(df2, lsuffix="_left",rsuffix="_right",how='right') #right table will be displayed fully and for left table only common entities will be displayed
df3

#pandas join on column
#if your not giving any column specifically it will take row index preference
df3 = df1.set_index('courses').join(df2.set_index('courses'),how='inner')
df3

df3 = df1.set_index('courses').join(df2.set_index('courses'),how='left')
df3

df3 = df1.set_index('courses').join(df2.set_index('courses'),how='right')
df3

#using pandas.merge() for inner join
df3 = pd.merge(df1,df2) #only joins the common entities rows
df3

###################################################################

#using pandas.concat(data)
import pandas as pd
data = {
        'courses':['python','spark','pandas','pyspark'],
        'fees':[20222,22000,23000,30000]
        }
df1 = pd.DataFrame(data)
df1
data_2={
        'courses':['pandas','hadoob','Hyperion','java'],
        'fees':[22000,25200,25400,24900]
        }
df2 = pd.DataFrame(data_2)
df2
#using pandas.concat() to concatinate two dataframes
data = [df1,df2] #make list of the dataframes
df2 = pd.concat(data) #concatinated dataframe gets stored in the df2 dataframe
df2 #index remains the same as of the original dataframe to change it use reset_index
#another way
df3 = pd.concat([df1,df2]).reset_index() #index gets changed(sequentially)
df3
#we can even append multiple dataframes

'''
   New_df = pd.concat([df1,df2,df3,....])
   print(New_df)
   
'''
##########################################################

#write dataframe to csv file with default params






