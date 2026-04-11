import random
print("Welcome to the PYPassword Generator!")

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_lettters = int(input("How many letters would you like in your password?\n "))
num_symbols = int(input("How many symbols would you like?\n "))
num_numbers = int(input("How many numbers would you like?\n "))

secret_letters = []
for _ in range(num_lettters):
    secret_letters.append(random.choice(letters))

secret_symbols = []
for _ in range(num_symbols):
    secret_symbols.append(random.choice(symbols))

secret_numbers = []
for _ in range(num_numbers):
    secret_numbers.append(random.choice(numbers))

password_list = secret_letters + secret_symbols + secret_numbers
random.shuffle(password_list)

print(''.join(password_list))