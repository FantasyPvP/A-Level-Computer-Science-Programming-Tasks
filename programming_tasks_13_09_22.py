
def HelloWorld():
    print("Hello, World!")

def Favourites():
    favourite_foods = ["pizza", "burgers", "spaghetti", "fish and chips", "wispas"]
    for food in favourite_foods:
        print(food)

def Quotation():
    quote = ("we dont talk about that", "ryclonefighter")
    print(f"{quote[0]}\n  -{quote[1]}")

def WelcomeUser():
    name = input("what is your name")
    print(f"Hello, {name}")
    
def FindSumAverage():
    x = int(input("enter first number > "))
    y = int(input("enter second number > "))

    print(f"sum = {x + y}\naverage = {(x+y)/2}")

def FindProduct():
    x = int(input("enter first number > "))
    y = int(input("enter second number > "))
    print(x*y)
    
def CalculateTip():
    bill = float(input("enter the bill > "))
    tip = 0.1 * bill
    tip2 = 0.125 * bill

    print(f"for 10% the tip is: {tip}\nfor 12.5% the tip is {tip2}")

def HolidaySpending():
    initial = 50000
    print("Italian Holiday")
    print(f"initial money: {initial}")

    food = float(input("input amount spent on food > "))
    trips = float(input("input amount spent on trips > "))
    presents = float(input("input amount spent on presents > "))
    print(initial - (food + trips + presents))

def GcseAvg():
    score = int(input("enter your gcse points score > "))    
    taken = int(input("enter the number of gcses taken > "))

    print(score / taken)

def CalculateTax():
    salary = float(input("enter the amount of money you earned in total > "))
    tax = 0.25 * salary
    print(f"tax: {tax}")
    print(f"net pay: {salary - tax}")

def FtoC():
    f = float(input("enter temperature in farenheit > "))
    c = 5*(f-32)/9

    c = (c*100)//100
    
    print(f"{c}c")

def CalculateFuel():
    miles = float(input("how many miles have you driven > "))
    litres = float(input("how many litres of fuel have you used > "))

    gallons = miles / 4.54609
    miles_per_gallon = miles / gallons
    print(miles_per_gallon)

def LiverChester():
    number = int(input("enter the number of people going to the match > "))
    capacity = int(input("how many people can fit on each coach > "))

    print(f"full coaches: {number // capacity}")
    print(f"people on last coach: {(number % capacity)}")

def AgeSelection():
    if int(input("enter age > ")) < 16:
        print("you can buy a child's ticket")
    else:
        print("you must buy an adult ticket")

def AgeSelection2():
    match int(input("enter age > ")):
        case num if 1 <= num < 16:
            print("you are too young to drive")
        case 16:
            print("you can drive from this year")
        case num if 16 < num < 66:
            print("you're old enought to drive")
        case num if 66 <= num < 76:
            print("you need to renew your license periodically")
        case num if num >= 76:
            print("you need to renew your license anually")
























