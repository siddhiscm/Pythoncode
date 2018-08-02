#15.Python Program to Accept a Hyphen Separated Sequence of Words as Input and Print the Words in a Hyphen-Separated Sequence after Sorting them Alphabetically
n = raw_input("enter the Hyphen separated sequence of words: ")
l = list(n.split('-'))
l.sort()
print '-'.join(l)



