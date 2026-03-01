import random

def play_guessing_game():
    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts_taken = 0
    
    print("I've picked a number between 1 and 100.")
    print(f"You have exactly {max_attempts} attempts to find it. Good luck!\n")

    while attempts_taken < max_attempts:
        try:
            # Show how many tries are left
            remaining = max_attempts - attempts_taken
            user_input = int(input(f" What's your guess? "))
            
            attempts_taken += 1

            if user_input < 1 or user_input > 100:
                print("Keep it between 1 and 100!")
            elif user_input < secret_number:
                print("Too low! Think bigger.")
            elif user_input > secret_number:
                print("Too high! Scale it back.")
            else:
                print(f"Incredible! You got it in {attempts_taken} tries!")
                return # Exit the function since they won

        except ValueError:
            print("Invalid input. That's going to cost you a try if you aren't careful!")

    # If the loop finishes without a 'return', the user lost
    print("Game Over!")
    print(f"You ran out of tries. The number I was thinking of was {secret_number}.")


play_guessing_game()
print("Thanks for giving it a shot!")
