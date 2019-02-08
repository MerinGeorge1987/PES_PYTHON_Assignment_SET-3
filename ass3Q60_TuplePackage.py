#!/usr/bin/python

#Title: Assignment3---Question60
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Tuple Package

#Summary:Repeat program 7 with Tuples 
def Q08():
    tup1=(10,20,30,40,50,60,70,80,90,100)
    print "Tuple:",tup1


    #a) Slicing operation
    print "\nSlicing operation:",tup1[0:9:3]

    #b) Repetition with  operator *
    print "Repeat tuple 10 times:",tup1*10

    #c) Read string 2 and concatenate with other string using + operator.
    tup2=('a','b','c')
    print "Tuple2",tup2
    print "Concatenated string:",tup1+tup2