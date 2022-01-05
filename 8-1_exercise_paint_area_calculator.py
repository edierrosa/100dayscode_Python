import math

# Define print_calc function


def paint_calc(height, width, cover):
    number_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_cans} cans of paint.")


# Asks for height and width and runs and tests function
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
