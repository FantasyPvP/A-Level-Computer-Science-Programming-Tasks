
# count is assigned to one where it should initially be assigned to 0 (line 5)
# Divisor and Testnumber are the wrong way round in line 7
# the <= operator should be used on line 7 instead of just <  
# Divisor is spelled wrong in line 9
# the contents of line 11 should be inside the if statement
# line 12 should say 'Divisor <- Divisor + 1'
# variable 'Count' is misspelled in line 14
# line 4 should be deleted and line 1 should say "while TestNumber != 0"
# an extra line with an endwhile should be added so the entirety of the code is within the initial while loop
# line 8: Divisor and TestNunber should be the opposite way round

num = -1
while num != 0:
    num = int(input("enter a positive integer > "))

    count = 0
    divisor = 1

    while divisor <= num:
        if num % divisor == 0:
            print(divisor)
            count += 1
        divisor += 1
    print("number of factors = ", count)
