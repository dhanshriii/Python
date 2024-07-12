# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:02:17 2023

@author: Dell
"""

#print Hello World
print('Hello World')
"""
.py extension. Such a file can contain 
one or more Python statements that represent
a Python program or Script."""
#Variables
'''
Types of Numbers
There are three types used to represent f
numbers in Python; 
these are integers (or integral) types, 
floating point numbers and complex numbers.
'''
x = 1
print(x)
print(type(x))
x =100000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))

'''
This makes it very easy to work with integer 
numbers in Python. Unlike some
programming languages such as C# and Java 
have different integer types depending
on the size of the number, 
small numbers having to be converted into 
larger types in some situations.
'''
#############################
#Converting to Ints

'''It is possible to convert another type 
into an integer using the int() function. For
example, if we want to convert a string 
into an int (assuming the string contains a
integer number) then we can do this using 
the int() function. For example 
total = int('100')
This can be useful when used with 
the input() function.
The input() function always returns a string.
 If we want to ask the user to input 
 an integer number, then we will need 
 to convert the string returned from the
input() function into an int.We can do this 
by wrapping the call to the input()
function in a call to the int() function
'''
age = input('Please enter your age:')
print(type(age))
print(age)


age1 = input('Please enter your age:')
print(type(age1))
print(age1)

age2 = input('Please enter your age:')
print(type(age2))
print(age2)
age=age1+age2
print(age)


age = int(input('Please enter your age:'))
print(type(age))
print(age)

age1 = int(input('Please enter your age:'))
print(type(age1))
print(age1)

age2 = int(input('Please enter your age:'))
print(type(age2))
print(age2)
age=age1+age2
print(age)
##############################################
#Floating Point Numbers
#Real numbers, or floating point numbers, 
#are represented in Python using the IEEE 754 
#double-precision binary floating-point number format
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))
######################################
#Converting to Floats
#As with integers it is possible to convert other 
#types such as an int or a string into a float.
int_value = 100
string_value = '1.5'
float_value = float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))
######################################
#Complex Numbers
c1 = 1
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
##############################
#Boolean Values
#Python supports another type called Boolean; 
#a Boolean type can only be one of True or False
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))
#############################
#You can also convert strings into Booleans as long as the strings contain either
#True or False (and nothing else). 
status = bool(input('OK it is confirmed?: '))
print(status)
print(type(status))
#################################
#Arithmetic Operators
'''
Arithmetic operators are used to perform 
some form of mathematical operation such
as addition, subtraction, multiplication 
and division etc. In Python they are represented
by one or two characters.
'''
home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))
###########################################
'''
However, you may notice that we have missed out 
division with respect to
integers, why is this? 
It is because it depends on which division operator 
you use as to what the returned type actually is.
For example, if we divide the integer 100 by 20 
then the result you might
reasonably expect to produce might be 5; 
but it is not, it is actually 5.0:
'''    
print(100 / 20)
print(type(100 / 20))
'''
to ignore the fractional part then 
there is an alternative version of the divide operator
//. 
This operator is referred to as the integer division operator
'''
print(100 // 20)
print(type(100 // 20))
'''
But what if you are only interested in the remainder
 part of a division, the integer
division operator has lost that? 
Well in that case you can use the modulus operation %
'''
print('Modulus division 100 % 13:', 100 % 13)
print('Modulus division 3 % 2:', 3 % 2)
'''
A final integer operator we will look at is 
the power operator that can be used to
raise an integer by a given power, 
for example 5 to the power of 3. 
The power operator is '**'
'''
a = 5
b = 3
print(a ** b)
#Assignment Operators
'''
These assignment operators are actually referred to 
as compound operators  as they combine together a numeric operation 
 (such as add) with the assignment operator. 
 For example, the += compound operator 
 is a combination of the add operator and the = operator 
 '''
x = 0
x += 1 # has the same behaviour as x = x + 1
######################################
#None Value
#Python has a special type, 
#the NoneType, with a single value, None.
winner = None
print(winner is None)
#Alternatively you can also write:
print(winner is not None)
#Which will print out True only if the

winner = None
print('winner:', winner)
print('winner is None:', winner is None)
print('winner is not None:', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True
#######################################
#Flow of Control Using If Statements
#Comparison Operators
'''
Before exploring if statements we need to discuss comparison 
operators. These are operators that return Boolean values. 
They are key to the conditional elements
of flow of control statements such as if.
A comparison operator is an operator that performs 
some form of test and returns True of False.
'''

'''
Note that indentation, this is very important in Python; 
indeed, layout of the code is very, very important in Python. 
Indentation is used to determine how one piece of
code should be associated with another piece of the code.

'''
num = int(input('Enter a number: '))
if num > 0:
   print(num)

#Now let us give the indentation
num = int(input('Enter a number: '))
if num > 0:
   print(num)
   
#Else in an If Statement
num = int(input('Enter yet another number: '))
if num < 0:
  print('Its negative')
else:
  print('Its not negative')
  
#The Use of elif
savings = float(input("Enter how much you have in savings: "))
if savings == 0:
   print("Sorry no savings")
elif savings < 500:
   print('Well done')
elif savings < 1000:
   print('Thats a tidy sum')
elif savings < 10000:
   print('Welcome Sir!')
else:
   print('Thank you')
#########################################
#Iteration/Looping
#While Loop
'''
The while loop exists in almost all programming languages 
and is used to iterative
(or repeat) one or more code statements 
as long as the test condition (expression) is True
'''
count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1
       
    
 #######################################
#For Loop
# Loop over a set of values in a range
print('Print out values in a range')
for i in range(2,10):
   print(i)
   print('Done')
################################
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 16):
    if i == num:
      break
    print(i)
print('Done')
##########################
# Now use an 'anonymous' loop variable
for _ in range(0,10):
   print('.', end='')
   print()
########################
for _ in range(0,10):
   print('.', end='')
#############################
#Break Loop Statement
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
   if i == num:
     break
   print(i, ' ', end='')
print('Done')
######################
#location of print is changed
for i in range(0, 6):
   if i == num:
     break
   print(i, ' ', end='')
   print('Done')
##############################################
'''
Print all odd numbers from the given list using for loop 

    Define the start and end limit of the range.
    Iterate from start till the range in the list using for loop and 
    check if num % 2 != 0. 
    If the condition satisfies, then only print the number. 
'''


# Python program to print odd Numbers in given range
 
start, end = 4, 19
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")


##############################################

# Python program to print Even Numbers in given range
 
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 != 0:
        print(num)
################################################
# Python program to print all even numbers  in range
for even_numbers in range(4,15,2):
  #here inside range function first no denotes starting,
  #second denotes end and
  #third denotes the interval
    print(even_numbers,end=' ')
################################################
# Python program to print Even Numbers in given range
 
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")