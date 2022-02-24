# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()

true_t = name1_lower.count("t") + name2_lower.count("t")
true_r = name1_lower.count("r") + name2_lower.count("r")
true_u = name1_lower.count("u") + name2_lower.count("u")
true_e = name1_lower.count("e") + name2_lower.count("e")

love_l = name1_lower.count("l") + name2_lower.count("l")
love_o = name1_lower.count("o") + name2_lower.count("o")
love_v = name1_lower.count("v") + name2_lower.count("v")
love_e = name1_lower.count("e") + name2_lower.count("e")

true_total = true_t + true_r + true_u + true_e
love_total = love_l + love_o + love_v + love_e

total_string = str(true_total) + str(love_total)
total_int = int(total_string)

print(total_string)
print(total_int)

if total_int < 10 or total_int > 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int >= 40 and total_int <= 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")




