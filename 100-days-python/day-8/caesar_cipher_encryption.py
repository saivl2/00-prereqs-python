alphabet = 'abcdefghijklmnopqrstuvwxyz'

direction = input("Type 'encode' or 'decode': ").lower()
text = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

def encrypt(text, shift):
    encrypt_text = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.find(letter)
            new_index = (index + shift) % 26
            encrypt_text += alphabet[new_index]
    return encrypt_text


print(encrypt(text, shift))
    