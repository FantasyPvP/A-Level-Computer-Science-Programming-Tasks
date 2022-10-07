def scramble():
    message = input("enter message > ")
    if len(message) % 2 != 0:
        message += " "

    newmessage = ""
    x = ""
    for char in message:
        if x != "":
            newmessage += char
            newmessage += x
            x = ""
        else:
            x = char

    return newmessage






print(scramble())
