# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:36:00 2023

@author: Lenovo

"""

#write a python program to to create an iterator from sevaral iterators in a sequence and display the type and elements of the new iterator
#use chain operator(chain())
from itertools import chain     
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#list
result = chain_func([1,2,3], ['a','b','c','d','e'], [4,5,6,7])
print("type of new iterator:")
print(type(result))
print("Elements of new iterator:")
for i in result:
    print(i)
#tuple
result = chain_func((1,2,3), ('a','b','c','d','e'), (4,5,6,7))
print("type of new iterator:")
print(type(result))
print("Elements of new iterator:")
for i in result:
    print(i)

############################################

#write python program that generates the running product of elements in a iterable
from itertools import accumulate
import operator  #it has all mathamatical operators
def running_product(lst):
    return accumulate(lst,operator.mul)
#list
result = running_product([1,2,3,4,5,6,7])
print("the running product is: ")
for i in result:
    print(i)
#tuple
result = running_product((1,2,3,4,5,6,7))
print("the running product is: ")
for i in result:
    print(i)
    
##################################################

#write python program to construct a infinite iterator thst returns evenly spaced values 
#starting with specified number and steps
import itertools as it
start = 10
step = 1
print("the starting is ",start," and the step is ",step)
my_counter= it.count(start,step)
#following loop will run for ever
print("the said function print never-ending items: ")
for i in  my_counter:
    print(i)

################################################

#write python program to generate infinite cycle of elements from an iterable
import itertools as it
def cycle_data(iter):
    return it.cycle(iter)

#following loops will run forever
#list
result = cycle_data(['A','B','C'])
print("Infinite cycle loop is : ")
for i in result:
    print(i)
#string
result = cycle_data('python itertools')
print("the said functions prints never ending loop: ")
for i in result:
    print(i)

#######################################################

#write a python program to make an iterator that that drops the element from the iterable as soon as an element is an positive number
import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x : x<0, nums)
nums = [-1,-2,-3,-4,5,-6,-7,-8,9]
print("original list: ",nums)
result = drop_while(nums)
print("Drop elements from the list when positive elements arises",list(result))

#######################################################








