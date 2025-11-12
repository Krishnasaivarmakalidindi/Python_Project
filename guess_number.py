import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_integer_input(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value <= min_value:
                print(f"Please enter a number greater than {min_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def select_difficulty():
    print("\nSelect difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    print("4. Custom")
    
    choice = get_integer_input("Enter your choice (1-4): ", 0)
    
    if choice == 1:
        return 50, 10
    elif choice == 2:
        return 100, 7
    elif choice == 3:
        return 200, 5
    elif choice == 4:
        n = get_integer_input("Enter the upper limit for the range (greater than 1): ", 1)
        attempts = get_integer_input("Enter the number of attempts you want (at least 1): ", 0)
        return n, attempts
    else:
        print("Invalid choice. Using Medium difficulty.")
        return 100, 7

def calculate_score(n, attempts_allowed, attempts_used):
    # Higher score for larger range and fewer attempts used
    max_score = n * 10
    if attempts_used == attempts_allowed:
        return 0  # No score if all attempts were used
    
    # More points for using fewer attempts
    return int(max_score * (1 - attempts_used/attempts_allowed))

def get_hint(guess, secret_number, prev_distance, n):
    current_distance = abs(guess - secret_number)
    
    if prev_distance is None:
        return current_distance, ""
    
    # Calculate how close as a percentage of the range
    if current_distance < prev_distance:
        if current_distance < n * 0.05:  # Within 5% of range
            return current_distance, "Very hot! 🔥"
        elif current_distance < n * 0.1:  # Within 10% of range
            return current_distance, "Getting hotter! 🔥"
        else:
            return current_distance, "Warmer 🌡️"
    else:
        if current_distance > n * 0.5:  # More than 50% of range away
            return current_distance, "Freezing cold! ❄️"
        else:
            return current_distance, "Colder ❄️"

def play_game():
    clear_screen()
    print("=" * 40)
    print("  WELCOME TO THE NUMBER GUESSING GAME!")
    print("=" * 40)
    
    total_score = 0
    play_again = "y"
    
    while play_again.lower() == "y":
        n, attempts_allowed = select_difficulty()
        secret_number = random.randint(1, n)
        attempts_used = 0
        prev_distance = None
        
        print(f"\nI'm thinking of a number between 1 and {n}...")
        print(f"You have {attempts_allowed} attempts to guess it.\n")
        
        start_time = time.time()
        
        while attempts_used < attempts_allowed:
            attempts_used += 1
            guess = get_integer_input(f"Attempt {attempts_used}/{attempts_allowed}: Your guess? ", 0)
            
            if guess == secret_number:
                elapsed_time = time.time() - start_time
                score = calculate_score(n, attempts_allowed, attempts_used)
                total_score += score
                
                print(f"\n🎉 CONGRATULATIONS! You've guessed it in {attempts_used} attempts!")
                print(f"Time taken: {elapsed_time:.2f} seconds")
                print(f"Score this round: {score}")
                print(f"Total score: {total_score}")
                break
            elif guess < secret_number:
                print("Too low!")
                prev_distance, hint = get_hint(guess, secret_number, prev_distance, n)
                if hint:
                    print(hint)
            else:
                print("Too high!")
                prev_distance, hint = get_hint(guess, secret_number, prev_distance, n)
                if hint:
                    print(hint)
                    
        if attempts_used == attempts_allowed and guess != secret_number:
            print(f"\n😢 Sorry, you've used all your attempts. The secret number was {secret_number}.")
            
        play_again = input("\nWould you like to play again? (y/n): ")
        
    print("\nThanks for playing! Final score:", total_score)

if __name__ == "__main__":
    play_game()