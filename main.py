def program_intro():
    print("Welcome to the Question Loop Program!")
    print("This program will ask you to answer a question until you quit.")
    print("Type 'exit' (with or without spaces and in any case) to stop the program.")

def main():
    program_intro()
    question_count = 0  # Initialize counter

    while True:
        # Prompt the user with a question
        answer = input("What is your favorite color? (Type 'exit' to quit): ").strip().lower()

        # Check if the user wants to exit
        if answer == "exit":
            print(f"You answered {question_count} questions. Exiting the program. Goodbye!")
            break
        else:
            question_count += 1  # Increment counter
            print(f"You answered: {answer}")

if __name__ == "__main__":
    main()