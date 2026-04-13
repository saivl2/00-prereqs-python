alphabet = 'abcdefghijklmnopqrstuvwxyz'

direction = input("Type 'encode' or 'decode': ").lower()
text = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

def main():
    if direction == 'encode':
        return encrypt(text, shift)
    else:
        return decode(text, shift)
    
def encrypt(text, shift):
    encrypt_text = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.find(letter)
            new_index = (index + shift) % 26
            encrypt_text += alphabet[new_index]
    return encrypt_text

def decode(text, shift):
    decode_text = ''
    for letter in text:
        if letter in alphabet:
            index = alphabet.find(letter)
            new_index = (index - shift) % 26
            decode_text += alphabet[new_index]
    return decode_text

print(main())