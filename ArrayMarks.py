names = [
    "Fred",
    "Jack",
    "Chris",
    "Ali",
    "Harry",
    "Bill",
    "Zak",
    "Phill"
]
marks = [67, 25, 92, 49, 38, 72, 99, 54]
total = sum(marks)
mean = sum(marks) / len(marks)

print(f"mean mark: {mean}")
below = 0
above = 0

for i in range(len(marks)):
    if marks[i] > mean:
       status = "above average"
       above += 1
    elif marks[i] == mean:
        status = "average"
    else:
        status = "below average"
        below += 1
        
    print(names[i], ":", marks[i], f"this score is {status}")
    total += marks[i]

print(f"above average scores: {above} | below average scores: {below}")

