#1. Write a Python function to find the Max of three numbers.

'''
def greatest(a,b,c):
    if a>b and a>c:
        print "a is greatest number"
    elif b>c:
        print "b is greatest number"
    else:
        print "C is greatest number"
    return

greatest(12,32,10)

'''


#2. Write a Python function to sum all the numbers in a list.(8, 2, 3, 0, 7)

'''
a = list(input("enter the list elements: "))
def listsum():
    c = 0
    for i in a:
        c = c + i
    print c
    return
listsum()
'''



#3. Write a Python function to check whether a number is perfect or not. (6,28,468)

'''
a = input("enter the number: ")
def perfect():
    c = 0
    for i in range(1,a):
        if a%i == 0:
            c = c+i
            pass
        pass
    if a == c:
        print "it is perfect number"
    else:
        print "it is not a perfect number"

perfect()
'''


#4. Write a Python function to multiply all the numbers in a list.


'''
a = list(input("enter the list elements: "))
def listmul():
    c = 1
    for i in a:
        c = c * i
    print c
    return
listmul()
'''


#5. Write a Python program to reverse a string. #Sample String : "1234abcd"
                                                #Expected Output : "dcba4321"

'''
a = raw_input("enter the string: ")
def reverse():
    b = ''
    for i in range((len(a)-1),-1,-1):
        b = b+a[i]
    print b
reverse()
'''

#6. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

'''
a = input("enter the number: ")
def fact(b):
    c = 1
    for i in range(b,0,-1):
        c = c*i
    print c
fact(a)
'''


#7. Write a Python function to check whether a number is in a given range.

'''
a = input("enter a number: ")
def grange(b):
    if b in range(1,250):
        print "Given number %d is in with a range" %b
grange(a)

'''


#8. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output : 
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

'''
d = raw_input("enter a string: ")
def lwrupr(c):
    d_lower=0
    d_upper=0
    for i in c:
        if i.isupper():
            d_lower += 1
        if i.islower():
            d_upper += 1
    print "No. of Upper case characters : ",d_upper
    print "No. of Lower case Characters : ",d_lower
lwrupr(d)
'''


#9. Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

'''
a = list(input("enter the list element: "))
def list2():
    print "sample list: ",a
    print "unique list: ", list(set(a))
list2()
'''


#10. Write a Python function that takes a number as a parameter and check the number is prime or not.

'''
n = input("enter a number: ")
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                print n,"it is not a prime number"
                break
        else:
            print n,"it is a prime number"
                 
prime(n)
'''

#11. Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
#Expected Result : [2, 4, 6, 8]

'''
n = list(input("enter a list element: "))
def evenlist(b):
    c = []
    print "even numbers from given list: ",
    for i in b:
        if i%2 == 0:
            c = c+list(str(i))
    print c
evenlist(n)
'''

#12. Write a Python function that checks whether a passed string is palindrome or not.


'''
n = raw_input("enter a string: ")
def palindrome(b):
    a = b[::-1]
    if a==b:
        print "palindrome"
    else:
        print "Not a palindrome"
palindrome(n)

'''

#13. Write a Python function to create and print a list where the values are square of numbers between 1 and 30

'''
n = list(input("enter a list: "))
def list1():
    b = []
    d = 0
    for i in n:
        d = i**2
        b.append(d)
    print b
list1()
'''    

#14. Write a Python function to check whether a string is a pangram or not.
#For example : "The quick brown fox jumps over the lazy dog"

'''
string = raw_input("enter a string: ")
b = string.lower()
def pangram():
    d = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    a = list(set(b))
    for i in a:
        if i == ' ':
            a.remove(i)
    a.sort()
    if a == d:
        print "it is pangram"
    else:
        print "it is not a panagram"

pangram()
'''

# 15. Write a Python program to access a function inside a function.

'''
def sum1(a,b,c):
    def sum2(a,b):
        return a+b
    return sum2(a,sum2(b,c))
print sum1(2,3,4)

def g1(a,b):
    if a>b:
        return a
    else:
        return b
def g2(a,b,c):
    return g1(a,g1(b,c))
print g2(23,42,3),"is greatest number"

'''


# 16.
items=[n for n in input("enter the string").split('-')]
print items
items.sort()
print('-'.join(items))

    





        
    

     










    

            
