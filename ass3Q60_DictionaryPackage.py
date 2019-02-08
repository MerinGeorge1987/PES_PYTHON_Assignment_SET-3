#!/usr/bin/python

#Title: Assignment3---Question60
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Dictionary Package

def Q37():
    #Dictionary Creation
    dict1={'Year':'yy','Month':'mm','Date':'dd'}
    dict2={'Hour':'hh','Minute':'mm','Second':'ss'}
    dict3={'Country':'C','State':'S','District':'D'}

    #a) Compare dictionaries to determine the biggest.
    print "dict1:",dict1
    print "dict2:",dict2
    print "dict3:",dict3
    if cmp(dict1,dict2)>0 and cmp(dict1,dict3)>0:
        print dict1," is the greatest"
    elif cmp(dict2,dict1)>0 and cmp(dict2,dict3)>0:
        print dict2," is the greatest"
    elif cmp(dict3,dict1)>0 and cmp(dict3,dict1)>0:
        print dict3," is the greatest"
    else:
        print "All are equal"

    #b) Add new elements in to the dictionaries dict1, dict2
    dict1['None']='N'
    print "New dict1:",dict1

    dict2['None']='N'
    print "New dict2:",dict2

    #c) print the length of dict1,dict2,dict3.
    print "Length of dict1:",len(dict1)
    print "Length of dict2:",len(dict2)
    print "Length of dict3:",len(dict3)

    #d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.
    str1=str(dict1)
    str2=str(dict2)
    str3=str(dict3)
    print "Concatenate of dict1,dict2 & dict3:",str1+str2+str3

#Summary:Create 2 dictionaries as follows;
#        dict1 ={'Name':'Ramakrishna','Age':25}
#        dict2={'EmpId':1234,'Salary':5000}
#        Perform following operations   
#           a) Create single dictionary by merging dict1 and dict2
#           b) Update the salary to 10%
#           c) Update the age to 26
#           d) Insert the new element with key "grade" and assign value as "B1"
#           e) Extract and print all values and keys separately.
#           f) delete the element with key 'Age' and print dictionary elements.
def Q38():
    #Dictionary Creation
    dict1 ={'Name':'Ramakrishna','Age':25}
    dict2={'EmpId':1234,'Salary':5000}
    print "dict1:",dict1
    print "dict2:",dict2

    #a) Create single dictionary by merging dict1 and dict2
    dict1.update(dict2)
    print "Merged dictionary:",dict1

    #b) Update the salary to 10%
    sal=dict1['Salary']
    sal=sal*1.1
    dict1['Salary']=sal
    print "New Salary of employee ",dict1['EmpId'],"is",dict1['Salary']

    #c) Update the age to 26
    dict1['Age']=26
    print "Age of ",dict1['Name'],"changed to",dict1['Age']

    #d) Insert the new element with key "grade" and assign value as "B1"
    dict1['grade']='B1'
    print "Updated dictionary:",dict1

    #e) Extract and print all values and keys separately.
    print "Keys of the dictionary:",
    for x in dict1:
        print x,",",
    print "\nValues of the dictionary:",
    for x in dict1.values():
        print x,",",

    #f) delete the element with key 'Age' and print dictionary elements.
    del dict1["Age"]
    print "Updated dictionary:",dict1
    


    
   