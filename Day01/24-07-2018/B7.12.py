#12.	Python Program to Find the Smallest Divisor of an Integer
n = input("enter a number")
l = []
for i in range(n,0,-1):
    if n%i == 0:
        if i != 1:
            print i
            l.append(i)
l.sort()
print "smallest divisor is: ",l[0]
