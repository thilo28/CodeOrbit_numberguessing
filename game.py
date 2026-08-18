import random


def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")

            elif guess > number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed the number!")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        play_game()

        choice = input("\nDo you want to play again? (yes/no): ").lower()

        if choice != "yes":
            print("Thanks for playing!")
            break


main()]