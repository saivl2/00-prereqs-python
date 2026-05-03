WORDS = {'PAIR': 4, 'HAIR': 4, 'CHAIR': 5, "GRAPHIC": 7}

def main():
    print('Welcome to spelling bee')
    print("Your letters are : A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words leeft!")
        guess = input("Guess a word: ")

        if guess == 'GRAPHIC':
            WORDS.clear()
            print('You Won!')
        if guess.upper() in WORDS:
            points = WORDS.pop(guess)
            print(f"Good Job. You scored {points}")

    print("That's the game!")

main()