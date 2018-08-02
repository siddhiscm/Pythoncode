#16.Python Program to Calculate the Number of Digits and Letters in a String
n = raw_input("enter the string: ")
c1 = 0
c2 = 0
for i in n:
    if i.isdigit():
        c1+=1
    if i.isalpha():
        c2+=1
print "The string contains %d digits." %c1
print "The string contains %d Letters." %c2
