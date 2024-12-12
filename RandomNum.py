import random

print("This is Guessing Game, we will start now!")

def guessing_game():
    while True:
        number_to_guess = random.randint(1, 10)
        print("\nI'm thinking of a number between 1 and 10.")
        
        while True:
            try:
                guess_input = input("Take a guess: ")
                
                if not guess_input.isdigit():
                    raise ValueError("Input is not a valid integer.")
                
                guess = int(guess_input)
                
                if guess == number_to_guess:
                    print("Congratulations! You guessed it!")
                    break
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Invalid input. Please enter a whole number (no decimals).")
        
        choice = input("Would you like to play with me again? (yes/no): ").lower()
        if choice != 'yes':
            print("Thanks for playing with me! Goodbye!")
            break

guessing_game()
