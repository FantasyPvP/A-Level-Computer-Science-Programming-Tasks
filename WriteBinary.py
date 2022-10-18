import pickle

def main():
	filehandle = open("./taskdata/WriteBinary/binary.bin", "wb")

	pickle.dump("./taskdata/WriteBinary/binary.bin", filehandle)
			
	ls = []
	
	while True:
		title = input("enter book title > ")
		if title.lower() == "end":
			break
		ISBN = input("enter ISBN of book >")
		price = float(input("enter price in format: xx.yy > "))
		year = int(input("enter release year > "))
		
		record = {
			"title" : title,
			"ISBN" : ISBN,
			"price" : price,
			"year" : year
		}
		ls.append(str(record))
	
	for record in ls:
		print(record)
		pickle.dump(record, filehandle)	
		
	
	
main()
