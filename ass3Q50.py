#!/usr/bin/python

#Title: Assignment3---Question50
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Write a program to open the existing file in read mode and perform following tasks,
#        a) Rad 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
#        b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
#        c) Open the file in read mode and start printing the contents from 5th line onwards.





#a) Read 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
print"\nRead 10 character at a time and then print its current position of file object. Repeat this operation till the EOF."
file1=open('test.txt','r')
while True:
    ch=file1.read(10)
    if len(ch)!=10:
        break
    else:
        print "Read operation:",ch
        p=file1.tell()
        print "Current position:",p
file1.close()
    
#b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
print "\nReset the file pointer after reading 100 Character from file"
file1=open('test.txt','r')
while True:
    ch=file1.read(10)
    p=file1.tell()
    print "Read operation:",ch
    print "Current position:",p

    if p>100:
        file1.seek(0)
        break
print "Position resetted to ", file1.tell()
file1.close()

#c) Open the file in read mode and start printing the contents from 5th line onwards.
print "Open the file in read mode and start printing the contents from 5th line onwards"       
file1=open('test.txt','r')
lines=file1.readlines()
x=5
while x<len(lines):
    print "Line %d:"%x,lines[x] 
    x=x+1
file1.close()

