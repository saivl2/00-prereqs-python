import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
      |
      |
      |
      |
========="""
]

# Expanded word list for more variety
word_list = [
    'aardvark', 'baboon', 'camel', 'python', 'jazz', 'galaxy', 
    'whiskey', 'abrupt', 'blizzard', 'oxygen', 'syndrome', 'vortex'
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
game_over = False

# Track the display and letters already tried
display = ["_"] * word_length
guessed_letters = []

print("Let's play Hangman!")
print(f"Word to guess: {' '.join(display)}")

while not game_over:
    guess = input("\nGuess a letter: ").lower().strip()

    # Input Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try something else!")
        continue

    guessed_letters.append(guess)

    # Check if the guess is correct
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good job! '{guess}' is in the word.")
    else:
        lives -= 1
        print(f"Sorry, '{guess}' is not there. You lose a life.")

    # Show progress
    print(f"{' '.join(display)}")
    print(stages[lives])

    # Check Win/Loss conditions
    if "_" not in display:
        game_over = True
        print("\nCongratulations! You saved the hangman!")
    elif lives == 0:
        game_over = True
        print(f"\nGame Over. You ran out of lives.")
        print(f"The word was: {chosen_word}")