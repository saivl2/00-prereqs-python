import random
word_list = ['aardvark', 'baboon', 'camel']

answer = random.choice(word_list)


print(len(answer) * ' _ ')
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

    if " _ " not in placeholder:
        game_over = True
        print('You Win!')


