def main():
    s = input('Enter a string: ')
    return even_index(s)

def even_index(s):
    for index in range(len(s)):
        if index % 2 == 0:
            print(s[index])

main()