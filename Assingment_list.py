# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:32:34 2023

@author: Lenovo
"""
#FUNCTIONS in python are: .append(), .insert(), .index(), 
#.clear(), .remove(), .reverse(), .count(), sum(), min(), 
# .max(), random.shuffle(),.split(),.join()

#write python program to get smallest number from the list
def smallest(items):
    min=items[0]
    for x in items:
        if x<min:
            min=x
    return min
smallest([2,1,3,4,5])

####################################

#write a python program to find the number of string whose len is 2 or more then 2 and its first and last char should be same
def count(list3):
    counter=0
    for x in list3:
        if len(list3)>=2 and x[0]==x[-1]:
            counter+=1
    return counter
count(['ece','yty','uyt','oio'])

######################################

#write python program to get a list sorted in increasing order by the last elemets in each tuple from given list of non-empty tuple
sample_list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for x in sample_list:
    for y in x:
        y[-1]#Wrong code /try it later code
        
def last(n):
    return n[-1]
def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

####################################

#write a python program to remove all the doblicates from the list
#given list a=[10,20,30,20,10,50,60,40,80,50,40]
a=[10,20,30,20,10,50,60,40,80,50,40]
dup_list=set()
uniq_list=[]
for x in a:
    if x not in dup_list:
        uniq_list.append(x)
        dup_list.add(x)
print(dup_list)
#OR
a=[10,20,30,20,10,50,60,40,80,50,40]
uniq_list=[]
for x in a:
    if x not in uniq_list:#check if that that element present in that list if not thrn append/add
        uniq_list.append(x)
print(uniq_list)
#OR
lst1=[10,20,30,20,10,50,60,40,80,50,40]
set1=set(lst1)#Convert it into set as set dosent allow dublicates
print(set1)
lst2=list(set1)#convert again into list as we want the out put as list
print(lst2)

######################################

#write python program to clone or copy a list
original_list=[10,22,24,23,4]
new_list=list(original_list)
print(original_list)
print(new_list)
#OR
original_list=[10,22,24,23,4]
new_list=[]
for x in original_list:
    if x not in new_list:
        new_list.append(x)
print(new_list)
print(original_list)

####################################

#write python program to find the list of words thst are longer then n from a given list of words
    
def long_word(n,str):
    word_len = []
    txt=str.split(" ")#created a list of words splitted from white space
    for x in txt:
        if len(x)>n:
            word_len.append(x)
    return word_len
long_word(3, "The quick brown fox jumps over the lazy do")

###################################### 

#write a python function that takes two lists and return true if have at least one common element in that both the lists
def common_data(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x==y:
                result = True #print true if samilar element present in the list
        return result
print(common_data([1,2,3,4], [5,6,7,8]))
print(common_data([1,2,3,4,5], [1,5,6,7,8,9]))

#########################################

#write a python program to calculate the difference between two list
#create a seperate list of unique elements from this two lists
list1=[1,2,3,4,5]
list2=[1,6,3,7,9,8]
diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
total_diff = diff1 + diff2
print(total_diff)

###########################################

#write a python program to convert a list of characters into a string.
s = ['a','b','c']
str1 = ''.join(s)
print(str1)

##########################################

#write a python program to find the index of an item in a specific list
num=[1,2,3,4]
print(num.index(3))

##############################################
#write a python program to append a list to thr second list
list1=[1,2,3]
list2=[]
list2.append(list1)
print(list2)
#OR
list1=[1,2,3,4]
list2=['red','green','black']
final_list=list1+list2
print(final_list)

##########################################




