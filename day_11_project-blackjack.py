############### Blackjack Project #####################

import os
import random
import blackjack_art


# Creates the set of cards and players dictionary to keep track of their cards and total score
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {
    'user': {
        'cards': [],
        'score': 0,
    },
    'computer': {
        'cards': [],
        'score': 0,
    },
}


def show_cards():
    """Show players' cards"""
    print(
        f"\nYour cards: {players['user']['cards']} - Total: {players['user']['score']}")
    print(
        f"Computer's cards: {players['computer']['cards']} - Total: {players['computer']['score']}")


def winner(player):
    """Declare the winner"""
    print(f"{'You win!😎' if player == 'user' else 'You lose!😭'}")


def deal_card(player):
    """Deals cards"""
    card = random.choice(cards)
    if card == 11:
        if players[player]["score"] + card > 21:
            players[player]["cards"].append(1)
    else:
        players[player]["cards"].append(card)
    players[player]['score'] = sum(players[player]['cards'])


def first_hand():
    """Deals the first hand"""
    for _ in range(2):
        deal_card('user')
        deal_card('computer')


def table():
    """Shows what's on table"""
    print(
        f"\nYour cards: {players['user']['cards']}, current score: {players['user']['score']}")
    print(f"Computer's first card: {players['computer']['cards'][0]}")


def check_blackjack(player):
    """Checks if player has a blackjack"""
    if players[player]['score'] == 21:
        print(f"BlackJack!")


def play_again():
    """Stars the game"""
    again = input("Start a new game?(y/n) ")
    if again == "y":
        players["user"]["cards"] = []
        players["computer"]["cards"] = []
        os.system('cls' if os.name == 'nt' else 'clear')
        print(blackjack_art.logo)
        running = True
        while running:
            if len(players['user']['cards']) == 0:
                first_hand()
                table()
                if check_blackjack('computer'):
                    show_cards()
                    winner('computer')
                    running = False
                    play_again()
                elif check_blackjack('user'):
                    show_cards()
                    winner('user')
                    running = False
                    play_again()
            else:
                next_card = input(
                    "Type 'y' to get anoyher card or 'n' to pass: ")
                if next_card == 'y':
                    deal_card('user')
                    if players['user']['score'] > 21:
                        show_cards()
                        print("You went over.")
                        winner('computer')
                        running = False
                        play_again()
                    else:
                        table()
                elif 'n':
                    while players['computer']['score'] < 17:
                        deal_card('computer')
                    if players['computer']['score'] > 21:
                        show_cards()
                        print("Computer went over.")
                        winner('user')
                        running = False
                        play_again()
                    elif players['user']['score'] > players['computer']['score']:
                        show_cards()
                        winner('user')
                        running = False
                        play_again()
                    elif players['user']['score'] == players['computer']['score']:
                        show_cards()
                        print("It's a draw!")
                        running = False
                        play_again()
                    else:
                        show_cards()
                        winner('computer')
                        running = False
                        play_again()


play_again()
