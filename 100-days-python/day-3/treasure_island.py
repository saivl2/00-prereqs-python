art = r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
'''

print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
print("You're at a cross road. Where do you want to go?")
task1 = input('Type "left" or "right"\n ')

if task1 == 'left':
    task2 = input('"swim" or "wait"?\n')
    if task2 == 'wait':
        task3 = input('Which door? (red, yellow, blue)\n')
        if task3 == 'red':
            print('Burned by fire. Game Over')
        elif task3 == 'yellow':
            print('You Won !')
        elif task3 == 'blue':
            print("Eaten by beasts. Game Over")
        else:
            print('Game Over.')
    else:
        print('Attacked by trout. Game Over')
else:
    print('Fall into a hole. Game Over')