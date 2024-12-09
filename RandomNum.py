import random
print("This is Quessing Game, we will strat now!")
def guessing_game():
    while True:
        number_to_guess = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100.")
        
        while True:
            try:
                guess = int(input("Take a guess: "))
                
                if guess == number_to_guess:
                    print("Congrate!, you guessed it!")
                    break
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
            except ValueError:
                print("Invalid input. Please enter a number only.")
        
        choice = input("Would you like to play with me again? (yes/no): ").lower()
        if choice != 'yes':
            print("Thanks for playing with me! Goodbye!")
            break

guessing_game()
