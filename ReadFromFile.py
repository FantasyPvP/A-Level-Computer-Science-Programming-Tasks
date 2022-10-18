def main():
	filehandle = open("./taskdata/WriteToFile/students.txt", "r")
	x = "".join(filehandle.readlines()).split("\n")
	for y in x:
		print(y)
		
	print("EOF")		
		
main()