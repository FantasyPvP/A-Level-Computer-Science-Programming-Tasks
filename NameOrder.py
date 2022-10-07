names = [
    input("enter first name").lower(),
    input("enter second name").lower(),
    input("enter third name").lower()
]

order = [0,1,0]
for x in order:
    if names[x] > names[x+1]:
        tmp = names[x]
        names[x] = names[x+1]
        names[x+1] = tmp

print(f"names: {names}")
