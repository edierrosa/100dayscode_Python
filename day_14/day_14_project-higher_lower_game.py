import high_lower_art
from high_lower_game_data import data
import os
import random


def pick_data():
    """Returns random data from high_lower_data"""
    return random.choice(data)


def show_data(var_1, var_2):
    """Displays formatted data"""
    print(
        f"Compare A: {var_1['name']}, a {var_1['description']}, from {var_1['country']}.")
    print(high_lower_art.vs)
    print(
        f"Against B: {var_2['name']}, a {var_2['description']}, from {var_2['country']}.")


def compare(guess, a_followers, b_followers):
    """Compares user's guess against right answer"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Set inicial variables and loop to run the game
got_right = True
score = 0
b = pick_data()

while got_right:
    a = b
    b = pick_data()
    while b == a:
        b = pick_data()
    show_data(a, b)
    # Asks user's guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers_number = a['follower_count']
    b_followers_number = b['follower_count']
    os.system('cls' if os.name == 'nt' else 'clear')
    print(high_lower_art.logo)
    if compare(guess, a_followers_number, b_followers_number):
        score += 1
        print(f"That's right! Score: {score}.")
    else:
        print(f"Wrong guess! Final score: {score}.")
        got_right = False
