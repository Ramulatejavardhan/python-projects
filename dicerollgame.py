import random
choice=input("Roll the dice? (y/n):").lower()
if choice == "y":
    print("Lets start the game")
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(die1,",",die2)
elif choice == "n":
    print("thanks")
else:
    print("Invalid choice")
