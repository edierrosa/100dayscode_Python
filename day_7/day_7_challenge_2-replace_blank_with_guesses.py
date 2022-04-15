import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display
# For each letter in the chosen_word, add a "_" to 'display'

display = ["_" for letter in chosen_word]
print(display)
guess = input("Guess a letter: ").lower()

# Loop through each position in the chosen_word
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
for index in range(0, len(chosen_word)):
    letter = chosen_word[index]
    if letter == guess:
        display[index] = guess
    else:
        display[index] = "_"

# Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
print(display)
