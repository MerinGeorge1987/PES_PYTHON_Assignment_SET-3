#Title: Assignment3---Question47
#Author:Merin
#Version:1
#DateTime:30/11/2018 4:00pm
#Summary:Write function to extend the tuple with elements of list.
#        Pass list and Tuple as parameter to the function.

#Function Body
def Extend(tup1,list1):
    list2=list1
    list2.extend(tup1)
    tup1=tuple(list2)
    return(tup1)
    

    
#Main Body
tup1=(1,2,3)
list1=['a','b','c']
print "Tuple:",tup1
print "List:",list1
tup1=Extend(tup1,list1)
print "Extended Tuple with elements of list:",tup1










