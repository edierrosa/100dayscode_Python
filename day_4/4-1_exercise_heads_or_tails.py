# Imports modules
import random

# Generates a side's correponding number
side = random.randint(0, 1)

# Prints corresponding side output 
if side == 0:
    print("Heads")
else:
    print("Tails")
