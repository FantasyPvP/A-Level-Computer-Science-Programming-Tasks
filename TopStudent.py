students = []

for i in range(5):
    students.append(
        (input("enter name of student > "), int(input("enter the mark for this student > ")))
    )

highest = ("N/A", 0)

for student in students:
    if student[1] > highest[1]:
        highest = student

print(f"the highest score was {highest[0]} with {highest[1]} marks")
