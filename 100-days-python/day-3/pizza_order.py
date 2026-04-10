print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S, M or L: ')
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input('Do you want extra cheese? Y or N: ')

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_small_prize = 2
pepperoni_medium_or_prize = 3
extra_cheese_price = 1

total_bill = 0
if size == 'L':
    if pepperoni == 'Y':
        if extra_cheese == 'Y':
            total_bill += large_pizza_price + pepperoni_medium_or_prize + extra_cheese_price
        else:
            total_bill += large_pizza_price + pepperoni_medium_or_prize
    else:
        total_bill += large_pizza_price

elif size == 'M':
    if pepperoni == 'Y':
        if extra_cheese == 'Y':
            total_bill += medium_pizza_price + pepperoni_medium_or_prize + extra_cheese_price
        else:
            total_bill += medium_pizza_price + pepperoni_medium_or_prize
    else:
        total_bill += medium_pizza_price


elif size == 'S':
    if pepperoni == 'Y':
        if extra_cheese == 'Y':
            total_bill += small_pizza_price + pepperoni_small_prize + extra_cheese_price
        else:
            total_bill += small_pizza_price + pepperoni_small_prize
    else:
        total_bill += small_pizza_price
else:
    print('Invalid Input !')

print(f"Your final bill is: ${total_bill}")


