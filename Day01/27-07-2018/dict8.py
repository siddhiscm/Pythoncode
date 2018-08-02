l1 = [1,2,3,4]
l2 = [6,7,8,9]
d = {}
for i in range(len(l1)):
    d.update({l1[i]:l2[i]})
print d
    
