#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    cans = math.ceil(height * width / cover)
    print(f"You'll need {cans} cans of paint.")

#Write your code above this line 👆
    
# 🚨 Don't change the code below 👇

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
