# Simple Hangman Game (Improved Version)

# Step 1: Word list
words = ["apple", "banana", "mango", "pineapple", "strawberry", "kiwi", "watermelon", "papaya", "guava", "lychee", "dragonfruit", "jackfruit", "starfruit", "passion fruit", "blueberry", "raspberry", "blackberry", "cranberry", "gooseberry", "elderberry", "orange", "lemon", "lime", "grapefruit", "tangerine", "clementine", "pomelo", "peach", "plum", "cherry", "apricot", "nectarine", "date", "fig", "pomegranate", "persimmon", "quince", "mulberry", "tamarind", "longan", "rambutan", "durian", "soursop", "coconut", "avocado", "grape", "pear", "cantaloupe", "honeydew", "boysenberry"]

import random
word = random.choice(words)

# Step 2: Track guessed letters
guessed = []

# Step 3: Attempts
attempts = 6

print("Welcome to Hangman!")

# Game loop
while attempts > 0:
    display = ""

    # Show word progress
    for letter in word:
        if letter in guessed:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)
    print("Guessed letters:", guessed)

    # Win check
    if "_" not in display:
        print("You won!")
        break

    # Take input
    guess = input("Guess a letter: ")
    guess = guess.lower()
    
    # Input validation
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    # Already guessed
    if guess in guessed:
        print("You already guessed that letter.")
        continue

    # Check guess
    if guess in word:
        print("Correct!")
        guessed.append(guess)
    else:
        print("Wrong!")
        attempts = attempts - 1
        guessed.append(guess)
        print("Attempts left:", attempts)

# Game over
if attempts == 0:
    print("\nGame Over! The word was:", word)