def askname():
    name = input("Insert name: ")
    return name

def greetUser(PName):    
    print(f"Hello {PName}!")
    return None
def main():
    print("program starting.")
    name = askname()
    greetUser(name)
    print("program ending.")
    return None

main()