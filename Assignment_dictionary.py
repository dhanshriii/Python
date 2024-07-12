# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:45:08 2023

@author: Lenovo
"""

#write a python code to add key to a dictionary
#sample dictionary= {0:10,1:20}
#expected result= {1:10,1:20,2:30}
d={0:10,1:20}
print(d)
d.update({2:30})
print(d)
#or
d[2]=30
print(d)

##############################

#write python code to concatenate the following dictionaries to create a new one
#we directly cannor concatenate dictionary using '+' operator so we create a empty dictionary 
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict4 = {}
for d in (dict1,dict2,dict3):dict4.update(d)
print(dict4)

################################

#write a python code to check whether a given key already exists in a dictionart
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

#######################################

#write python code to iterate over dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for dict_key,dict_value in d.items():
    print(dict_key,":",dict_value)
    
############################################
    




