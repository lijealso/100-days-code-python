# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇

weight2 = float(weight)
height2 = float(height)

result = round(weight2 / (height2**2), 2)

print(result)