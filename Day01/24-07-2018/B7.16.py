#16.	Python Program to Read a Number n And Print the Series "1+2+…..+n= "
n = input("enter a number: ")
c = ''
for i in range(1,n+1):
    c = c + '+' + str(i)
print c[1:]

