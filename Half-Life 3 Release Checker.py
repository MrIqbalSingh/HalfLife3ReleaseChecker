# Welcome the user to the program.
print("\nWelcome to the Half-Life 3 release checker.")
# Set an initial value for choice other than quit
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\n[1] Enter 1 for yes.")
    print("[2] Enter 2 for no.")
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input(
        "\nHas the world ended? Please look outside your window and choose one of the above options.\n")

    # Respond to the user's choice.
    if choice == '1':
        print("\nThe world is ending, so Half-Life 3 will probably release tomorrow.\n")
    elif choice == '2':
        print("\nThe world hasn't ended yet, so Half-life 3 probably won't release anytime soon!\n")
    elif choice == 'q':
        print("\nThanks for checking. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")

# Print a message now that the program has run.
print("Check again tomorrow and see if this has changed!")
