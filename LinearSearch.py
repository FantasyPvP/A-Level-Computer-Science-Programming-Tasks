def main():
    names = ["person1", "person2", "person3", "person4", "person5"]

    prompt =  input("enter name to search for > ")

    found = False
    for (x, name) in enumerate(names):
        if name == prompt:
            print(f"{x}: {name}")
            found = True
            break
    if found == False:
        print("this name was not in the list")


main()
