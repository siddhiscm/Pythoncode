#1. python Program to Add a Key-Value Pair to the Dictionary
D = {1:123}
D.update({2:1234})
print D


# 2.Python Program to Concatenate Two Dictionaries Into One
d1 = {1:123}
d2 = {2:1234}
d1.update(d2)
print d1

#3. Python Program to Check if a Given Key Exists in a Dictionary or Not
d1 = {1:123,2:234,3:123,3:134}
n = input("enter the key: ")
if n in d1:
    print "Yes %d is present in Dictionary"%n
else:
    print "No %d is not present in Dictionary"%n

#4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n)in the Form (x,x*x).
n = input("enter a range: ")
d1 = {}
for i in range(1,n+1):
    d1.update({i:i*i})
print d1


#5. Python Program to Sum All the Items in a Dictionary
d = {1:234,2:23,3:43}
c = list(d.values())
c1 = 0
for i in c:
    c1 += i
print "The sum of all the items in a dictionary is: ",c1


#6. Python Program to Multiply All the Items in a Dictionary
d = {1:2,2:3,3:4}
c = list(d.values())
c1 = 1
for i in c:
    c1 *= i
print "The sum of all the items in a dictionary is: ",c1

#7. Python Program to Remove the Given Key from a Dictionary
d = {1:234,2:12,3:34,4:23}
n = input("enter the key: ")
d.pop(n)
print d






    
