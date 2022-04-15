import os
import guess_number_art
import random

# Set global variables
ATTEMPTS = 0
NUMBER = 0


def greeting_messages():
    """Prints out greeting messages"""
    print(guess_number_art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")


def difficulty():
    """Sets game difficulty"""
    global ATTEMPTS
    ATTEMPTS = 10
    if input("Choose game difficulty, type 'e' for easy, 'h' for 'hard': ") == "h":
        ATTEMPTS = 5
    print(f"You have {ATTEMPTS} to guess the number.")


def pick_number():
    """Returns a random number between 1 and 100"""
    global NUMBER
    NUMBER = random.randint(1, 100)


def check_guess():
    """Check if user's guess is right or wrong"""
    global NUMBER
    global ATTEMPTS
    while ATTEMPTS != 0:
        guess = int(input("Make a guess: "))
        if guess == NUMBER:
            print(f"Well done! {guess} is the answer!")
            ATTEMPTS = 0
        else:
            ATTEMPTS -= 1
            if guess > NUMBER:
                print("Maybe a bit lower than that!?")
            else:
                print("You should go higher!")
            print(
                f"You have {ATTEMPTS} attemps remaining to guess the number.")
    print("Game over!")


def play_again():
    """Restarts game"""
    play_again = input("Do you want to play again?(y/n) ")
    return play_again


def play():
    """Runs the game"""
    greeting_messages()
    pick_number()
    difficulty()
    check_guess()
    if play_again() == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        play()


play()
