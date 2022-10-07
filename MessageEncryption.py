import math

def main():
    print(e(input("enter message to encrypt or decrypt > ")))


def e(msg):
    dimensions = 1 + int(math.sqrt(len(msg)))
    arr = []
    for x in range(dimensions):
        inner = []
        for y in range(dimensions):
            if dimensions*x+y < len(msg):
                inner.append(msg[dimensions*x+y])
            else:
                inner.append(" ")
                
        arr.append(inner)
        
    string = ""
    for y in range(dimensions):
        for x in range(dimensions):
            string += arr[x][y]
    return string

main()
