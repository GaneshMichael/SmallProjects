import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

choice = int(input("Type '0' for rock, '1' for paper or '2' for scissors"))

comp_choice = random.randint(0, 2)

if choice >= 3 or choice < 0:
    print("Invalid choice, game over!")
elif choice == 0 and comp_choice == 2:
    print("You win!")
elif comp_choice == 0 and choice == 2:
    print("You lose")
elif comp_choice > choice:
    print("You lose")
elif choice > comp_choice:
    print("You win!")
elif comp_choice == choice:
    print("It's a draw")
