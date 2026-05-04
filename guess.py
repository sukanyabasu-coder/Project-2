import random
best_score = None

def choose_difficulty():

    print("\nChoose Difficulty Level")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return 10

    elif choice == "2":
        return 50

    elif choice == "3":
        return 100

    else:
        print("Invalid choice. Defaulting to Easy level.")
        return 10

def play_game():

    global best_score

    max_number = choose_difficulty()

    random_number = random.randint(1, max_number)

    attempts = 0

    print(f"\nI have selected a number between 1 and {max_number}")

    while True:

        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < random_number:
                print("Too low! Try again.")

            elif guess > random_number:
                print("Too high! Try again.")

            else:
                print("\nCorrect! You guessed the number.")
                print(f"You guessed it in {attempts} attempts.")

                # Update best score
                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print("New Best Score!")

                print(f"Best Score: {best_score}")

                break

        except ValueError:
            print("Please enter a valid number.")

while True:

    print("\n===== NUMBER GUESSING GAME =====")

    play_game()

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThank you for playing!")
        break