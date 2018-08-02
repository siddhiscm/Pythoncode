# 2.Python Program to Remove the nth Index Character from a Non-Empty String

s = "String"
r = input("enter the index number: ")
for i in range(len(s)):
    if i == r:
        v = s[i]
        s = s.replace(v,'')
print s

