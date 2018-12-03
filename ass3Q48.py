#Title: Assignment3---Question48
#Author:Merin
#Version:1
#DateTime:30/11/2018 4:00pm
#Summary:Create a Calculator with the following functions.
#        a) Addition/subtraction/multiplication and division of two numbers (Note: Create separate function for each operation)
#        b) Find square root of a given number.(Use keyword arguments in your function)
#        c) Create a list of sub strings from a given string, such that sub strings are created with given character. i.e. String = "Pack: My: Box: With: Good: Food"
#        Create sub strings with the delimiter character ":" such that the following sub strings are created. substrlist=[Pack, My, Box, With, Good, Food]
#        Note : Function should take at least 2 parameters ( Main string and delimiter character)return value from function will be list of substring.


#Function Body for subquestion a)
def Add(num1,num2):
    return(num1+num2)
def Subtract(num1,num2):
    return(num1-num2)
def Multiply(num1,num2):
    return(num1*num2)
def Divide(num1,num2):
    return(num1/num2)
    
#Function Body for subquestion b)
def SquareRoot(num):
    import math
    return math.sqrt(num)

#Function Body for subquestion c)
def Substring (string,delimiter):
    substrlist=string.split(delimiter)
    return substrlist
    
    
#Main Body
#a) Addition/subtraction/multiplication and division of two numbers (Note: Create separate function for each operation)
num1=20;num2=10
print "Sum of %d & %d="%(num1,num2),Add(num1,num2)
print "Difference of %d from %d="%(num2,num1),Subtract(num1,num2)
print "On multiplying %d & %d="%(num1,num2),Multiply(num1,num2)
print "On dividing %d by %d="%(num1,num2),Divide(num1,num2)

#b) Find square root of a given number.(Use keyword arguments in your function)
print "square root of %d:"%num1,SquareRoot(num=num1)

#c) Create a list of sub strings from a given string, such that sub strings are created with given character.
string=raw_input("Enter a string:")
delimiter=raw_input ("Enter delimiter using which substrings need to be created:")
substrlist=Substring(string,delimiter)
print "Sub string list:",substrlist










