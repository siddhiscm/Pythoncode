#9. Python Program to Accept Three Digits and Print all Possible Combinations from the Digits
n1 = input("enter the first number: ")
n2 = input("enter the second number: ")
n3 = input("enter the third number: ")
for i in range(n1+1):
    for j in range(n2+1):
        for k in range(n3+1):
            print i,j,k
