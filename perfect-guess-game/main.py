from random import randint  # Import function to generate a random number
start = input("Two Player = [Two], One PLayer = [One], Quit Game = [Q] :").lower()

if start == "q":
    print("Game Over!!!")
    exit()
else:
    print("Let's Perfect Guess!!!")
        
print("Player A will start.")
a = int(input("Enter a Number between 0 to 100: "))  # Get the user's initial guess
guess_a = 1  # Initialize guess counter
computer = randint(0, 100)  # Computer randomly selects a number in the given range


if start == "one" or start == "two":

    # Keep asking the user until they guess correctly
    while True:

        if a == computer:  # Case: correct guess
            print("You guessed Perfect!!!")
            print(f"You had guessed {computer} in {guess_a} guesses")  # Show number of attempts
            break  # Exit the loop

        elif a < computer:  # Case: user's guess is too low
            guess_a += 1  # Increment guess counter
            print("Higher")  # Hint to go higher
            a = int(input("Enter a Number between 0 to 100: "))  # Get next guess

        elif a > computer:  # Case: user's guess is too high
            guess_a += 1  # Increment guess counter
            print("Lower")  # Hint to go lower
            a = int(input("Enter a Number between 0 to 100: "))  # Get next guess



    if start == "two":
        print("Player B will start.")
        b = int(input("Enter a Number between 0 to 100: "))  # Get the user's initial guess

        guess_b = 1  # Initialize guess counter

        computer = randint(0, 100)  # Computer randomly selects a number in the given range

        # Keep asking the user until they guess correctly
        while True:

            if b == computer:  # Case: correct guess
                print("You guessed Perfect!!!")
                print(f"You had guessed {computer} in {guess_b} guesses")  # Show number of attempts
                break  # Exit the loop

            elif b < computer:  # Case: user's guess is too low
                guess_b += 1  # Increment guess counter
                print("Higher")  # Hint to go higher
                b = int(input("Enter a Number between 0 to 100: "))  # Get next guess

            elif b > computer:  # Case: user's guess is too high
                guess_b += 1  # Increment guess counter
                print("Lower")  # Hint to go lower
                b = int(input("Enter a Number between 0 to 100: "))  # Get next guess


        if guess_a == guess_b:
            print("It's a Draw")

        elif guess_b > guess_a:
            print("Player A won!!!")

        elif guess_b < guess_a:
            print("Player B won!!!")


        




