# 8.Python Program to Remove the Characters of Odd Index Values in a String
Str = raw_input("enter the string: ")
c = Str
for i in range(len(Str)):
    if i%2 != 0:
        c = c.replace(Str[i],'')
print c
