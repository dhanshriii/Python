#!/usr/bin/env python
# coding: utf-8

# ## Lets start  our Python journey, paving the way in the world of data scinece

# In[1]:


#Variable : countiners to store data 
a = 10


# In[2]:


print(a) #print : used to display information on console


# In[3]:


type(a) #type() : this function is used to check the datatype of the variable


# In[15]:


#More data types

#1) Integer 
b = 9.8
print(b ," ", type(b))

#2) Boolean
c = True
d = False
print(c ," ", type(c))    
#True stores internal value as 1 and false stores internal value as 0
print("True + False =",c + d)  #If we perform this it does the addition of internal values 
    #Result : 1
print("True * False =",c * d)
    #Result : 0
    #We can only perform + and * and not _ , / 

#3)String
e = "Dhanshri"
print(d ," ", type(3))

#4)Complex number
f = 5 + 8j  #Here we dont use 'i' as we do in maths but python uses 'j' notation to identify complex numbers
print(f ," ", type(f))


# In[23]:


#String indexing
Name = "Dhanshri"
print(Name)
#python supports positve as well as negative indexing
Name[0]   #positive [staring from 0, 1,....]

Name[-1]  #Negative [straing from -1, -2,.....]

#String are immutable and it does not support item assignment
#While using replace() : its changes the element but it generates new memeory location and does not change the original stirng


# In[26]:


#String Slicing based in indexing
#Str[lower_bound : upper bound + 1]
Name[0 : 4]

#Want to step between the character or want some gap 
Name[0 : 9 : 2]  #The upper bound dosent matter in slicing it can be any number
Name[0 : 90]

#But its not the same in Indexing , In indexing we have to put only valid index


# In[34]:


#String Functions
#If your working on jupyter notebook Str.(Press tab) The available fuctions will be dislayed

#Some basic functions are
Name.find('a')   #Find() : returns the index of the character or substring
Name.count('h')  #count() : counts how many times the charecter or substring occured in the string
Name.upper()     #upper() : Converts the whole string in Capital letters
Name.lower()     #lower() : Converts the whole string in small letters
Name.title()     #tilte() : First letters of all the words turns capital
Name.capitalize()#capitalize : Only first letter Capital

#Note
sent = 'Don't do copy paste'  #this will give error as python is not able to understand where did we actually closed the qoute
#So whenever you are using a single quote in the string, the outer quote should be ("") Double and whenever using double quote in the string give the single outer quote
sent = "Don't do copy paste"

#Multi line stirng
sent = """Hello every one 
    To day i have learned about variable diclaration ,
    different data types in python
    and looking forward to dive deep in the world of python."""
#Triple qoute can be used as a multiline comment as well as to store string.


# In[36]:


#List : Colection of data of different data types
l1 = [1,'DC',3.4,True]
type(l1)


# In[71]:


#List follows the indexing same as Stirng
#So to print any element from list use indexing
l1[1]  #Positive
l1[-1] #Negative

#Here we can also use slicing
l1[1 : 4] 

#Reversing the list
l1[::-1]

#Printing data available on even indexes
l1[::2]
#printing data available on odd indexes
l1[1::2]

#adding new data in string
s = 'Dhanshri'
l1.append(s)  #inbuilt function To appned at th end of the list
l1
#We also have extend() : but using this we can only add iterable values
#We also have insert() : to add values at specific values

#Printing the 'Dha' from dhanshri
l1[4][:3]

#Concatinate list with list
l2 = [2, 3, 4]
l1 + l2

#Number of elements present in the list
len(l1)
len(l2) 


# In[70]:


#Delete any element
l1.pop(5)  #Delete any specific element By index we pass index as parameter
l1.remove(1) #It deletes the value and valyes are pssed as parameter



# In[73]:


#Reversing The list
l1[::-1]  #We can also use reverse() But permently reverses the list

#Sorting list is applicable only on the list having similar kind of data
l3 = [3,2,4,1]
l3.sort()
l3

l3.index(3) #gives the index of the element
l3.count(3) #Give the number of times the element is repeated

#List is mutable as we can even change or reassign the elements


# In[81]:


#Tuples : Similar to list Data stored in '()'
#Tuples are immutable
t = (1, 2, 3, 4)
type(t)

#Length
len(t)

##Printing any element
t[1]

#Slicing
t[1:5:2]

#Note : Reassignemnet and mutability are different
#The data cannot be changed in tuple as it is mutable

#Reversing tuple
t[::-1]

#The functions available are count and index


# In[87]:


#Set : Collection of unique data elements
#It accepts only immutable collection of data

s = {1,2,3,4,'Dhanshri',5.4}
type(s)
s
#Set is unordered collection it prints randomly any data

#We cannot perform indexing and slicing on list as it is unordered

s.add(6)  #This is element to be added

s.remove(4) #This the element and not index
s


# In[106]:


#Dictionary
d = {'Key' : 'Value'}  #The key should always be unique
type(d)

d1 = {'name' : "Dhanshri",
     'email' : "abc@gmail.com",
     'Phone' : 12345678,
     'sub' : ['phy','chem'],   #The value can be a list also
     'time' : (1,2.3),         #The value can also be a tuple
      'Alpha' : {'a','b','c'},  #The value can also be a set
      'Num' : {1 : 2, 4 : 5},   #The value can also be another dictionary 
      2 : 45,
     True : 1,
     }
d1

#If we want to print any key value we use the keys as here we dont have the concept of indexing
d1[1]  #As internally True stores 1 thats why we will get the output
d1['name']  

#If we give different values for same keys the the last updated values get assigned overriding the other values

#Adding new key value
d1[False] = 0  #IF already exists then it will update the value
d1

#DElete any key value pair
del d1[True]
d1

#Printing keys
d1.keys()

#Printing all the values
d1.values()

#Printing both keys and values
d1.items()  #In the form of tuple

#Deleting using pop()
d1.pop(False)


# In[ ]:




