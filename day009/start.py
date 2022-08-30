programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# retrieve items from dictionaries:
print(programming_dictionary["Bug"])

# add item
programming_dictionary["Key"] = "Value"
print(programming_dictionary)

# create empty dictionary:
new_dict = {}

# edit item in dictionaries:
programming_dictionary["Key"] = "New Value"
print(programming_dictionary)

# loop through a dictionary:
for key in programming_dictionary:
    print(key + ": " + programming_dictionary[key])