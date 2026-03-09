lines = int(input())
strings = []
for _ in range(lines):
    sentence = input().lower()
    strings.append(sentence)

def check_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for char in word:
        if char in vowels:
            counter += 1
    return counter

v_counter = []
for words in strings:
    v_counter.append(check_vowels(words))

print(' '.join(str(x) for x in v_counter))