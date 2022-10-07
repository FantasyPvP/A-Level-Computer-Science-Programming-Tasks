cost = float(input("enter cost > "))

if cost < 1000:
    print(cost)
elif cost < 2000:
    print(cost*0.95)
elif cost < 5000:
    print(cost*0.9)
elif cost < 10000:
    print(cost*0.85)
else:
    print(cost*0.8)
