#18.Python Program to Count the Occurrences of Each Word in a Given String Sentence
n = raw_input("enter the string sentence: ")
l = list(n.split(' '))
c=0
for i in l:
    c += 1
print "the given string sentence contains %d words"%c
