with open("./file1.txt") as file:
    file_1 = [int(n.strip()) for n in file.readlines()]

with open("./file2.txt") as file:
    file_2 = [int(n.strip()) for n in file.readlines()]

result = [n for n in file_2 if n in file_1]

print(file_1)
print(file_2)
print(result)
