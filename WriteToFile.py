
def main():
	filehandler = open("./taskdata/WriteToFile/students.txt", "w")
	names = []
	for i in range(10):
		names.append(input(f"enter the name of a student {i+1}/10 > "))
		
	for x in names:
		filehandler.write(f"{x}\n")




main()
