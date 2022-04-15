import pandas as pd

# Import Nato Alphabet and create a dictionary
data = pd.read_csv("./nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for index, row in data.iterrows()}

# Create a list of letters from the inputed word
word_letters = [letter for letter in (input("Word: ").upper())]

# Create a correspond NATO Alphabet list
nato = [data_dict[letter] for letter in word_letters]

print(nato)
