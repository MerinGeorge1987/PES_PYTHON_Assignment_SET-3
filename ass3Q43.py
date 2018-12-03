#Title: Assignment3---Question43
#Author:Merin
#Version:1
#DateTime:26/11/2018 2:30pm
#Summary:Write a program to search given element from the list. Use your own function to search an element from list.
#        Note: Function should receive variable length arguments and search each of these arguments present in the list.

#Function body
def search(element,length):
    flag=0
    for x in range(len(list1)):
        if length==len(list1[x]):
            if element.lower()==list1[x].lower():
                
                flag=flag+1
    if flag==0:
        print "Search failed"
    else:
        print "Found",element
             

#main body
list1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
element=raw_input('Enter the element(any week day) to be searched:')
length=len(element)

#function call
search(element,length)

