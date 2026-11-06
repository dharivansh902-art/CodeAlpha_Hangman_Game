
import random

# List of predefined words
words = ["python", "computer", "program", "keyboard", "internet"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("=" * 40)
print("       WELCOME TO HANGMAN GAME")
print("=" * 40)

print("Guess the hidden word, one letter at a time!")
print("You have 6 wrong attempts.")

# Main game loop
while wrong_guesses < max_attempts:

    # Display the word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong attempts:", wrong_guesses, "/", max_attempts)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Take user input
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# Losing condition
if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")

