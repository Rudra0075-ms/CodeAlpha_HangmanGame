import random

# Words for the game
words = ["python", "computer", "developer", "college", "programming"]

# Choose a random word
word = random.choice(words)

# Store letters guessed by the player
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You have 6 wrong guesses.\n")


while wrong_guesses < max_wrong_guesses:

    # Show the word with guessed letters
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\nYou won!")
        print("The word was:", word)
        break

    # Take a guess
    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Store the new guess
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
        print()

# Game over
if wrong_guesses == max_wrong_guesses:
    print("Game over!")
    print("The word was:", word)