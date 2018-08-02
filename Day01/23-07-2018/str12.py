#12.	Python Program to Check if a String is a Palindrome or Not
Str = raw_input("Enter the string: ")
Str1 = Str[::-1]
if Str1 == Str:
    print "Palindrome"
else:
    print "Not a palindrome"
    
