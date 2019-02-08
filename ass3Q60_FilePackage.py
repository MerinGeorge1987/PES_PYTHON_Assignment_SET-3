#!/usr/bin/python

#Title: Assignment3---Question60
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Create a package of all programs you have done in earlier.
#        f. All programs related to Files  -- FilePackage



#Write a program to perform following file operations
#a) Open the file in read mode and read all its contents on to STDOUT.
#b) Open the file in write mode and enter 5 new lines of strings in to the new file.
#c) Open file in Append mode and add 5 lines of text into it.
def Q49(filename):
    #a) Open the file in read mode and read all its contents on to STDOUT.
    file1=open(filename,'r')
    import sys
    sys.stdout.write(file1.read())
    file1.close()

    #b) Open the file in write mode and enter 5 new lines of strings in to the new file.
    file1=open(filename,'w')
    file1.write("Line1 string\nLine2 string\nLine3 string\nLine4 string\nLine5 string")
    file1.close()

    #c) Open file in Append mode and add 5 lines of text into it.
    file1=open(filename,'a')
    file1.write("\nLine1 append string\nLine2 append string\nLine3 append string\nLine4 append string\nLine5 append string")
    file1.close()



#Write a program to open the existing file in read mode and perform following tasks,
#        a) Rad 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
#        b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
#        c) Open the file in read mode and start printing the contents from 5th line onwards.   
def Q50(filename):
    #a) Read 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.
    print("\nRead 10 character at a time and then print its current position of file object. Repeat this operation till the EOF.")
    file1=open(filename,'r')
    while True:
        ch=file1.read(10)
        if len(ch)!=10:
            break
        else:
            print ("Read operation:",ch)
            p=file1.tell()
            print ("Current position:",p)
            file1.close()
    
    #b) Reset the file pointer after reading 100 Character from file (Use Seek function to reset)
    print ("\nReset the file pointer after reading 100 Character from file")
    file1=open(filename,'r')
    while True:
        ch=file1.read(10)
        p=file1.tell()
        print ("Read operation:",ch)
        print ("Current position:",p)

        if p>100:
            file1.seek(0)
            break
    print ("Position resetted to ", file1.tell())
    file1.close()

    #c) Open the file in read mode and start printing the contents from 5th line onwards.
    print ("Open the file in read mode and start printing the contents from 5th line onwards")       
    file1=open(filename,'r')
    lines=file1.readlines()
    x=5
    while x<len(lines):
        print ("Line %d:"%x,lines[x])
        x=x+1
    file1.close()
    
#In a given directory search all text files for the pattern "Treasure". 
#        a) Find how many text files has the pattern.
#        b) Count how many times pattern repeats in each file
#        Note:Create at least 4 text files in a directory and keep the pattern in at least 2 files.Repeat the pattern in the file many times.
def Q51():
    import glob
    import re
    #a) Find how many text files has the pattern.
    y=0
    for filename in glob.glob('*.txt'):
        file1=open(filename,'r')
        lines=file1.readlines()
        for x in range(len(lines)-1):
            if lines[x].count('Treasure')>0:
                y=y+1
                break
        file1.close()
    print "Number of files with pattern:",y
    

    #b) Count how many times pattern repeats in each file
    for filename in glob.glob('*.txt'):
        y=0
        file1=open(filename,'r')
        lines=file1.readlines()
        for x in range(len(lines)-1):
            if lines[x].count('Treasure')>0:
                y=y+lines[x].count('Treasure')
            print filename," has the pattern %d times"%y
        file1.close()


#Open existing text file and reverse its contents. i.e
#        a) print the last line as first line and first line as last line (Reverse the lines of the file)
#        b) print characters of file from last character of file till the first character of the file.(Reverse entire contents of  file )        
def Q52():
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
    
    
#Open the file is read & write mode and apply following functions
#        a) All 13 functions mentioned in Tutorial File object table.
def Q53():
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

