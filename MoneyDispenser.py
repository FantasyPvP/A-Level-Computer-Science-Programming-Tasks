pounds = int(input("how much money do you have > "))

print("20's: ", pounds // 20)
pounds %= 20
print("10's: ", pounds // 10)
pounds %= 10
print("5's: ", pounds // 5)
pounds %= 5
print("2's: ", pounds // 2)
pounds %= 2
print("1's:" , pounds // 1)
