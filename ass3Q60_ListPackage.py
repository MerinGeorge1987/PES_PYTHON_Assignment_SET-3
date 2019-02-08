#!/usr/bin/python

#Title: Assignment3---Question60
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:List Package

#Create a list with at least 10 elements having integer values in it;
#       Print all elements
#       Perform slicing operations
#       Perform repetition with * operator
#      Perform concatenation with other list.
def Q07():
    list1=[10,20,30,40,50,60,70,80,90,100]
    print "List:",list1


    #a) Slicing operation
    print "\nSlicing operation:",list1[0:9:2]

    #b) Repetition with  operator *
    print "Repeat list 10 times:",list1*10

    #c) Read string 2 and concatenate with other string using + operator.
    list2=['a','b','c']
    print "List2",list2
    print "Concatenated string:",list1+list2