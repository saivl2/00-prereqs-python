def main():
    s = input('Enter String: ')
    char = int(input('Enter index: '))
    return substring(s, char)

def substring(s, char):
    new_string = s[char:]
    return new_string

print(main())