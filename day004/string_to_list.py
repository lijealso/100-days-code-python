"""
# 1. String to List of Strings

# given string
string1 = "Python is great"

# printing the string
print("Actual String: ", string1)

# type of string1
print("Type of string: ", type(string1))

# prints the list given by split()
print("String converted to list: ", string1.split())


# 2. String to List of Characters

# given string
string2 = "AskPython"

# printing the string
print("Actual string: ", string2)

# confirming the type
print("Type of string: ", type(string2))

# type-casting the string into list using list()
print("String converted to list: ", list(string2))


# 3. List of Strings to List of Lists

# given string
string3 = "This is Python"

print("Actual string: ", string3)

# converting string3 into a list of strings
string3 = string3.split()
print(string3)

# applying list method to the individual elements of the list string3
list1 = list(map(list, string3))

print(type(list1))

# printing the resultant list of lists
print("Converted to list of characters list:\n",  list1)


# 4. CSV to List

# given string
string4 = "abc,def,ghi"

print("Actual string: ", string4)

#spliting strng4 into list with ',' as the parameter

print("CSV converted to list: ", string4.split(','))
"""

# 5. A string consisting of Integers to List of integers

# string with integers separated by spaces
string5 = "1 2 3 4 5 6 7 8"

print("Actual string containing integers: ", string5)
print("Type of string: ", type(string5))

list1 = list(string5.split())

list2 = list(map(int, list1))

print("List of integers: ", list2)





