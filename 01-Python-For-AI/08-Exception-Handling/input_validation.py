# Keep asking until valid integer is entered

while True:
    try:
        num = int(input("Enter an integer: "))
        print("Valid number:", num)
        break

    except ValueError:
        print("Invalid input, please enter a number")
