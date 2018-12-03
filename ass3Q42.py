#Title: Assignment3---Question42
#Author:Merin
#Version:1
#DateTime:26/11/2018 9:50pm
#Summary:Write a program to generate a Fibonacci series using a function called fib(n), 
#        a) Where ‘n’ is user specified argument specifies number of elements in the series.




#Function Body
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
    
    

#Main Body

#User Input
n=input("Number of elements needed in the Fibonacci Series:")

#Function Call
print "Fibonacci Series:",
fib(n)
