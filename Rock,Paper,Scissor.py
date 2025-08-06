import random
print("\n######### WELCOME TO THE ROCK PAPER SCISSORS GAME ###########\n")
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

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if user_choice>=0 and user_choice<=2:
    print(images[user_choice])

computer_choose = random.randint(0, 2)
print("Computer choice.")
print(images[computer_choose])

if user_choice>=3 or user_choice<0:
    print("You typed Invalid number. you lose!")
elif (user_choice==0 and computer_choose==2) or (user_choice>computer_choose):
    print("You win!")
elif (computer_choose==0 and user_choice==2) or (computer_choose>user_choice):
    print("Computer win. You lose!")
elif computer_choose==user_choice:
    print("It's Draw")