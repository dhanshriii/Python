# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:26:04 2023

@author: Lenovo
"""

#Python for datascience: Numpy
#used for scientific computing applications
#It stands for numerical python
#it consists of multidimentional array
#array cannot contain different types of datatypes i.e arrays are homogeneous
#Array is also known as vector 

'''
array in Numpy
'''
#Creating ndarray
import numpy as np
arr = np.array([1,2,3,4,5]) #creating and initializing an array 
print(arr)

#Creating multidimentional array
arr = np.array([[1,2,3,4,],[5,6,7,8]]) #For multidimentional array we have 2 sqaure brackets
print(arr) #Gets displayed one below the other ,The size of all the arrays must be same
#output
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
#represent the minimum dimention
#use ndmin param to specify how many minimum dimentionas you wanted to create
arr = np.array([10,20,30,40],ndmin=2)
print(arr) #as we specified ndmin=2 the array becomes two dimentional

#change the data type
#dtype parameter
arr = np.array([1,2,3,4],dtype=complex)
print(arr) #the array becomes complex one diemntional array

arr = np.array([1,2,3,4],dtype=str,ndmin = 2)
print(arr) #This array becomes string array ,two dimentional

#Get the dimentionas of the array 
#using arr.ndim
arr = np.array([[1,2,3,4],[5,6,7,8],[7,8,9,19]])
print(arr)
print(arr.ndim) #gives the dimention of the array 

#finding the size of each item in the array
#use arr.itemsize
arr = np.array([1,3,4,5])
print(arr.itemsize) #gives the number of the array elements present

#Finding datatype of each array
#use arr.dtype
arr = np.array([1,3,4,5])
print(arr.dtype) #gives the datatype of the array

#properties of array
#shape and size of array
arr = np.array([[1,2,3,4],[5,6,7,8],[7,8,9,19]])
print(arr)
print("Size of the array is: ",arr.size) #gives total number of elements
print("shape of the array is: ",arr.shape) #gives (row,column)

#create a sequence of integers using arange()
#Example creating sequence of integers form 0 to 20 with step of 3
arr = np.arange(0,20,3) #(Start,end+1,step)
print(arr)

##################################################################

#array indexing in numpy
#accessing single element using indexing
arr = np.arange(11)
print(arr)
print(arr[2]) #positive indexing
print(arr[-2]) #negative indexing

#multidimentional array indexing
#access multidementionalarray elements using array elements
arr = np.array([[1,2,3,4],[5,6,7,8],[7,8,9,19]])
print(arr)
print(arr[1,2]) #output will be 7 
print(arr[1,-1]) #output will be 8

#access array elements using slicing
#start:end:step
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,7,8,9,10])
print(arr)
x = arr[1:8:2]
print(x) 

x = arr[-2:3:-1]
print(x)

x = arr[-2:8] #not getting output
print(x)

##############################################################

#Slicing array
#for multidimentional numpy array you can access the elemets as below
multi_arr = np.array([[10,20,10,40],
                    [40,50,70,90],
                    [60,10,70,80],
                    [30,90,40,30]])
multi_arr[1,2] #to access the value at row 1 and column 2
multi_arr[1,:] #To access the value at row one and all the columns
multi_arr[:,1] #to access the value at all rows and 1 column
#
multi_arr[:3,::2] #columns from 0 to 3 and every alternate rows

#Integer array indexing
#integer array indexing allows the selection of arbitrary items
arr = np.arange(35).reshape(5,7)
print(arr)
#output : two dimentional array gets created of 5 rows and 7 columns
'''
[[ 0  1  2  3  4  5  6]
 [ 7  8  9 10 11 12 13]
 [14 15 16 17 18 19 20]
 [21 22 23 24 25 26 27]
 [28 29 30 31 32 33 34]]
'''
##################################################################

#boolean array indexing  

#
arr = np.arange(12).reshape(3,4)
print(arr)
rows = np.array([False,True,True]) #not zeroth row only first and second row
wanted_rows = arr[rows,:] #selected rows and all columns
print(wanted_rows)

#################################################################

#converting array to list
#using tolist()

#convert one dimentional array to list
#create array
array = np.array([1,2,3,4,5])
print("Array: ",array)
print(type(array))  #<class 'numpy.ndarray'>
#converting array to list
lst = array.tolist()
print("List: " , lst)
print(type(lst))  #<class 'list'>

#converting multidimentional array to list
arr = np.array([[10,20,10,40],
                    [40,50,70,90],
                    [60,10,70,80],
                    [30,90,40,30]])
print("Array: ",arr)
print(type(arr))
lst = arr.tolist()
print("List: ",lst)  #becomes list of lists
print(type(lst))
#List:  [[10, 20, 10, 40], [40, 50, 70, 90], [60, 10, 70, 80], [30, 90, 40, 30]]

#################################################################3

#converting list to a numpy array
#numpy provides us two fuctions
#   1)numpy.array()
#   2)numpy.asarray()

#create list
list = [20,30,40,50]
print(list)
print(type(list))
#convert to array
array = np.array(list)
print(array)
print(type(array))

#using asarray()
list =  [20,30,40,50]
array = np.asarray(list)
print("Array: ",array)
print(type(array))

##################################################################3

#Numpy array properties

#ndarray.shape
#ndarray.size
#ndarray.itemsize
#ndarray.dtype
#ndarray.ndim

################################################################

#Numpy also provides numpy.reshape() function to resize an array
#reshape usage
import numpy as np
array = np.array([[10,20,30],[40,50,60]])
print(array)
#output
'''[[10 20 30]
 [40 50 60]]'''
new_array = array.reshape(3, 2) 
print(new_array)
#output
'''[[10 20]
 [30 40]
 [50 60]]'''

###############################################################

#operations using numpy
#numpy operations are divied into three main categories
''' 
Fourier Transform and Shape Manipulation
 Mathematical and logical operationas
 linear algebra and random number generation
'''

########################################################################



















