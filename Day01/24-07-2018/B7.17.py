# 17. Python Program to Read a Number n and Print the Natural Numbers Summation Pattern
n = input("enter the number: ")
c = 0
for i in range(n+1):
    c += i
print "The Natural Numbers Summation Pattern is: ",c
