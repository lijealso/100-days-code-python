import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")

print(names_string)

names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(len(names))

rand_number = random.randint(0, len(names) - 1)

print(rand_number)

print(f"{names[rand_number]} is going to buy the meal today!")


