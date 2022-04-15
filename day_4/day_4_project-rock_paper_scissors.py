# Import modules
import random

# Attributes ASCII Art for rock, paper and scissors variables
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
options = [rock, paper, scissors]

# Gets user's choice and checks if it's a valid entry
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 0 or user_choice >= 3:
    print("Impossible choice mate! Try again: 0, 1 or 2.")
else: 
    print(options[user_choice])

    # Gets computer's choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chooses:\n{options[computer_choice]}")

    # Determines the winner 
    if user_choice > computer_choice:
        if user_choice == 2 and computer_choice == 0:
            print("Not today! Computer wins!")
        else:
            print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw! Try again.")
    elif computer_choice > user_choice:
        if computer_choice == 2 and user_choice == 0:
            print("Well played... You win!")
        else:
            print("Bad luck today!? Computer wins!")