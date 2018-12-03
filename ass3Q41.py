#Title: Assignment3---Question41
#Author:Merin
#Version:1
#DateTime:26/11/2018 2:00pm
#Summary:Using calendar module perform following operations.
#        a) Print the 2016 calendar with space between months as 10 characters.
#        b) How many leap days between the years 1980 to 2025.
#        c) Check given year is leap year or not. 
#        d) print calendar of any specified month of the year 2016.




#import time & calendar module
import time
import calendar

#a)2016 calendar with space between months as 10 characters.
print "Calendar for 2016:"
print calendar.calendar(2016,0,0,10)

#b)leap days between the years 1980 to 2025.
print "Leap days between 1980 to 2025:",calendar.leapdays(190, 2025)

#c)Check given year is leap year or not.
year=input("Enter an year which needs to checked as leap year or not:")
if calendar.isleap(year):
    print ("The year is leap") 
else:
    print ("The year is not leap")

#d)calendar of any specified month of the year 2016.
month=input("Enter the month (in number) for which 2016 calendar is needed:")
print calendar.month(2016,month)
