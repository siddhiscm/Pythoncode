#4.	Python Program to Reverse a Given Number
n = input("enter a number: ")
c = 0
b = 0
print n
while n>0:
    c = n%10
    b = b*10+c
    n = n/10
print b

