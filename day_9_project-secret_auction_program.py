import os
import gavel_art

# Creates a while loop variable and a bids dictionary
auction = True
bids_dictionary = {}


# Creates a bid function
def add_bid():
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bids_dictionary[name] = bid


# Creates a fuction to check the winner
def check_winner():
    # Alternative:
    # winner = max(bids_dictionary, key=bids_dictionary.get)
    # print(f"The winner is {winner} with a bid of ${bids_dictionary[winner]}.")
    winner_bid = 0
    winner = ""
    for key, value in bids_dictionary.items():
        if bids_dictionary[key] > winner_bid:
            winner_bid = value
            winner = key
    print(f"The winner is {winner} with a bid of ${winner_bid}.")


# Starts auction
print(gavel_art.logo)
while auction:
    add_bid()
    bidding = input("Are there any other bidders?(Y/N) ").lower()
    if bidding == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        auction = False
        check_winner()
