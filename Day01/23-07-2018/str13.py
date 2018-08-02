#13.	Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
Str = raw_input("Enter the string: ")
c1 = 0
c2 = 0
for i in Str:
    if (i.islower()):
        c1 += 1
    elif (i.isupper()):
        c2 += 1
print "The number of lowercase character is: ",c1
print "The number of uppercase character is: ",c2
