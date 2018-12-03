#Title: Assignment3---Question46
#Author:Merin
#Version:1
#DateTime:29/11/2018 3:30pm
#Summary: Write a function to find the biggest of 4 numbers.
#         a) All numbers are passed as arguments separately (Required argument)
#         b) use default values for arguments(Default arguments)

#Function Body
def Biggest(a=10,b=20,c=30,d=40):
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
    

    
#Main Body
a=23;b=100;c=765;d=1

#a) All numbers are passed as arguments separately 
res=Biggest(a,b,c,d)
print "Biggest of all 4 numbers(%d,%d,%d,%d):"%(a,b,c,d),res

#b) use default values for arguments(Default arguments)
res=Biggest()
print "Biggest of all 4 numbers(10,20,30,40):",res









