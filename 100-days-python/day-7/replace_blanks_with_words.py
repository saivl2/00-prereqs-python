import random
word_list = ['aardvark', 'baboon', 'camel']

answer = random.choice(word_list)
user_letter = input("Guess a letter: ").strip().lower()

placeholder = ''
for letter in answer:
    if letter == user_letter:
        placeholder += user_letter
    else:
        placeholder += ' _ '


print(placeholder)