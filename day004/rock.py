rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice == 0:
    print(rock)
if my_choice == 1:
    print(paper)
if my_choice == 2:
    print(scissors)

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print("Computer chose:\n", rock)
if computer_choice == 1:
    print("Computer chose:\n", paper)
if computer_choice == 2:
    print("Computer chose:\n", scissors)

if my_choice == computer_choice:
    print("It's a draw")
elif(my_choice == 0 and computer_choice == 2) or (my_choice == 1 and computer_choice == 0) or (my_choice == 2 and computer_choice == 1):
    print("Player wins")
else:
    print("Computer wins")
