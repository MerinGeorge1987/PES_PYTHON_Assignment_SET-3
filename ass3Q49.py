#!/usr/bin/python

#Title: Assignment3---Question49
#Author:Merin
#Version:1
#DateTime:03/12/2018 2:50pm
#Summary:Write a program to perform following file operations
#        a) Open the file in read mode and read all its contents on to STDOUT.
#        b) Open the file in write mode and enter 5 new lines of strings in to the new file.
#        c) Open file in Append mode and add 5 lines of text into it.

#a) Open the file in read mode and read all its contents on to STDOUT.
file1=open('test.txt','r')
import sys
sys.stdout.write(file1.read())
file1.close()

#b) Open the file in write mode and enter 5 new lines of strings in to the new file.
file1=open('test.txt','w')
file1.write("Line1 string\nLine2 string\nLine3 string\nLine4 string\nLine5 string")
file1.close()

#c) Open file in Append mode and add 5 lines of text into it.
file1=open('test.txt','a')
file1.write("\nLine1 append string\nLine2 append string\nLine3 append string\nLine4 append string\nLine5 append string")
file1.close()



