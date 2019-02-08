#!/usr/bin/python

#Title: Assignment3---Question56
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Write a program to handle following exceptions using Try block.
#        a) IO Error while you try writing contents into the file that is opened in read mode only.
#        b) ValueError


#  a) IO Error
try:
    print('\n*****IOError example*****')
    file1=open('Q56.txt','r')
    print('File opened in read mode:',file1.name)
    y = input('Enter data to write into the file : ')
    file1.write(y)
    
except IOError:
    print("Error: The file need to be opened in write mode to write contents into it")
    
#  b) ValueError
try:
    print('\n*****ValueError example*****')
    x=input('Enter data to convert to integer : ')
    int(x)
except ValueError:
    print ('Error:String cannot be converted to integer')


    
