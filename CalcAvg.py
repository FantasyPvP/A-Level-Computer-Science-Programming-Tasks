
ls = []

while True:
    ls.append(int(input("enter a number > ")))
    if ls[-1] == 999:
        ls.pop()
        break

total = 0
for i in ls:
    total += i

mean = total/ len(ls)

print(mean)
