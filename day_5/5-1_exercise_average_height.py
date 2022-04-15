# Creates a list of student heights
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Calculates the average student height
sum_heights = 0
num_students = 0
for height in student_heights:
    sum_heights += height
    num_students += 1
average_height = round(sum_heights / num_students)

# Prints the average students height:
print(f"Average student height: {average_height}")
