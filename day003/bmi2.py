# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height**2)
bmi_f = "{:.2f}".format(bmi)

print(bmi_f)

if bmi_f < 18.5:
    print(f"Your bmi is {bmi_f}, you are underweight")
elif bmi_f < 25:
    print(f"Your bmi is {bmi_f}, you have a normal weight")
elif bmi_f < 30:
    print(f"Your bmi is {bmi_f}, you are slightly overweight")
elif bmi_f < 35:
    print(f"Your bmi is {bmi_f}, you are obese")
else:
    print(f"Your bmi is {bmi_f}, you are clinically obese")
