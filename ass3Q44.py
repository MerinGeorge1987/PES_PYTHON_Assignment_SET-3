#Title: Assignment3---Question44
#Author:Merin
#Version:1
#DateTime:01/12/2018 3:00pm
#Summary:Write a program with lambda function to perform following.
#        a) Perform all the operations of basic calculator (Add, Sub, Multiply, Divide, Modulus, Floor division)


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


