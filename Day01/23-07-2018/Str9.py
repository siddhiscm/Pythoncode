#9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
Str = raw_input("enter the string: ")
w = 1
c = 0
for i in Str:
    c += 1
    if i == ' ':
        w += 1
print "the number of words in the string is: ",w
print "the number of character in the string is:",c
