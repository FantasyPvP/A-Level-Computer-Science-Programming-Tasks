nums = []
while True:
    num = int(input("enter number > "))
    if num != -1:
        nums.append(num)
    else:
        break

h = 0
l = 0

for num in nums:
    if num > h:
        h = num
    if num < l:
        l = num
print(nums, "\n", h, l)
