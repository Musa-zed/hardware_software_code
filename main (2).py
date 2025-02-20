def main():
    print("Welcome to the Addition Program!")
    print("This program allows you to add two whole numbers.")
    print("You can continue adding numbers until you decide to exit.\n")

    while True:
        # Get valid input from user
        num1 = get_valid_number("Enter the first whole number: ")
        num2 = get_valid_number("Enter the second whole number: ")

        # Perform addition
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.\n")

        # Ask user if they want to continue
        choice = input("Do you want to add more numbers? (yes to continue, no to exit): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the program. Goodbye!")
            break

def get_valid_number(prompt):
    """ Function to ensure valid whole number input """
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

# Run the program
if __name__ == "__main__":
    main()
