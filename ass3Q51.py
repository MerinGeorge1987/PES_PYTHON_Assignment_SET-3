#!/usr/bin/python

#Title: Assignment3---Question51
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:In a given directory search all text files for the pattern "Treasure". 
#        a) Find how many text files has the pattern.
#        b) Count how many times pattern repeats in each file
#        Note:Create at least 4 text files in a directory and keep the pattern in at least 2 files.Repeat the pattern in the file many times.

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
            
        





