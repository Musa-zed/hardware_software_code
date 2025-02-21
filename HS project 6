def program_intro():
    print("Welcome to the Number Conversion Program!")
    print("This program will convert between decimal and binary numbers.")
    print("You can choose to convert from decimal to binary or binary to decimal.")
    print("Type 'exit' anytime to quit the program.")

def decimal_to_binary(decimal_num):
    """Convert a decimal number to binary."""
    return bin(decimal_num)[2:]

def binary_to_decimal(binary_str):
    """Convert a binary string to decimal."""
    return int(binary_str, 2)

def get_valid_decimal():
    """Prompt the user for a valid decimal number."""
    while True:
        try:
            decimal_num = int(input("Enter a decimal number: "))
            if decimal_num < 0:
                print("Please enter a positive decimal number.")
            else:
                return decimal_num
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

def get_valid_binary():
    """Prompt the user for a valid binary number."""
    while True:
        binary_str = input("Enter a binary number: ").strip()
        if all(char in '01' for char in binary_str):  # Check if the input contains only 0s and 1s
            return binary_str
        else:
            print("Invalid input. Please enter a valid binary number (only 0s and 1s).")

def main():
    program_intro()

    while True:
        print("\nChoose an option:")
        print("1. Convert decimal to binary")
        print("2. Convert binary to decimal")
        print("Type 'exit' to quit.")

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif choice == '1':
            decimal_num = get_valid_decimal()
            binary_num = decimal_to_binary(decimal_num)
            print(f"The binary representation of {decimal_num} is: {binary_num}")
        elif choice == '2':
            binary_str = get_valid_binary()
            decimal_num = binary_to_decimal(binary_str)
            print(f"The decimal representation of {binary_str} is: {decimal_num}")
        else:
            print("Invalid choice. Please choose 1 or 2, or type 'exit' to quit.")

if __name__ == "__main__":
    main()
