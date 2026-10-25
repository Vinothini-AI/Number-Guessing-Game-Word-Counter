
import random
import string
from collections import Counter


def number_guessing_game():
    """Play a number guessing game with attempts and scoring."""

    print("\n===== NUMBER GUESSING GAME =====")
    print("I have selected a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess (1-100): ").strip())

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:
                score = (max_attempts - attempts + 1) * 10
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                print(f"Your score: {score}")
                return

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            print(f"Attempts remaining: {max_attempts - attempts}")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print(f"\nGame over! The correct number was {secret_number}.")
    print("Your score: 0")


def word_counter():
    """Read a text file and analyse word frequencies."""

    print("\n===== WORD COUNTER =====")
    filename = input(
        "Enter text filename (press Enter for sample.txt): "
    ).strip()

    if not filename:
        filename = "sample.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Make all words lowercase and remove punctuation.
        cleaned_text = text.translate(
            str.maketrans("", "", string.punctuation)
        ).lower()

        words = cleaned_text.split()

        if not words:
            print("The file is empty or contains no words.")
            return

        word_counts = Counter(words)

        print("\n===== WORD ANALYSIS RESULTS =====")
        print(f"Total words: {len(words)}")
        print(f"Unique words: {len(word_counts)}")
        print("\nTop 10 most frequent words:")

        for word, count in word_counts.most_common(10):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("File not found! Check the filename and try again.")

    except OSError as error:
        print(f"Could not read the file: {error}")


def main():
    """Display the main menu until the user exits."""

    while True:
        print("\n================================")
        print(" NUMBER GUESSING GAME")
        print("       & WORD COUNTER")
        print("================================")
        print("1. Play Number Guessing Game")
        print("2. Analyse a Text File")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("Thank you for using the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
