stages = [
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
"""
]
lives = 6
import random
word_list = ['aardvark', 'baboon', 'camel']
answer = random.choice(word_list)

print('_ ' * len(answer))
user_guess_letters = []
game_over = False
while not game_over:
    user_letter = input("Guess a letter: ").strip().lower()

    placeholder = ''

    for letter in answer:
        if letter == user_letter:
            placeholder += user_letter
            user_guess_letters.append(letter)
        elif letter in user_guess_letters:
            placeholder += letter
        else:
            placeholder += ' _ '
    print(placeholder)

    if user_letter not in answer:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You Lose.')

    if " _ " not in placeholder:
        game_over = True
        print('You Win!')
    
    # Print the ASCII art
    print(stages[lives])



