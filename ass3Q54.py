#!/usr/bin/python

#Title: Assignment3---Question54
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Write a program to handle the following exceptions in you program.
#        a) KeyboardInterrupt
#        b) NameError
#        c) ArithmeticError
#        Note: Make use of try, except, else: block statements.


try:
    x = int(input("Enter any first number : "))
    y = int(input("Enter any second number : "))
    print ("The values given are ", x,y)
    res = x/y
    print ("The result of two divided numbers are ", res)
#  a) KeyboardInterrupt
except KeyboardInterrupt:
    print("W: interrupt received, stopping....")
#  b) NameError
except NameError:
    print ("You are trying to access a label which is not defined")
#  c) ArithmeticError
except ArithmeticError:
    print ('This is an example of catching ArithmeticError')
else:
    print ("Else: execute only if the error is not thrown in program")
finally:
    print ("Finally: I will be executed all the times, irrespective of error thrown or not")


    
