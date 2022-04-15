# Mail merge

# Create a list of recipients
with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()

# Read letter content
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    new_letter = letter.read()

# Generate merged letter
for _ in names:
    recipient = _.strip()
    new_letter = new_letter.replace("[name]", recipient)
    with open(f"./Output/ReadyToSend/{recipient}_letter.txt", "w") as output_letter:
        output_letter.write(new_letter)
