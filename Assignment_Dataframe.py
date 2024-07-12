# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:01:06 2023

@author: Lenovo
"""

# Write a pandas program to create dataframe from dictionary and display it
import numpy as np
import pandas as pd
d = {
    'X': [1, 2, 3, 4, 5, 6],
    'Y': [11, 12, 13, 14, 15, 16],
    'Z': [21, 22, 23, 24, 25, 26]
}
df = pd.DataFrame(d)
df

###########################################

# write a pandas program to create and display a dataframe from a specified didctionary and give it row lables
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, 9.6, 7, 4, 8],
    'attemps': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df

################################################

# write a pandas program to dsiplay summary of basic information abount the dataframe
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, 9.6, 7, 4, 8],
    'attemps': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
Df.describe()
Df.info

#####################################################

# write pandas prgram to get first three rows of pandas dataframe
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, 9.6, 7, 4, 8],
    'attemps': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
# Diplaying using loc first three rows will be dsiplayed
df2 = Df.loc[['A', 'B', 'C']]
df2
# OR
df2 = Df.iloc[:3]
df2

######################################################

# write python program to select name and score column from the given data frame
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, 9.6, 7, 4, 8],
    'attemps': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
df2 = Df.loc[:, ['name', 'score']]
df2
# Or
print(Df[['name', 'score']])

##########################################################

# write pandas program to select specified rows and columns
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, 9.6, 7, 4, 8],
    'attemps': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
df2 = Df.loc[['B', 'D', 'F', 'G']]
df2
df3 = df2.loc[:, ['score', 'Qualify']]
df3
# Or

###########################################################

# write a pandas program to select the rows where the number of attempts in the examination is greater then 2
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
print("Number of attemts in thr examination greater then 2 are:")
print(Df[Df['attempts'] > 2])
Df2 = Df.loc[Df.attempts > 2]
Df2

########################################################

# write  apandas program to to find the number of rows and columns

# rows
row_count = len(Df.index)
row_count
# columns
column_count = Df.shape[1]
print("No.of column: ", column_count)

##############################################################

# write a pandas program to select the row where the score is missing that is none
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
print("Rows where score is missing: ")
df2 = Df[Df['score'].isnull()]
df2

##################################################################

# write a pandas program to select rows between 15 and 20(Inclusive)
# We can between() function to get the expected output
# In parenthesis we give the range
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 20, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 16, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
# Students having score in between 15 and 20 including 15 and 20 will be displayed
df2 = Df[Df['score'].between(15, 20)]
df2

#############################################################

# Write pandas program to select the rows in which the number of attempts in the examination
# is less then 2 and score greater than 15
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
df2 = Df[Df['attempts'] < 2]
df3 = df2[df2['score'] > 15]
df3
# OR
df2 =Df[(Df['attempts'] < 2) & (Df['score'] > 15)]
df2  

##################################################################

# Write a pandas program to change the score in row 'D' to 11.5
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
Df.loc['D', 'score'] = 11.5
Df

# 33

# write pandas program to calculate sum of the examination attempts by the students
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
# Gives the sum of all the values in the attempts column
sum = Df['attempts'].sum()
print(sum)

###################################################################

# write a pandas program to calculate mean of all students score
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
# Gives the mean of all the values in the score column
mean = Df['score'].mean()
print(mean)

###############################################################

# write a pandas program to append new row 'K' to the dataframe by giving that specific values
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
print("Append new row : ")
Df.loc['K'] = ['Raj', 45, 2, 'yes']
Df

##########################################################

# write a pandas program to sort dataframe first by name in decending order then by score in acending order
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'priya', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
df = Df.sort_values(by=['name', 'score'], ascending=[False, True])
df
df = Df.sort_values(by=['name'], ascending=[False])
df
df2 = df.sort_values(by=['score'], ascending=[True])
print("sorted dataframe first by name in decending order then by score in ascending order :")
df2

# write pandas program to replace thw Qualify column contains the values 'yes' and 'no' with 'false' and 'true'
# we can use map(pass dictionary)
dic = {
    'name': ['Ram', 'Sham', 'Ghansham', 'Bahubali', 'Krishna', 'Kisan', 'Karishna', 'radha', 'Rohit', 'roshni'],
    'score': [12.4, 4.7, 56.7, np.nan, 7.8, 67.7, np.nan, 7, 4, 8],
    'attempts': [1, 2, 1, 2, 3, 1, 1, 1, 1, 1],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']

}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Df = pd.DataFrame(dic, labels)
Df
Df['Qualify'] = Df['Qualify'].map({'yes': True, 'no': False})  # Yes and no gets replaced
Df

######################################################################

#write a pandas program to change name rohit to james in column names of the dataframe
import pandas as pd
import numpy as np
dic = {
       'name':['Ram','Sham','Ghansham','Bahubali','Krishna','Kisan','Karishna','radha','rohit','roshni'],
       'score':[12.4,4.7,56.7,np.nan,7.8,67.7,9.6,7,4,8],
       'attemps':[1,2,1,2,3,1,1,1,1,1],
       'Qualify':['yes','no','yes','yes','yes','yes','yes','yes','yes','no']
     
       }
labels = ['A','B','C','D','E','F','G','H','I','J']
Df = pd.DataFrame(dic,labels)                                                                                                                                      
Df
Df['name'] = Df['name'].replace('rohit','James') #it is case sensitive put the name properly
Df

########################################################################

#write a pandas program to add new column to the existing data frame
import pandas as pd
import numpy as np
dic = {
       'name':['Ram','Sham','Ghansham','Bahubali','Krishna','Kisan','Karishna','radha','priya','roshni'],
       'score':[12.4,4.7,56.7,np.nan,7.8,67.7,np.nan,7,4,8],
       'attempts':[1,2,1,2,3,1,1,1,1,1],
       'Qualify':['yes','no','yes','yes','yes','yes','yes','yes','yes','no']
     
       }
labels = ['A','B','C','D','E','F','G','H','I','J']
Df = pd.DataFrame(dic,labels)
Df
color = ['Red','blue','green','purple','voilet','marun','peach','black','yello','white']
Df['color'] = color #this column gets added to the dtataframe
Df

###################################################################

#write a pandas program to iterate over rows in the dataframe

import pandas as pd
import numpy as np
dic = {
       'name':['Ram','Sham','Ghansham','Bahubali','Krishna','Kisan','Karishna','radha','priya','roshni'],
       'score':[12.4,4.7,56.7,np.nan,7.8,67.7,np.nan,7,4,8],
       'attempts':[1,2,1,2,3,1,1,1,1,1],
       'Qualify':['yes','no','yes','yes','yes','yes','yes','yes','yes','no']
     
       }
labels = ['A','B','C','D','E','F','G','H','I','J']
Df = pd.DataFrame(dic,index=labels)
Df                    
for index,row in Df.iterrows():
    print(row['name'],row['score'])
















  