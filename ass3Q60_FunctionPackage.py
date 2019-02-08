#!/usr/bin/python

#Title: Assignment3---Question60
#Author:Merin
#Version:1
#DateTime:03/12/2018 3:00pm
#Summary:Create a package of all programs you have done in earlier.
#        e. All programs related to Functions - FunctionPackage


#Write a program to generate a Fibonacci series using a function called fib(n), 
#        a) Where n is user specified argument specifies number of elements in the series.

def Q42():
    n=input("Number of elements needed in the Fibonacci Series:")
    print "Fibonacci Series:",
    if n==1:
        print "0"
    elif n==2:
        print "0,1"
    else:
        print "0,1",
        a=0;b=1
        for x in range(3,n+1):
            c=a+b
            print ",",c,
            a=b;b=c
    
    
#Write a program to search given element from the list. Use your own function to search an element from list.
#        Note: Function should receive variable length arguments and search each of these arguments present in the list.

def Q43():
    list1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    element=raw_input('Enter the element(any week day) to be searched:')
    length=len(element)
    flag=0
    for x in range(len(list1)):
        if length==len(list1[x]):
            if element.lower()==list1[x].lower():
                
                flag=flag+1
    if flag==0:
        print "Search failed"
    else:
        print "Found",element
        
#Write a program with lambda function to perform following.
#        a) Perform all the operations of basic calculator (Add, Sub, Multiply, Divide, Modulus, Floor division)
def Q44():
    #add
    add = lambda x,y: x * y

    #subtract
    diff = lambda x,y: x - y

    #multiply
    multiply = lambda x,y: x * y

    #divide
    divide = lambda x,y: x / y

    #modulus
    mod= lambda x,y: x % y

    #floor division
    floordiv = lambda x,y: x//y

    print "Sum of 10 & 20:",add(10,20)
    print "Difference of 10 from 30:",diff(30,10)
    print "On multiplying 20 with 25:",multiply(20,25)
    print "On dividing 30 by 4:",divide(30,4)
    print "Reminder on dividing 30 by 4:",mod(30,4)
    print "(Floor division) On dividing 30 by 4:",floordiv(30,4)
    
    
#Write a program to check given string is Palindrome or not. (Use function Concepts and Required keyword, Default parameter concepts)i.e Reverse the given string and check whether it is same as original string, if so then it is palindrome.
#         Example: String "malayalam" when reversed will be "malayalam" hence palindrome.

def Q45(check):
    #User Input
    string=raw_input('Enter string to be checked as palindrome or not:')
   
    #Finding reverse of string
    reverse=check[::-1]
    #Comparing the strings & printing the result
    if cmp(check.lower(),reverse.lower())==0:
        res=1
    else:
        res=0
    #Output
    if res==1:
        print "%s is a palindrome"%string
    else:
        print "%s is not a palindrome"%string
    

    
#Write a function to find the biggest of 4 numbers.
#         a) All numbers are passed as arguments separately (Required argument)
#         b) use default values for arguments(Default arguments)

def Q46(a=10,b=20,c=30,d=40):
    if a>b and a>c and a>d:
        return(a)
    elif b>a and b>c and b>d:
        return(b)
    elif c>a and c>b and c>d:
        return(c)
    elif d>a and d>b and d>c:
        return(d)
    else:
        return(0)
    

    
#Write function to extend the tuple with elements of list.
#        Pass list and Tuple as parameter to the function.
def Q47(tup1,list1):
    list2=list1
    list2.extend(tup1)
    tup1=tuple(list2)
    return(tup1)
    
#Create a Calculator with the following functions.
#        a) Addition/subtraction/multiplication and division of two numbers (Note: Create separate function for each operation)
#        b) Find square root of a given number.(Use keyword arguments in your function)
#        c) Create a list of sub strings from a given string, such that sub strings are created with given character. i.e. String = "Pack: My: Box: With: Good: Food"
#        Create sub strings with the delimiter character ":" such that the following sub strings are created. substrlist=[Pack, My, Box, With, Good, Food]
#        Note : Function should take at least 2 parameters ( Main string and delimiter character)return value from function will be list of substring.

#Function Body for subquestion a)
def Q48Add(num1,num2):
    return(num1+num2)
def Q48Subtract(num1,num2):
    return(num1-num2)
def Q48Multiply(num1,num2):
    return(num1*num2)
def Q48Divide(num1,num2):
    return(num1/num2)
    
#Function Body for subquestion b)
def Q48SquareRoot(num):
    import math
    return math.sqrt(num)

#Function Body for subquestion c)
def Q48Substring (string,delimiter):
    substrlist=string.split(delimiter)
    return substrlist
    
    

    

    



             




    
