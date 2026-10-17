print("Program starting.")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

if start >= stop:
    print("Starting point value must be less than the stopping point value.")

elif inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")

else:
    print()
    print("First loop - inspection with break:")

    first = True

    for i in range(start, stop + 1):
        if i == inspection:
            break

        if not first:
            print(" ", end="")
        print(i, end="")
        first = False

    print()

    print("Second loop - inspection with continue:")

    first = True

    for i in range(start, stop + 1):
        if i == inspection:
            continue

        if not first:
            print(" ", end="")
        print(i, end="")
        first = False

    print()

print()
print("Program ending.")