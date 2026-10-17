def frameWord(PWord):
     print("*" * (len(PWord) + 4))
     print("* " + PWord + " *")
     print("*" * (len(PWord) + 4))
     return None

def main():
    print("starting program.")
    word=input("Insert word: ")
    frameWord(word)
    print("ending program.")
    return None


main()  