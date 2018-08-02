# 5.	Python Program to Count the Number of Vowels in a String
str1 = raw_input("enter the string: ")
c = 0
for i in str1:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        c += 1
print "The string has %i vowels in their string" %c
