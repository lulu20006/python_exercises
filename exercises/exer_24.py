# Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line. 
# Hints: Use len() function to get the length of a string

l=input().split(',')
n = str (l[0])
m = str (l[1])
if len(n)>len(m):
    print (n)
if len(n)<len(m):
    print (m)
if len(n)==len(m):
    print(n)
    print(m)

