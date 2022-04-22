# Simple game just to pass time


import random


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


random.seed(5)

choice = int(input("Choose Rock(1), Paper(2), or Scissors(3): "))

if choice == 1:
  print(rock)
elif choice == 2:
  print(paper)
else:
  print(scissors)

pc_choice = random.randint(1,3)

print(pc_choice)

print("PC choice:")
if pc_choice == 1:
  print(rock)
elif choice == 2:
  print(paper)
else:
  print(scissors)

if pc_choice == choice:
  print("It is a draw!")

if pc_choice == 1 and choice == 2:
  print("You win!")
elif pc_choice == 2 and choice ==1:
  print("PC win!")

if pc_choice == 1 and choice == 3:
  print("PC win!")
elif pc_choice == 3 and choice ==1:
  print("You win!")

if pc_choice == 2 and choice == 3:
  print("You win!")
elif pc_choice == 3 and choice ==2:
  print("PC win!")

