global VAT
VAT = 0.15

def main():
    price = float(input("enter price of item > "))
    print(f"VAT: ({VAT*100}%) = {VAT*price}")
    print(f"initial price: {price}")
    print(f"final price: {price * (1+VAT)}")











main()
