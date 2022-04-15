import random

# Defines a function to check if number is prime:


def prime_checker(number):
    # Alternative
    # a = random.choice(range(2, number))
    # if ((a**(number-1)) % number) != 1:
    #     print("It's not a prime number.")
    # else:
    #     print("It's a prime number.")
    prime = True
    for a in range(2, number):
        if number % a == 0:
            prime = False
    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Asks input and calls the function
n = int(input("Check this number: "))
prime_checker(number=n)
