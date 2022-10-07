import random

def main():
    tally = [0,0,0,0,0,0]
    for i in range(100):
        num = random.randint(1,6)
        tally[num-1] += 1

    for value in tally:
        fives = value // 5
        ones = value % 5
        print("#"*fives + "I"*ones)








main()
