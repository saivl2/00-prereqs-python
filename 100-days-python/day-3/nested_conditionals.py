print('Welcome to the rollercoaster!')
height = int(input('Enter height: '))
age = int(input("Enter age: "))

if height >= 120:
    if age < 12:
        print('Pay $5')
    elif age <= 18:
        print('Pay $7')
    else:
        print('Pay $12')
    print('You can ride the rollercoaster')
else:
    print('Sorrry you have to grow taller before you can ride.')