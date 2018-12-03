#Title: Assignment3---Question59
#Author:Merin
#Version:1
#DateTime:1/12/2018 11:30am
#Summary:Create file called "stringop.py" which has following functions
#        i) functions to sort numbers(Use loops for  sorting, do not use built in function)
#        ii) function to search given element through binary search method.(Refer to net for the Binary search algorithm)
#        iii) function to reverse the given string 
#        Write new program in file strpackage.py such that you import functions of file "stringop.py" to your new program



#new program in file strpackage.py such that you import functions of file "stringop.py" to your new program

import stringpop

#Call Sort function
n=[12,43,76,3,90,68,82,16]
print "Original List:",n
stringpop.SortList(n)

#Call Search function
s=input("Enter an element which needs to be searched:")
res=stringpop.binarySearch(n,0,7,s)
if res==-1:
    print "%d is not found"%s
else:
    print "%d is found at index %d"%(s,res)


#Call reverse function
st=input("Enter a string (within quotes):")
stringpop.ReverseString(st)

  



    










