print('Welcome to the rollercoaster!')
height = int(input('Enter height: '))
age = int(input("Enter age: "))
want_photo = input("Want picture taken? (yes/no) ").strip().lower()

price = 0
if height >= 120:
    if age < 12:
        price += 2
    elif age <= 18:
        price += 7
    else:
        price += 12
    print('You can ride the rollercoaster')
    if want_photo == 'yes':
        price += 3
    print(f"Total price is: {price}")
else:
    print('Sorry you have to grow taller before you can ride.')