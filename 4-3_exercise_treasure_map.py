# Asks for user's input
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Converts into coordinates
x = int(position[0]) - 1
y = int(position[1]) - 1

# Marks the "X" on the map
map[y][x] = "X"

# Prints the updated map
print(f"{row1}\n{row2}\n{row3}")