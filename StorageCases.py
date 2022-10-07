def main():
    prices = []

    for i in range(11):
        prices.append(3.5 + 0.82*i)

    end = False
    
    while not end:
        dividers = int(input("how many dividers are required [1..10] > "))
        print(f"{prices[dividers]}0")

        while True:
            match input("do you want to find another price [Y/N] > "):
                case "Y":
                    break
                case "N":
                    end = True
                    break
                case _:
                    print("invalid option")
        
    








main()
