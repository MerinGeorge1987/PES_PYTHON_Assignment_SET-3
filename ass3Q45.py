#Title: Assignment3---Question45
#Author:Merin
#Version:1
#DateTime:29/11/2018 3:15pm
#Summary: Write a program to check given string is Palindrome or not. (Use function Concepts and Required keyword, Default parameter concepts)i.e Reverse the given string and check whether it is same as original string, if so then it is palindrome.
#         Example: String "malayalam" when reversed will be "malayalam" hence palindrome.

#Function Body
def Palindrome(check):
    #Finding reverse of string
    reverse=check[::-1]
    #Comparing the strings & printing the result
    if cmp(check.lower(),reverse.lower())==0:
        return (1)
    else:
        return(0)
    
#User Input
string=raw_input('Enter string to be checked as palindrome or not:')

#Function call
res=Palindrome(string)
if res==1:
    print "%s is a palindrome"%string
else:
    print "%s is not a palindrome"%string







