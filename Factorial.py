def main():
    number = get_number()
    print(factorial(number))

def get_number():
    return int(input("enter a number > "))

def factorial(number):
    for i in range(number-1):
        number *= (i+1)
    return number

main()
