# guessing_game.py
import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Try to guess the secret number between 1 and 100.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guessing_game()
