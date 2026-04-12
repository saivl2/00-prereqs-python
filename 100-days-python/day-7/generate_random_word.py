import random
word_list = ['aardvark', 'baboon', 'camel']

answer = random.choice(word_list)

user_letter = input("Guess a letter: ").strip().lower()

for letter in answer:
    if letter == user_letter:
        print('Right')
    else:
        print('Wrong')