import pandas

data = pandas.read_csv(
    "./day_30/30-3_exercise_nato_project_exception_handling/nato_phonetic_alphabet.csv")

# Create a dictionary in this format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# Create a list of the phonetic code words from a word that the user inputs
def nato_word():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato_word()
    else:
        print(output_list)


nato_word()
