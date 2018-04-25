import random

my_num =random.randint(1,100)

print("Please input a number from 1 to 100:") 
name = input()

is_correct = False

while(is_correct == False):
    if((name.isdigit())==False):
        print('It is not a number')
        name = input()
    elif( int (name) > 100 or int (name) < 1):
        print('Please input a number from 1 to 100')
        name = input()
    elif( int (name) < my_num):
        print('It is too low')
        name = input()
    elif( int (name) > my_num):
        print('It is too high')
        name = input()
    elif( int (name) == my_num):
        print('You are right')
        is_correct = True
        
    
    