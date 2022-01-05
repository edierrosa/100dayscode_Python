import caesar_art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Caesar encryption decryption function
def caesar(message, encryption, function):
    coded_message = ""
    shifted_alphabet = alphabet[encryption:] + alphabet[:encryption]
    for index in message:
        if index not in alphabet:
            coded_message += index
        else:
            if function == "encode":
                coded_message += shifted_alphabet[alphabet.index(index)]
            elif function == "decode":
                coded_message += alphabet[shifted_alphabet.index(index)]
    print(f"The {function} message is {coded_message}")


# Input and starting module
run = True
print(caesar_art.logo)
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = (shift % 26)
    caesar(message=text, encryption=shift, function=direction)
    run = input("Run again?(Y/N) ").lower()
    if run == "n":
        print("Bye!")
        run = False
