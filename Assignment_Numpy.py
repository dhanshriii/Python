# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:04:44 2023

@author: Lenovo
"""

#write a numpy program to check the numpy version
import numpy as np
print(np.__version__)

##################################################################

#write a numpy program whether none of the element of the array are zero
import numpy as np
x = np.array([1,2,3,4,5])
print("Original array")
print(x) 
print("Test if none of the element in the given array is zero: ")
print(np.all(x)) #gives true if all the lements are non-zero
x = np.array([0,2,3,4,5])
print("Original array")
print(x)
print("Test if none of the element in the given array is zero: ")
print(np.all(x)) #will give false as there is a zero

#######################################################################

#write a numpy program to test if any on the elements in the given array are non-zero
x = np.array([0,0,0,0,5])
print("Original array")
print(x)
print("Test if any of the element in the given array is zero: ")
print(np.any(x))  #will give true as there is one non-zero element present in the array
x = np.array([0,0,0,0,0])
print("Original array")
print(x)
print("Test if any of the element in the given array is zero: ")
print(np.any(x))  #will give false as there in no non-zero element in the array

#####################################################################

#write a numpy program to test given array element-wise for finiteness(not infinity or not a numuber)
#we'll use np.isfinite(array)
import numpy as np
a = np.array([1,2,np.nan,np.inf])
print("Original array: ")
print(a)
print("Test a given array element-wise for finiteness: ")
print(np.isfinite(a)) #It will check element to element and give a list of true and false true if element is not nan or inifinite and false if element is nan or infinite

######################################################################

#write a numpy program to test element-wise for Nan of a given array
#use np.isnan()
import numpy as np
a = np.array([1,2,np.nan,np.inf])
print("Original array: ")
print(a)
print("Test a given array element-wise for NaN: ")
print(np.isnan(a)) #will check element to element in thelist and will a list of true and false values true if there is a nan value and false if other then that

####################################################################

#write a numpy program to create a element wise comparison 
#(greater,greater_equal,less and less_equal)
#using functions np.greater,np.gtrater_equal,np.less,np.less_equal
import numpy as np
a = np.array([3,5])
b = np.array([2,5])
print("Original arrays: ")
print(a)
print(b)
print("Comaprison - greater")
print(np.greater(a,b)) #checks if elements in a are greater then b
print("Comaprison - greater_equal")
print(np.greater_equal(a,b))
print("Comaprison - less")
print(np.less(a,b)) #checks if elements in a are less then b
print("Comaprison - less_equal")
print(np.less_equal(a,b))

###################################################################

#write a numpy program to create a 3*3 identity matrix
#there is a build in function to cfeate an identity matrix
#np.identity()
import numpy as np
array_2D = np.identity(3)
print("3*3 matrix: ")
print(array_2D) #3*3 identity matrix will be created

###################################################################

#write a numpy program to generate a random number between 0 and 1
import numpy as np
rand_num = np.random.normal(2,9,4) #(loc,scale,how many number of random number do you want)
print("Random number in 0 and 1: ")
print(rand_num)

####################################################################

#Write a numpy program to create a 3*4 array and iterate over it
import numpy as np
a = np.arange(10,22 ).reshape(3,4)
print("Original array ")
print(a)
print("Each element of the array is: ")
for i in np.nditer(a):
    print(i,end = " ")
    print()

##################################################################

#Write an numpy program t create a vector of lenght 5 with values equally distributed between 5 and 50
import numpy as np
v = np.linspace(10,49,5) #(start,end,num)
print("Length 5 with values equally distributed between 10 to 50:" )
print(v)

####################################################################

#write a numpy program to create 3*3 matrix with value ranging from 2 to 10
import numpy as np
x = np.arange(2,11).reshape(3,3)
print("3*3 matrix: ")
print(x) #A matrix will be created which include numbers from 2 to 10

####################################################################3 

#write a numpy program to reverse an array
#(First element becomes last)
import numpy as np
x = np.arange(12,38)
print("Original array: ")
print(x)
print("Reverse array: ")
x = x[::-1]
print(x)

########################################################################

#write a numpy program to compute multiplication of two matrix
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("Original matrix: ")
print(p)
print(q)
result1 = np.dot(p, q)
print(result1) #gives the dot product of the given matrix

#Write a numpy program to compute the cross product of the two given vectors
import numpy as np
p = [[1,0],[0,1]]
q = [[1,2],[3,4]]
print("Original matrix: ")
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print(result1) 
print(result2)

####################################################################

#write a numpy program to comute determinant of a given square array
import numpy as np
#from numpy import linalg as LA
a = np.array([[1,0],[1,2]])
print("Original 2-D array:")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))

###################################################################

#write a numpy program to compute the eigen values and eigen vectors of given square array
#using inbuild methods np.linalg.eig(matrix)
import numpy as np
m =np.mat("3 -2;1 0")
print("Original matrix:")
print("a/n",m)
w,v = np.linalg.eig(m)
print("Eigen values of the said matrix: ",w)
print("Eigen values of the said matrix: ",v)

#################################################################

#Write a numpy program to compute the inverse of a given matrix
import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix: ")
print(m)
result = np.linalg.inv(m)
print("inverse matrix is: ")
print(result) #Gives the inverse of the matrix

#################################################################

#write a numpy program to add,substract,multiply,divide 
import numpy as np
arr = np.arange(1,4)
arr2 = np.arange(1,4)
print(arr)
print(arr2)
print(np.add(arr,arr2))
print(np.subtract(arr,arr2))
print(arr*arr2)
print(arr/arr2)












