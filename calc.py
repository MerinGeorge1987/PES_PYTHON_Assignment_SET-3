#Title: Assignment3---Question58
#Author:Merin
#Version:1
#DateTime:30/11/2018 10:00pm
#Summary:Create file called  "calc.py" which has following functions
#        i) functions to add 2 numbers
#        ii) function to find diff of 2 numbers
#        iii) function to multiply 2 numbers
#        iv) all maths operations ( sqrt, div, floor div, modulus, primenumber)
#        v) Fibonacci series
        
#        a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
#        b) Use From <module> import <function> statement to import only few function  from calc module.


#i) functions to add 2 numbers
def Add(num1,num2):
    return(num1+num2)

#ii) function to find diff of 2 numbers
def Subtract(num1,num2):
    return(num1-num2)
#iii)function to multiply 2 numbers
def Multiply(num1,num2):
    return(num1*num2)

#iv) all maths operations ( sqrt, div, floor div, modulus, primenumber)
#sqrt
def SquareRoot(num):
    import math
    return math.sqrt(num)
#div
def Divide(num1,num2):
    return(num1/num2)
#floor div
def FloorDiv(num1,num2):
    return(num1//num2) 
#modulus
def Modulus(num1,num2):
    return(num1%num2)
#prime number
def Prime(num1):
    x=2;flag=0
    while x<=num1/2:
        if num1%x==0:
            flag=flag+1
        x=x+1
#flag=0 means prime & flag>0 means non-prime        
    return(flag) 

#v) Fibonacci series
def fib(n):
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



    










