# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:40:48 2023

@author: Lenovo
"""

#python for nlp
#NLP full form in data science is Natural Language Processing
#firstly install regex pakage from anaconda navigator
import re
text = ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = r'\d\d\d\d\d\d\d\d\d\d'
matches = re.findall(pattern, text)
matches
#instead of writing '\d' this many times we can also write it as
pattern = r'\d{10}'
matches = re.findall(pattern, text)
matches #gives the same out put as first
#this finds the number in indian patter but if we have the number in other form eg.100-345-4566
#to get that : pattern = \d{3}-\d{3}-\d{4}
pattern = r'\(\d{3}\)-\d{3}-\d{4}'  #We have put '\( , \)' to get as it is number with parenthesis
matches = re.findall(pattern, text)
matches
#if we want both the patherns
#use: '|' (or) sign also known as 'Pipe' in machine learing.
pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'  #We have put '\( , \)' to get as it is number with parenthesis
matches = re.findall(pattern, text)
matches #Gives both the pattern numbers
#output : ['9991116666', '(999)-333-7777']

#######################################################################
'''Lets try some other text
   A protracted; legal battle; over a 32-carat;
  Golconda diamond-
  
  If we want any charecter except ; and - 
  The pattern will be [^;-]
  goto regular expressing window and type [^;-]
  '^' : indicates except (Acts as a filter)
'''
text = '''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''
pattern = r'[^;-]'  # ^ - Except ,but compulasory has to written in square brackets
matches = re.findall(pattern, text)
matches

###########################################################################

#finding in some other text file
#to find only some specific text or line
#pattern = r'Note 1 - [^\n]+'
text = '''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.'''
pattern = r'Note \d - [^\n]'  #using ^\n omly one line will be extracted
pattern = r'Note 1 - [^\n]+'
matches = re.findall(pattern, text)
matches

#now we only want 'Summary of Significant Accounting Policies' as a output
#we will use (...) :Capture every thing enclosed
pattern = r'Note \d - ([^\n]+)' #only the content in the paranthesis will be displayed
matches = re.findall(pattern,text)
matches

###############################################################################

#lets take another example
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern = r'FY\d{4} Q\d'
matches = re.findall(pattern, text)
matches

pattern = r'FY\d{4} Q[1234]'
matches = re.findall(pattern, text)
matches
#can also be written as pattern = r'FY\d{4} Q\d'
pattern = r'FY\d{4} Q[1-4]'
matches = re.findall(pattern, text)
matches
#but if in some cases the case of alphabets is not same for eg some palces it is fy and some places it is FY
#then we use re.IGNORECASE
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''
pattern = r'FY\d{4} Q[1234]'
matches = re.findall(pattern,text,re.IGNORECASE)
matches

pattern = r'FY\d{4} Q[1234]|fy\d{4} Q[1234]' #both will be displayed
matches = re.findall(pattern,text)
matches 
#output: ['FY2021 Q1', 'fy2020 Q4'] 
#############33
#Now if we only want ['2021 Q1', '2020 Q4'] 
#Use parenthesis to capture only that part
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern = r'FY(\d{4} Q\d)'
matches = re.findall(pattern, text)
matches
#output : ['2021 Q1', '2020 Q4', '2021 Q1', '2020 Q4']

##########################################################################

#noe let us assume that we want to find financial number (money related)
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
pattern = r'\$[0-9\.]+'
matches = re.findall(pattern, text)
matches
#Now if i dont want $ sign
pattern = r'\$([0-9\.]+)'
matches = re.findall(pattern, text)
matches

#################################################################################
 
























