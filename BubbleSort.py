
def main():
	n = []
	for i in range(10):
		n.append(input(f"enter name {i+1}"))
	
	print(n)
	
	for x in range(10):
		for y in range(10-x):
			if y == len(n) -1:
				pass
			elif n[y] > n[y+1]:
				t = n[y]
				n[y] = n[y+1]
				n[y+1] = t
		print(n)
	print(n)

main()