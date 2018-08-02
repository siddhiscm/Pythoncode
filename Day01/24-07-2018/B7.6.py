#6. Python Program to Take in the Marks of 5 Subjects and Display the Grade
sub1 = input("enter the marks of sub1: ")
sub2 = input("enter the marks of sub2: ")
sub3 = input("enter the marks of sub3: ")
sub4 = input("enter the marks of sub4: ")
sub5 = input("enter the marks of sub5: ")
Total = (sub1+sub2+sub3+sub4+sub5)/5
if (Total >= 90):
    print "S grade"
elif (Total >= 80) and (Total < 90):
    print "A grade"
elif (Total >= 70) and (Total < 80):
    print "B grade"
elif (Total >= 60) and (Total < 70):
    print "C grade"
elif (Total >= 50) and (Total < 60):
    print "D grade"
else:
    print "E grade"
    
