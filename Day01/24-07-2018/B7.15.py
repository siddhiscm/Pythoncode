#15.Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50
n = input("enter the number: ")
for i in range(1,n+1):
    if (i%2 != 0) and (i%3 != 0):
        print i,
        
