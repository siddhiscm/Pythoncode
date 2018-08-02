#14.	Python Program to Check if a Number is a Palindrome
n = input("enter the number: ")
d = n
b = 0
while d>0:
    c = d%10
    b = b*10+c
    d /= 10
print b
if b == n:
    print "the given number is palindrome"
else:
    print "The given number is not a palindrome"
  
