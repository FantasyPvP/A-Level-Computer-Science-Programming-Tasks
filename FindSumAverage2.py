
def main():
    (x,y) = InputData()
    (sum_, average) = CalculateResults(x,y)
    OutputResults(sum_, average)

def CalculateResults(x,y):
    sum_ = x + y
    average = (x + y) / 2
    return (sum_, average)

def OutputResults(sum_, average):
    print(f"sum = {sum_}\naverage = {average}")

def InputData():
    x = int(input("enter first number > "))
    y = int(input("enter second number > "))
    return (x,y)

main()
