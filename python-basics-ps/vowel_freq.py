s = input("Enter string: ").lower().strip()
vowels_counter = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in s:
    if char in vowels:
        vowels_counter += 1
print(vowels_counter)