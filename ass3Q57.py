#!/usr/bin/python

#Title: Assignment3---Question57
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Try implementing atleast any 5 exceptions in you program.


#  a) IO Error
try:
    x = input("Enter first number :")
    assert int(x)>10
    y = input("Enter second number : ")
    print ("The values given are ", x,y)   
    
    res = int(x)/int(y)
    print ("The result of two divided numbers are ", res)
    z = input("Enter third number : ")
    res=int(x)/z
    print ("The result of two divided numbers are ", res)
    
    print ("The final result:",result)

#This error will be triggered on entering a string instead of number for x or y    
except ValueError:
    print ('Error:Only number is accepted as input')

#This error will be triggered on assigning '0' to y
except ZeroDivisionError:
    print('Error: Cannot divide by zero')
    
# This error will be triggered on providing x<=10    
except AssertionError:
    print('First Number should be greater than 10')
        
except NameError:
    print('Unknown Variable')
    
except TypeError:
    print('Division can be applied only on numbers')
    
   
    
   