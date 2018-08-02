#11.Python Program to Count Number of Lowercase Characters in a String

Str = raw_input("enter a string:  ")
c = 0
for i in Str:
    if (i.islower()):
        c+=1
print c
        
        
