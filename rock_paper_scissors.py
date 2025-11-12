import random

EMOJIS = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️",
    "win": "🏆",
    "lose": "😢",
    "tie": "🤝",
    "computer": "💻",
    "user": "🧑"
}

user_wins = 0
computer_wins = 0
rounds = 0
options = ["rock", "paper", "scissors"]

def print_choices(user, computer):
    print(f"{EMOJIS['user']} You: {user.capitalize()} {EMOJIS[user]}")
    print(f"{EMOJIS['computer']} Computer: {computer.capitalize()} {EMOJIS[computer]}")

print("\nWelcome to Rock, Paper, Scissors! ✊✋✌️\nType 'quit' to exit.\n")

while True:
    print(f"--- Round {rounds + 1} ---")
    user_input = input("Enter rock, paper, scissors or quit: ").strip().lower()
    if user_input == "quit":
        print("\nThanks for playing!")
        break
    if user_input not in options:
        print("❗ Invalid input! Please try again.\n")
        continue
    computer_pick = random.choice(options)
    print_choices(user_input, computer_pick)
    if user_input == computer_pick:
        print(f"It's a tie! {EMOJIS['tie']}\n")
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print(f"You win this round! {EMOJIS['win']}\n")
        user_wins += 1
    else:
        print(f"Computer wins this round! {EMOJIS['lose']}\n")
        computer_wins += 1
    rounds += 1

print("="*30)
print(f"Final score after {rounds} rounds:")
print(f"{EMOJIS['user']} You: {user_wins}   {EMOJIS['computer']} Computer: {computer_wins}")
if user_wins > computer_wins:
    print(f"Congratulations, you are the overall winner! {EMOJIS['win']}")
elif user_wins < computer_wins:
    print(f"Computer wins the game! {EMOJIS['lose']}")
else:
    print(f"It's a tie overall! {EMOJIS['tie']}")
print("="*30)