#10.Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
Str1 = raw_input("enter the string: ")
Str2 = raw_input("enter the string: ")
c1 = 0
c2 = 0
for i in Str1:
    c1 += 1
for i in Str2:
    c2 += 1
if c1 == c2:
    print "both the strings lenght are equal"
elif c1 > c2:
    print "String1 is having largest lenght"
else:
    print "String2 is having largest lenght"
