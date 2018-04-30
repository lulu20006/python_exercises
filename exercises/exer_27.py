#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

n=input()
if n=="Yes" or n=="yes" or n=="YES":
    print ("yes")
if n!="Yes" and n!="yes" and n!="YES":
    print ("no")