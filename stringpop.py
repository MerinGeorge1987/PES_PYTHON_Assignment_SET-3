#Title: Assignment3---Question59
#Author:Merin
#Version:1
#DateTime:1/12/2018 11:30am
#Summary:Create file called "stringop.py" which has following functions
#        i) functions to sort numbers(Use loops for  sorting, do not use built in function)
#        ii) function to search given element through binary search method.(Refer to net for the Binary search algorithm)
#        iii) function to reverse the given string 
#        Write new program in file strpackage.py such that you import functions of file "stringop.py" to your new program


#i) functions to sort numbers
def SortList(num):
    for x in range(len(num)-1,0,-1):
        for i in range(x):
            if num[i]>num[i+1]:
                temp = num[i]
                num[i] = num[i+1]
                num[i+1] = temp
    print "Sorted List:",num

#ii) function to search given element through binary search method
def binarySearch (list1, startIndx, stopIndx, search):
    if stopIndx >= startIndx:
        mid = (startIndx + stopIndx) /2
  
        # If element is present at the middle itself 
        if list1[mid] == search: 
            return mid
           
        # If element is smaller than mid then search in the left half
        elif list1[mid] > search: 
            return binarySearch(list1, startIndx, mid-1, search) 
  
        # Else search in the right half 
        else: 
            return binarySearch(list1, mid+1, stopIndx, search) 
  
    else: 
        # Element is not present in the list1ay 
        return -1


#iii) function to reverse the given string
def ReverseString(string):
    reverse=string[::-1]
    print "Reverse of '%s' is '%s'"%(string,reverse)
  



    










