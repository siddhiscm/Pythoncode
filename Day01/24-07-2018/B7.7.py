#7. Python Program to Print all Numbers in a Range Divisible by a Given Number
n = input("enter a number")
for i in range(1,n+1):
    if n%i == 0:
        print i,
