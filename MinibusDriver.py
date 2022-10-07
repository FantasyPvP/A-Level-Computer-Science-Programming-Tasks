age = int(input("enter age > "))
passed = input("did you pass your test? [yes/no] > ")
if age >= 21 and passed == "yes":
    print("you can drive the minibus")
elif passed == "no":
    print("you cannot drive the minibus")
elif age >= 21:
    print("you must answer yes/no to passing your test")
else:
    print("you cannot drive the minibus")
