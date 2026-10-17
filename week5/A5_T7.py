
DELIMITER = ","


def collectWords() -> str:
    Words = ""

    while True:
        Word = input("Insert word(empty stops): ")

        if Word == "":
            break

        if Words != "":
            Words += DELIMITER

        Words += Word

    return Words


def analyseWords(Words: str) -> None:
    WordList = Words.split(DELIMITER) if Words != "" else []

    WordCount = len(WordList)
    CharacterCount = sum(len(Word) for Word in WordList)

    if WordCount > 0:
        Avg = CharacterCount / WordCount
    else:
        Avg = 0

    print(f"- {WordCount} Words")
    print(f"- {CharacterCount} Characters")
    print("- {:.2f} Average word length".format(Avg))


def main() -> None:
    Words = collectWords()
    analyseWords(Words)


print("Program starting.")
main()
print("Program ending.")
