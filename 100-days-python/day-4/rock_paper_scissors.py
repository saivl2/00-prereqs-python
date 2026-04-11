import random



rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
# rock = 0, paper = 1, scissors = 2
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
computer_choice = random.randint(0, 2)
li = [rock, paper, scissors]
if user_input  == computer_choice:
    print(li[computer_choice])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print("It's a draw")
elif user_input == 0 and computer_choice == 1:
    print(li[0])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print('Computer Wins!')
elif user_input == 0 and computer_choice == 2:
    print(li[0])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print('User Wins!')
elif user_input == 1 and computer_choice == 0:
    print(li[1])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print("User Wins!")
elif user_input == 1 and computer_choice == 2:
    print(li[1])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print('Computer Wins!')
elif user_input == 2 and computer_choice == 0:
    print(li[2])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print('Computer Wins!')
elif user_input == 2 and computer_choice == 1:
    print(li[2])
    print(f'Computer Chose:\n{li[computer_choice]}')
    print('User Wins!')