import random

emoji = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}
choice = ("r", "p", "s")

while True:
    user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
    if user_choice not in choice:
        print("Invalid choice. Please choose r, p, or s.")
        continue

    computer_choice = random.choice(choice)
    print(f"You chose {emoji[user_choice]}.")
    print(f"Computer chose {emoji[computer_choice]}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "r" and computer_choice == "s":
        print("You win! Rock beats scissors.")
    elif user_choice == "p" and computer_choice == "r":
        print("You win! Paper beats rock.")
    elif user_choice == "s" and computer_choice == "p":
        print("You win! Scissors beat paper.")
    else:
        print("Computer wins! Better luck next time.")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye.")
        break