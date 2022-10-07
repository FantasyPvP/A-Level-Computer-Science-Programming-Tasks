
def wordcount(sentence):
    length = 0
    words = sentence.split(" ")
    for word in words:
        if word != "":
            length += 1
    return length

def vowelcount(sentence):
    vowels = 0
    for char in sentence:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
    return vowels   





print("sentence analysis\n\n")
sentence = input("enter a sentence > ")
print(f"your sentence contains : {wordcount(sentence.lower())} words")
print(f"your sentence contains : {vowelcount(sentence.lower())} vowels")
