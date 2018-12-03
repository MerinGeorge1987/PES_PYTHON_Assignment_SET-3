#!/usr/bin/python

#Title: Assignment3---Question55
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Write a program for converting weight from Pound to Kilo grams.
#        a) Use assertion for the negative weight.
#        b) Use assertion to weight more than 100 KG

try:
    p=input("Enter the weight in pounds:")
    assert p>=0
    kg=p*0.45359237
    assert kg>100
    print "weight in kg:",kg
except AssertionError,e:
    print "Either negative or less than 100kg"
            
        





