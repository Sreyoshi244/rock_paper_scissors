import random

# Mapping and emojis
youDict = {"r": 1, "p": -1, "s": 0}
revDict = {1: "rock 🪨", -1: "paper 📄", 0: "scissors ✂️"}

your_score = 0
computer_score = 0

print("Welcome to Rock 🪨 Paper 📄 Scissors ✂️!")
print("Type 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to quit.")

while True:
    yourchoice = input("\nYour choice (r/p/s): ").lower()

    if yourchoice == 'q':
        print("\nThanks for playing!")
        print(f"Final Score – You: {your_score} | Computer: {computer_score}")
        break

    if yourchoice not in youDict:
        print("Invalid input! Please type 'r', 'p', or 's'.")
        continue

    you = youDict[yourchoice]
    computer = random.choice([-1, 1, 0])

    print(f"You chose {revDict[you]}")
    print(f"Computer chose {revDict[computer]}")

    diff = (you - computer) % 3

    if diff == 0:
        print("It's a draw 😐")
        print("\n✨ Get ready for the next round! ✨\n")
    elif diff == 1:
        print("You win! 🎉")
        your_score += 1
        print("\n✨ Get ready for the next round! ✨\n")
    else:
        print("You lose! 😢")
        computer_score += 1
        print("\n✨ Get ready for the next round! ✨\n")