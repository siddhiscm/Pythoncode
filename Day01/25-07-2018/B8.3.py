#3.	Python Program to Check Whether a Given Year is a Leap Year
n = input("enter the year: ")
if (n%4) == 0:
    if (n%100) == 0:
        if (n%400) == 0:
            print "It is a Leap year"
        else:
            print "It is not a leap year"
    else:
        print "It is a leap year"
else:
    print "It is not a leap year"
