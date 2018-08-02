#11.	Python Program to Find the Sum of Digits in a Number
n = input("enter the number: ")
b = 0
while n>0:
    c = n%10
    b += c
    n /= 10
print b
