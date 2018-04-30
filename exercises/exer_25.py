#Define a function that can accept an integer number as input and print the "It is an even number" 
#if the number is even, otherwise print "It is an odd number".
#Hints: Use % operator to check if a number is even or odd.

n= int (input())
if n%2==0:
    print ("It is an even number")
if n%2==1:
    print ("It is an odd number")