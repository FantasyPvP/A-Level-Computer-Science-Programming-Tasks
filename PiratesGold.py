gold = int(input("how much gold do you have? > "))
num = int(input("how many pirates to share between > "))
print("gold per pirate = ", gold // num)
print("left over = ", gold % num)
