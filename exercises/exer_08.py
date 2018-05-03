#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

'''
lines = []
words = input()
while words != ':w':
    line = lines.append(str(words).upper())
    words = input()

print(",".join(lines))
'''
s=input()
while s != '':
    print(str(s).upper())
    s=input()




