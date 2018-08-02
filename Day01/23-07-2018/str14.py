#14. Python Program to Check if a String is a Pangram or Not
Str = raw_input("Enter the String: ")
Str1=Str.lower()
Str1=Str1.replace(' ','')
Str1=list(set(Str1))
Str1.sort()
'''j = 0
for i in Str1:
    if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        j += 1
if j == 26:
    print "panagram"
else:
    print "it is not a panagram"
'''

if Str1 == ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    print "Panagram"
else:
    print "It is not a panagram"
        

