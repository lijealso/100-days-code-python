def is_leap(year):
  "return if is a leap year or not"
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
       return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(month, year):
  "returns number of days in a specific month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) == False:
    return month_days[month - 1]
  if is_leap(year) == True and month == 2:
    return month_days[month - 1] + 1
  if is_leap(year) == True and month != 2:
    return month_days[month - 1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(month, year)
# docstring
print(is_leap.__doc__)
print(days_in_month.__doc__)

print(days)