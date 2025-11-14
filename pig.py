"""
Pig Dice Game - Simple Version

How to play:
- Players take turns rolling a die.
- Each roll adds to your turn score.
- If you roll a 1, you lose all points for that turn.
- You can "hold" to save your turn score to your total.
- First player to reach the target score wins!
"""

import random


def roll_die():
    """Roll a 6-sided die and return the result (1-6)."""
    return random.randint(1, 6)


def get_number_of_players():
    """Ask how many players (2-4) and keep asking until valid."""
    while True:
        answer = input("How many players? (2-4): ").strip()
        if answer in ["2", "3", "4"]:
            return int(answer)
        print("Please enter 2, 3, or 4.")


def get_target_score():
    """Ask for the target score to win."""
    while True:
        answer = input("What score to win? (e.g., 50): ").strip()
        if answer.isdigit() and int(answer) >= 10:
            return int(answer)
        print("Please enter a number 10 or higher.")


def play_turn(player_number, current_total):
    """Play one player's turn. Returns the points earned this turn."""
    print(f"\nPlayer {player_number}'s turn!")
    print(f"Current total score: {current_total}")
    
    turn_points = 0  # Points earned just this turn
    
    while True:
        # Ask if they want to roll or hold
        choice = input("Roll the die? Type 'y' to roll or 'n' to hold: ").strip().lower()
        
        if choice == "n":
            # Player holds - they keep their turn points
            print(f"You hold! You earned {turn_points} points this turn.")
            return turn_points
        
        if choice == "y":
            # Roll the die
            roll = roll_die()
            print(f"You rolled: {roll}")
            
            if roll == 1:
                # Bad luck! Lose all turn points
                print("Oh no! You rolled a 1. You lose all points from this turn.")
                return 0  # Return 0 points for this turn
            else:
                # Add to turn points
                turn_points += roll
                print(f"Turn points so far: {turn_points}")
                print(f"If you hold now, your new total will be: {current_total + turn_points}")
        else:
            print("Please type 'y' or 'n'.")


def play_game():
    """Main game loop."""
    print("Welcome to Pig Dice Game! 🐷🎲\n")
    
    # Setup
    num_players = get_number_of_players()
    target = get_target_score()
    
    # Create a list to store each player's score (starts at 0)
    scores = [0 for _ in range(num_players)]
    
    print(f"\nStarting game! First to {target} wins!")
    
    # Keep playing until someone wins
    current_player = 0  # Start with player 1 (index 0)
    
    while True:
        # Play one turn for the current player
        player_num = current_player + 1  # Show as 1, 2, 3 instead of 0, 1, 2
        points_earned = play_turn(player_num, scores[current_player])
        
        # Add the points to their total
        scores[current_player] += points_earned
        print(f"Player {player_num} now has {scores[current_player]} points total.\n")
        
        # Check if this player won
        if scores[current_player] >= target:
            print(f"🏆 Player {player_num} WINS with {scores[current_player]} points!")
            print("Congratulations! 🎉")
            break
        
        # Move to next player (wraps around to 0 after last player)
        current_player = (current_player + 1) % num_players


def main():
    """Start the game and ask if they want to play again."""
    play_game()
    
    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "y":
            print("\n" + "="*40 + "\n")
            play_game()
        elif again == "n":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please type 'y' or 'n'.")


# This runs the game when you execute the file
if __name__ == "__main__":
    main()
