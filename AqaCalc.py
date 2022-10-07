p1 = int(input("enter marks for paper 1 > "))
p2 = int(input("enter marks for paper 2 > "))
p3 = int(input("enter marks for paper 3 > "))
p4 = int(input("enter marks for paper 4 > "))


percentage1, percentage2, percentage3, percentage4  = p1/100*100, p2/60*100, p3/100*100, p4/75*100

percentage = (percentage1*0.3 + percentage2*0.2 + percentage3*0.3 + percentage4*0.2)  

if percentage >= 80:
    print("A")
elif percentage >= 70:
    print("B")
elif percentage >= 60:
    print("C")
elif percentage >= 50:
    print("D")
elif percentage >= 40:
    print("E")
elif percentage < 40:
    print("U")
else:
    print("something went wrong")
