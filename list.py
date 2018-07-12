"""
#---list is a muttable 
name=['bhuna','roja','teju','gayi']
name[0]='bhuvana'
print (name)
"""
#--list can have a multipule datatypes 
#example
"""
friends=['bhuvana',23,'sriram',25,'nandu',22,'divya',24]
print (friends)
"""
#---sublist
"""
person = [["bhuna","nandu"],["21,AP", "20,KA"],"friends"]
print (person)
print (person[0][0])
print (person[0][1])
print (person[1][0])
print (person[1][1])
print (person[2])
#complex list 
complex_list = [["a",["b",["c","x"]]]]
complex_list = [["a",["b",["c","x"]]],42]
print (complex_list[0][1])
print (complex_list[0][1][1][0])
#---Concatination
l1=[1,2,3,4]
l2=[1,2,3,4]
l3=l1+l2
print (l3)
#------repeat in list and change the value 
x = ["a","b","c"]

print (x)
y = [x] * 4
print (y)
y[1][1] ="p"
print (y)
print (x)
subject =['s','m','p']
print(subject)
subject.reverse()
print (subject)
number=[1,2,3,4]
number.remove(2)
print (number)
subject.append("h")
print (subject)
subject.insert(2,"g")
print (subject)
subject.extend(number)
print (subject)
subject.remove("s")
subject.sort()
print (subject)
#------tuples
number=(1,2,3,4,5,4,5,6,4,4)
string1=('a','b','c','d')
print (number[1])#---indexing
print (number[1:4])#---slicing
con=number+string1
print (con)
print (number.count(4))#---counting how many time repeat 4 number in number list 
print (number *2) #---repeatition 
print [len(number)]
a=100
b=60

c=70
if (a>b)& (a>c) &(a==10):
print (a  is greatest &value holds the 100)
else:
print (a is greatest &value holds not equal )
"""


















