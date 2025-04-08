# Game: Stone, Paper, Scissors
import random

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0

    # Dictionary to map choices
    youDict = {"stone": 0, "paper": 1, "scissor": 2}
    reverseDict = {0: "stone", 1: "paper", 2: "scissor"}

    # Play up to 3 rounds
    round_number = 1
    while round_number <= 3:
        print(f"\nRound {round_number}/3")

        # Generate a new random choice for the computer each round
        computer = random.choice([0, 1, 2])

        # Get user input
        youstr = input("Choose between:\n1. stone\n2. paper\n3. scissor\nSelect from the above options: ").lower()

        # Check if user input is valid
        if youstr not in youDict:
            print("Invalid choice! Please enter 'stone', 'paper', or 'scissor'.")
            continue  # Skip this round if input is invalid

        # Convert user choice to number
        you = youDict[youstr]

        # Display choices
        print(f"\nYou chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

        # Determine the winner
        if computer == you:
            print("It's a Draw!")
        elif (computer == 0 and you == 1) or (computer == 1 and you == 2) or (computer == 2 and you == 0):
            print("You Won!")
            user_score += 1
        else:
            print("Computer Won!")
            computer_score += 1

        # Ask user if they want to continue to the next round
        if round_number < 3:
            next_round = input("\nDo you want to play the next round? (y/n): ").lower()
            if next_round == "n":
                break  # Stop the game early if the user doesn't want to continue
            else:
                continue
        
        round_number += 1  # Increase round number only if continuing

    # Final score
    print("\nFinal Score")
    print(f"You: {user_score} | Computer: {computer_score}")

    # Determine final winner
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer wins the game! Better luck next time!")
    else:
        print("It's a tie!")

# Main loop for replaying the game
while True:
    play_game()
    replay = input("\nWant to quit the game? (y/n): ").lower()
    if replay == "y":
        print("Thanks for playing! Goodbye!")
        break  # Exit the loop if the user enters "n"
    else:
        continue
