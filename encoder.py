# Gareth Bacchus Lab 6

def encoder(passcode):
    result = ''
    for digit in passcode:
        new_digit = str((int(digit) + 3) % 10)  # Shifts the digit up by 3 numbers
        result += new_digit  # Obtains the new digit
    return result  # Output


def main():
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            value = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print("The encoded password is", encoder(value))
            print("and the original password is", value)
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()


main()
