# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:01:47 2023

@author: Lenovo
"""

#Take 5 element in list and find the min and max
#using inbuilt fuction
#min
list1=[4,3,1,2,5]
print(min(list1))
 
#using logical code
min=list1[0]
for i in list1:
    if min>i:
        min=i
print(min)

#max
#using inbuilt fuction
list1=[4,3,1,2,5]
print(max(list1))

#using logical code
max=list1[0]
for ele in list1:
    if max< ele:
        max=ele
print(max)

#######################################

#take 5 strings and reverse its order
list2=['ritu','priya','rahi','prachi','ruchi']

print(list2[::-1])
list2.reverse()
print(list2)

###########################################

#take 10 numbers in the list write code to find any number in the list
listt=[1,2,3,4,5,6,7,8,9,10]
num=int(input("Enter a number you want search in the list: "))
flag=0
for i in listt:
    if num==i:
       flag=1
if flag==1:
    print(f"yes the number is present in the list at {i} location")
else:
    print("The number is not present in the list")
    
##########################################

#take 10 number in a list find dublicates
list4=[1,2,3,1,4,2,5]
ele=int(input("Enter the number whose dublicate you want to see: "))
count=0
for i in list4:
    if i==ele:
        count+=1
if count==1:
    print("The element has no dublicate")
else:
    print(f"The element is repeated {count} times")
    
############################################

#take vovels and cosonents in the list find the no of vvels in the lis
list5=['a','e','i','o','u','A','c','d','z','f']
count=0
for i in list5:
    if i=='a' or i=='e' or i=='i'or i=='o'or i=='u'or i=='A' or i=='E' or i=='I' or i=='O'or i=='U':
        count+=1
if count>0:
    print(f"The number of vovels in the list are :{count}")
else:
    print("There are no vovels in the list")

    