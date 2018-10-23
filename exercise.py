numbers = []

def norepeat():
    while True:
        number = int(input("Please insert number"))
        if number in numbers:#or not in
            continue
        numbers.append(number)
        decide = input("Do you wish to continue y or n")
        if decide == "n":
            break

norepeat()
print(numbers)