
def fmt(num):
    pad = " "*(maxsize-len(str(num)))
    return f"{pad}{num}"


size = int(input("enter size of table > "))
maxsize = len(str(size*size))


ylist = []
for y in range(size):
    xlist = []
    for x in range(size):
        xlist.append(fmt((x+1)*(y+1)))
    print(xlist)
