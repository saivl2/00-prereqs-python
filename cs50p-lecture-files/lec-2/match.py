name = input().lower()

match name:
    case 'harry' | 'ron' | 'hermione':
        print('Gryffindor')
    case 'draco':
        print('Slytherin')
    case _:
        print('Who?')