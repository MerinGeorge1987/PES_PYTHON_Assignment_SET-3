#!/usr/bin/python

#Title: Assignment3---Question53
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Open the file is read & write mode and apply following functions
#        a) All 13 functions mentioned in Tutorial File object table.


#Open the file in read & write mode    
file1=open('Q53.txt','r+')

#a) Functions for File Handling 
# Reference associated to file handle
print('The file handle opened at : ',file1)
# Name of the File
print('Name of the file opened is : ',file1.name)
# Status of the file
print('Is the file closed? : ',file1.closed)
# Mode of the file opened
print('Mode of the file opened : ',file1.mode)
# Read operation
print ('Read 10 bytes : ',file1.read(10))
# Position of file pointer
print ('File pointer is in : ',file1.tell())
# Change position of file pointer
file1.seek(30)
print ('File pointer is in : ',file1.tell())
# Read Line Operation
print ('Read Line operation : ',file1.readline())
# Write text into file
text='\nThis ia a newly added line.....'
file1.write(text)
#Close the file
file1.close()

#Open file in read mode
file1=open('Q53.txt','r')
#File descriptor associated to the file
print ('File descriptor : ',file1.fileno())
# Read multiple lines operation
print ('Read Line operation : ',file1.readlines())






