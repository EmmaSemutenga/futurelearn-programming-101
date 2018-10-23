#print(len(set("semutenga")))

def issiogram():
    word = input("Please insert your word: ")
    if len(word) == len(set(word)):
        return f"{word} is an isogram"
    return f"{word} is not an isogram"

print(issiogram())