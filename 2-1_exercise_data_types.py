# Asks user to type a two digit number
two_digit_number = input("Type a two digit number: ")

# Adds the input's first and second digits
result = int(two_digit_number[0]) + int(two_digit_number[1])

# Prints the addition and result
print(f"{two_digit_number[0]} + {two_digit_number[1]} = {result}")