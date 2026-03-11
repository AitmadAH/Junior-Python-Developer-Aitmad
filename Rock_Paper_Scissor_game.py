import random
from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

user_score = 0
computer_score = 0
rounds = 0


def get_user_choice():
    while True:
        choice = input(Fore.WHITE + "Choose 🪨 rock, 📄 paper, ✂️  scissors or ❌ q to quit: ").strip().lower()

        if choice in ["rock", "paper", "scissors", "q"]:
            return choice
        else:
            print(Fore.RED + "⚠️ Invalid input! Please type rock, paper, or scissors.")


print(Fore.LIGHTCYAN_EX + "🎮 ROCK PAPER SCISSORS GAME 🎮")

while True:

    user_choice = get_user_choice()

    if user_choice == "q":
        break

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(Fore.LIGHTBLUE_EX + f"👤 You chose: {user_choice}")
    print(Fore.LIGHTMAGENTA_EX + f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print(Fore.YELLOW + "🤝 It's a Tie!")

    elif wins[user_choice] == computer_choice:
        print(Fore.GREEN + "🏆 You Win this round!")
        user_score += 1

    else:
        print(Fore.RED + "🤖 Computer Wins this round!")
        computer_score += 1

    rounds += 1

    table = [
        ["👤 Player", user_score],
        ["🤖 Computer", computer_score],
        ["🎯 Rounds Played", rounds]
    ]

    print("📊 Scoreboard")
    print(tabulate(table, headers=["Name", "Score"], tablefmt="fancy_grid"))

print(Fore.CYAN + "👋 Game Over! Thanks for playing!")