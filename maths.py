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

    
    
#Main Body
import calc

#a) Write a new program in file "maths.py" such that you import functions of file "calc.py" to your new program
num1=20;num2=10
print "Sum of %d & %d="%(num1,num2),calc.Add(num1,num2)
print "Difference of %d from %d="%(num2,num1),calc.Subtract(num1,num2)
print "On multiplying %d & %d="%(num1,num2),calc.Multiply(num1,num2)
print "square root of %d:"%num1,calc.SquareRoot(num1)
print "On dividing %d by %d="%(num1,num2),calc.Divide(num1,num2)
print "On dividing (floor division) %d by %d="%(num1,num2),calc.FloorDiv(num1,num2)
print "Reminder on dividing %d by %d="%(num1,num2),calc.Modulus(num1,num2)
if calc.Prime(num1)==0:
    print "%d is a prime number"%num1
else:
    print "%d is not a prime number"%num1
print "Fibonacci Series with %d elements:"%num1
calc.fib(num1)

#b) Use From <module> import <function> statement to import only few function  from calc module.
from calc import SquareRoot,Prime,fib
print "\n\nsquare root of %d:"%num2,SquareRoot(num2)
if calc.Prime(num2)==0:
    print "%d is a prime number"%num2
else:
    print "%d is not a prime number"%num2
print "Fibonacci Series with %d elements:"%num2
calc.fib(num2)
    












