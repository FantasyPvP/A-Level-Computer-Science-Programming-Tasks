import random

value = random.randint(0,100)
guesses = 0

while True:
    guess = int(input("guess a number between 1 and 100 > "))
    if guess == value:
        print("you win!")
    elif guess < value:
        guesses += 1
        print("too low")
    else:
        guesses += 1
        print("too high")

    if guesses >= 5:
        print("you lose")
        break
