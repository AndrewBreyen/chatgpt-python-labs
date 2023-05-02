# Define a function to start the game and display the opening text
def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself standing at a fork in the road.")
    print("You must choose between two paths. Which path will you choose?")

# Define a function to prompt the player to choose a path
def choose_path():
    print("You can choose between two paths:")
    print("1. The path to the left")
    print("2. The path to the right")

    # Allow the player to choose a path
    choice = input("Which path will you choose? (Enter 1 or 2): ")

    # Use conditional statements to determine the player's choice
    if choice == "1":
        print("You chose the path to the left.")
        swim_or_raft()
    elif choice == "2":
        print("You chose the path to the right.")
        navigate_or_go_around()
    else:
        print("Invalid input. Please try again.")
        choose_path()

# Define a function to prompt the player to choose between swimming and building a raft
def swim_or_raft():
    print("You come across a river. Do you swim across or build a raft?")
    print("1. Swim across")
    print("2. Build a raft")

    # Allow the player to choose between swimming and building a raft
    choice = input("What will you do? (Enter 1 or 2): ")

    # Use conditional statements to determine the player's choice
    if choice == "1":
        print("You swim across the river and continue on your journey.")
        play_again()
    elif choice == "2":
        print("You build a raft and cross the river safely.")
        play_again()
    else:
        print("Invalid input. Please try again.")
        swim_or_raft()

# Define a function to prompt the player to choose between navigating through a dense forest or going around it
def navigate_or_go_around():
    print("You come across a dense forest. Do you try to navigate through it or go around?")
    print("1. Navigate through the forest")
    print("2. Go around the forest")

    # Allow the player to choose between navigating through the forest or going around it
    choice = input("What will you do? (Enter 1 or 2): ")

    # Use conditional statements to determine the player's choice
    if choice == "1":
        print("You navigate through the forest and emerge on the other side unscathed.")
        play_again()
    elif choice == "2":
        print("You go around the forest and eventually reach your destination.")
        play_again()
    else:
        print("Invalid input. Please try again.")
        navigate_or_go_around()

# Define a function to ask the player if they want to play again
def play_again():
    choice = input("Do you want to play again? (Enter yes or no): ")

    # Use conditional statements to determine if the player wants to play again
    if choice.lower() == "yes":
        start_game()
        choose_path()
    elif choice.lower() == "no":
        print("Thank you for playing the Text-Based Adventure Game!")
    else:
        print("Invalid input. Please try again.")
        play_again()

# Define the main method to start the game
def main():
    start_game()
    choose_path()

# Call the main method to start the game
if __name__ == "__main__":
    main()
