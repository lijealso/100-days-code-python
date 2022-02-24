print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the roalercoaster...")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        
    elif age <= 18:
        bill = 7
    
    elif age >= 45 and age <= 55:
        bill = 0
    
    else:
        bill= 12
 
    wants_photo = (input("Do tou want a photo taken? Y or N. "))
    if wants_photo == "Y":
        bill += 3
    
        
    print(f"bill: {bill}")
    
else:
    print("You can't ride the roalercoaster")
