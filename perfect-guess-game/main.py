from random import randint
import sys

MAX_ATTEMPTS = 10

# ============== Helper Functions ==============

def get_valid_input(prompt, valid_options):
    """Get validated input from user."""
    while True:
        try:
            choice = input(prompt).lower().strip()
            if choice in valid_options:
                return choice
            print(f"Please enter one of: {', '.join(valid_options)}")
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Goodbye!")
            sys.exit(0)

def get_number_input(min_val=0, max_val=100):
    """Get a valid number from user within range."""
    while True:
        try:
            x = int(input(f"Enter a Number between {min_val} to {max_val}: "))
            if min_val <= x <= max_val:
                return x
            print(f"Please enter a number between {min_val} and {max_val}!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Goodbye!")
            sys.exit(0)

def show_range(number, guess):
    """Visualize how close the guess is to the target (more bars = closer)."""
    diff = abs(number - guess)
    proximity = 50 - (diff // 2)  # Inverted: closer = more bars
    proximity = max(0, min(50, proximity))  # Clamp between 0-50
    print(f"Proximity: [{'#' * proximity}{'-' * (50 - proximity)}]")
    print()

def check_max_attempts(attempts):
    """Check if max attempts reached."""
    if attempts >= MAX_ATTEMPTS:
        print("You have reached the maximum number of attempts.")
        return True
    return False

# ============== Player Functions ==============

def player_turn(number, player_name="Player"):
    """Handle a player's guessing turn."""
    attempts = 0
    
    while True:
        attempts += 1
        print(f"\n[{player_name}] Attempt {attempts}/{MAX_ATTEMPTS}")
        guess = get_number_input()
        
        if guess == number:
            print(f"*** {player_name} guessed Perfect in {attempts} attempts! ***")
            return attempts
        elif guess < number:
            print(">> Higher!")
        else:
            print(">> Lower!")
        
        # Hint after 5 attempts
        if attempts >= 5:
            show_range(number, guess)
        
        if check_max_attempts(attempts):
            return attempts
    
    return attempts

# ============== Computer Functions ==============

def computer_easy(number):
    """Easy mode: Computer guesses randomly within narrowing bounds."""
    attempts = 0
    left, right = 0, 100
    
    while left <= right and attempts < MAX_ATTEMPTS:
        attempts += 1
        guess = randint(left, right)
        print(f"[Computer] Attempt {attempts}/{MAX_ATTEMPTS}: Guessing {guess}...")
        
        if guess == number:
            print(f"*** Computer guessed Perfect in {attempts} attempts! ***")
            return attempts
        elif guess < number:
            print("  Too low!")
            left = guess + 1
        else:
            print("  Too high!")
            right = guess - 1
    
    print("Computer couldn't guess the number.")
    return attempts

def computer_mid(number):
    """Medium mode: Computer uses binary search."""
    attempts = 0
    left, right = 0, 100
    
    while left <= right and attempts < MAX_ATTEMPTS:
        mid = (left + right) // 2
        attempts += 1
        print(f"[Computer] Attempt {attempts}/{MAX_ATTEMPTS}: Guessing {mid}...")
        
        if mid == number:
            print(f"*** Computer guessed Perfect in {attempts} attempts! ***")
            return attempts
        elif mid < number:
            print("  Too low!")
            left = mid + 1
        else:
            print("  Too high!")
            right = mid - 1
    
    print("Computer couldn't guess the number.")
    return attempts

def computer_hard(number):
    """Hard mode: Optimal binary search (always finds in ~7 attempts)."""
    attempts = 0
    left, right = 0, 100
    
    while left <= right:
        mid = (left + right) // 2
        attempts += 1
        print(f"[Computer] Attempt {attempts}: Guessing {mid}...")
        
        if mid == number:
            print(f"*** Computer guessed Perfect in {attempts} attempts! ***")
            return attempts
        elif mid < number:
            left = mid + 1
        else:
            right = mid - 1
    
    return attempts

# ============== Game Flow ==============

def play_again(player_a_wins, player_b_wins, draws, rounds_played, mode):
    """Ask if player wants to play again."""
    print("\n" + "=" * 50)
    choice = get_valid_input("Play Again? [Y]es / [N]o: ", ["y", "n", "yes", "no"])
    
    if choice in ["y", "yes"]:
        return game_start(player_a_wins, player_b_wins, draws, rounds_played)
    else:
        print("\n" + "=" * 50)
        print("           *** GAME OVER ***")
        print("=" * 50)
        print("Final Statistics:")
        print(f"   Rounds Played: {rounds_played}")
        print(f"   Player A Wins: {player_a_wins}")
        opponent = "Player B" if mode == "two" else "Computer"
        print(f"   {opponent} Wins: {player_b_wins}")
        print(f"   Draws: {draws}")
        print()
        
        if player_a_wins > player_b_wins:
            print("[CHAMPION] Player A won the most rounds!")
        elif player_b_wins > player_a_wins:
            print(f"[CHAMPION] {opponent} won the most rounds!")
        else:
            print("[TIE] It's a tie overall!")
        
        print("=" * 50)
        print("Thanks for playing! Goodbye!")
        sys.exit(0)

def game_start(player_a_wins=0, player_b_wins=0, draws=0, rounds_played=0):
    """Main game loop."""
    
    # Game mode selection
    print("\n" + "=" * 50)
    print("       *** PERFECT GUESS GAME ***")
    print("=" * 50)
    print("  1. One Player (vs Computer)")
    print("  2. Two Player")
    print("  Q. Quit")
    print("=" * 50)
    
    mode = get_valid_input("Choose mode: ", ["1", "2", "one", "two", "q", "quit"])
    
    if mode in ["q", "quit"]:
        play_again(player_a_wins, player_b_wins, draws, rounds_played, "one")
        return
    
    # Normalize mode
    if mode == "1":
        mode = "one"
    elif mode == "2":
        mode = "two"
    
    print("\n*** Let's Perfect Guess! ***")
    
    # Initialize the secret number
    number = randint(0, 100)
    print("(Secret number has been chosen between 0-100)")
    
    computer_attempts = 0
    
    # Computer's Turn (only in one-player mode)
    if mode == "one":
        print("\n" + "-" * 30)
        print("Choose Computer Difficulty:")
        print("  E. Easy (Random guessing)")
        print("  M. Medium (Binary search)")
        print("  H. Hard (Optimal search)")
        print("-" * 30)
        
        difficulty = get_valid_input("Difficulty: ", ["e", "m", "h", "easy", "medium", "hard"])
        
        print("\n[Computer's Turn]")
        print("-" * 30)
        
        if difficulty in ["e", "easy"]:
            computer_attempts = computer_easy(number)
        elif difficulty in ["m", "medium"]:
            computer_attempts = computer_mid(number)
        else:
            computer_attempts = computer_hard(number)
    
    # Player A's Turn
    print("\n" + "-" * 30)
    print("[Player A's Turn]")
    print("-" * 30)
    player_a_attempts = player_turn(number, "Player A")
    
    # Player B's Turn (only in two-player mode)
    player_b_attempts = 0
    if mode == "two":
        print("\n" + "-" * 30)
        print("[Player B's Turn]")
        print("-" * 30)
        player_b_attempts = player_turn(number, "Player B")
    else:
        player_b_attempts = computer_attempts
    
    # Reveal the number
    print(f"\nThe secret number was: {number}")
    
    # Determine winner
    print("\n" + "=" * 50)
    rounds_played += 1
    
    opponent_name = "Player B" if mode == "two" else "Computer"
    print(f"Player A: {player_a_attempts} attempts")
    print(f"{opponent_name}: {player_b_attempts} attempts")
    print()
    
    if player_a_attempts == player_b_attempts:
        print("[DRAW] It's a Draw!")
        draws += 1
    elif player_a_attempts < player_b_attempts:
        print("[WINNER] Player A wins this round!")
        player_a_wins += 1
    else:
        print(f"[WINNER] {opponent_name} wins this round!")
        player_b_wins += 1
    
    # Play again?
    play_again(player_a_wins, player_b_wins, draws, rounds_played, mode)

# ============== Main Entry ==============

if __name__ == "__main__":
    try:
        game_start()
    except (EOFError, KeyboardInterrupt):
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)