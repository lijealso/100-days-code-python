import art
import os

bids = []

print(art.logo)
print("Welcome to the secret auction program.")

def make_bids():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids.append({"name": name, "bid": bid})
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == 'yes':
        os.system('cls')
        make_bids()
    else:
        return 0

def winner():
    max_value = max(item['bid'] for item in bids)
    for item in bids:
        if item["bid"] == max_value:
            name_winner = item["name"]
    print("The winner is " + name_winner +  " with a bid of $" + max_value)

make_bids()
# print(bids)
winner()
# print("End")