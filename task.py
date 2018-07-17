
#1.
'''
print "Twinkle,twinkle,little star,"
print '\t' "How i wonder what you are!"
print '\t\t' "up above the world so high,"
print '\t\t' "Like a dimond in the sky."
print "Twinkle,twinkle,little star,"
print '\t' "How i wonder what you are!"
'''

#2.

l = [10,20,30,40,50,60,70,80,90]
d = l
print l
print d
for i in range(len(d)):
    print d
    if d[i]%3 == 0:
        print d.pop(i)
        pass
for i in range(0,len(d)):
    if d[i]%4 == 0:
        print d.pop(i)
        pass
for i in range(0,len(d)):
    if d[i]%5 == 0:
        print d.pop(i)
for i in range(0,(len(d)-1)):
    if d[i]%2 == 0:
        print d.pop(i)






'''

    while i<len(d):
        if d[i]%3 == 0:
            print d[i]
            d.pop(i)
        break
    elif d[i]%4 == 0:
        print d[i]
        d.pop(i)
    elif d[i]%5 == 0:
        print d[i]
        d.pop(i)
        
'''
