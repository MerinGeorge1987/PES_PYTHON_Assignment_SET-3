#!/usr/bin/python

#Title: Assignment3---Question52
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Open existing text file and reverse its contents. i.e
#        a) print the last line as first line and first line as last line (Reverse the lines of the file)
#        b) print characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )


#a) print the last line as first line and first line as last line (Reverse the lines of the file)
print "Lines of the file reversed:"       
file1=open('test.txt','r')
lines=file1.readlines()
x=len(lines)-1
while x>=0:
    print lines[x] 
    x=x-1
file1.close()

#b) print characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )
print "Characters of the file reversed:"       
file1=open('test.txt','r')
lines=file1.read()
x=len(lines)-1
while x>=0:
    print lines[x], 
    x=x-1
file1.close()



