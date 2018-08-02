#4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged
Str = raw_input("enter the String: ")
Str = list(Str)
Str[0],Str[len(Str)-1] = Str[len(Str)-1],Str[0]
print ''.join(Str)

