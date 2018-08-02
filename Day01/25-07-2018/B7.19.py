#19.	Python Program to Print an Inverted Star Pattern

n = input("enter the n value: ")
for i in range(n,0,-1):
    for j in range(i):
        print '*',
    print ''
