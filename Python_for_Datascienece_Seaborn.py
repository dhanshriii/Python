# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:06:55 2023

@author: Lenovo
"""

#Python for data science
#Seaborn: used for data vitualization
#Seaborn has some ready datasets 
import seaborn as sns 
#Seaborn has 18 in-built datasets
#That can be found using following command
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head() #it only takes 1st five rows of the dataset by defaiult however you can set the number of rows you want
df.head(10) #gives first 10 lines

#Count plot
#Used to plot the frequencies of different categories
#the column sex contains categorical data in the titanic data i.e.,male and femal
sns.countplot(x='sex',data=df) #Graph will be plotted  
#x = The name of the column
#data = Tha dataframe

sns.countplot(x='sex',hue ='survived',data=df,palette = 'Set1')
#Gives how many males were survived and how many females were survived(0-death,1-alive)
sns.countplot(x='sex',hue ='survived',data=df,palette = 'Set2')
sns.countplot(x='sex',hue ='survived',data=df,palette = 'Set3') 
#palette : Used for changing the set of colours /color palette to be used
#hue:name of the categorical column to split the bars

##########################################################################

#KDE Plot: Kernel Density Estimate plot
#Used to plot the distribution of continuous data
sns.kdeplot(x='age',data=df,color='black')
#x=name of the column
#data = dataframe
#color = color of the graph

#Distribution plot
sns.displot(x = 'age',kde=True,bins = 6,data=df)
#kde = it set to false by default but if you want to add kde plot also then set it to True
#bins = the number of bins or bars,the lower the number the wider the bars 
sns.displot(x='age',kde=True,bins=5,hue=df['survived'],palette = 'Set1',data=df)

#Scatter plot using Seaborn:More powerfull then matplotlib.pyplot.scatterpot()
#We will be working on  iris dataset:iris is a flower
df = sns.load_dataset('iris')
df.head()
#Scatter plots help understand cp-relation between datasets
sns.scatterplot(x='sepal_length',y='petal_length',data=df,hue='species')
#Gives legends alsoo

#joint plot
#Also used to plot corelation between data
#it consists of scatter plot as well as histogram and can also add kde
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='reg')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='hist')
sns.jointplot(x='sepal_length',y='petal_length',data=df,kind='kde')
'''
kind: the kind of the plot to be plotted it can be one of the following
scatter,hist,hex,kde,reg,resid
''' 

#pair plot
sns.pairplot(df)

#heat map
#A heat map can be udes to visualize confusion,matrices and correlations
corr = df.corr()
sns.heatmap(corr)






