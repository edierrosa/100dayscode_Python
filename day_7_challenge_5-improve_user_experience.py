import hangman_words
import hangman_art
import random
import os

# Choose a word from 'word_list' and set game's initial paramenters
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# Import the logo and print it at the start of the game
print(hangman_art.logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"
guesses = []

# Asks user to guess a letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    # Prints the letter and let them know if they've already guessed the letter
    if guess in guesses:
        print(
            f"You've chosen '{guess}' before. Please try a different letter.")
    else:
        guesses.append(guess)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # Prints out the letter and let them know if it's not in the word
        print(f"'{guess}' is not a letter in this word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Joins all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    # Checks if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
