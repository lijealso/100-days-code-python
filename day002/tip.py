print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
bill_as_float = float(bill)

percentage = input("How much tip would you like to give? 10, 12, or 15? ")
percentage_as_float = float(percentage) / 100.0

total_bill = bill_as_float * (1 + percentage_as_float)

people = int(input("How many people to split the bill?" ))

bill_split = total_bill / people

format_bill = "{:.2f}".format(bill_split)

print(format_bill)