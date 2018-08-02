#3. Python Program to Detect if Two Strings are Anagrams


str1 = raw_input("enter the first string: ")
str2 = raw_input("enter the second string: ")
'''a = str1[::-1]
b = str2[::-1]
if a == str1:
    if b == str2:
        print "both strings are Anagrams"
    else:
        print "both strigs are not anagrams"
'''


if (sorted(s1)==sorted(s2)):
	print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")

