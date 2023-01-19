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

#Write your code below this line 👇

game_iamges = [rock,paper,scissors]
user_choice = int(input("press 0 for Rock, 1 for paper, 2 for scissor.\n"))

computer_choice = random.randint(0,2)
if user_choice >=3 or user_choice < 0:
  print("invalid input")
else:
  print("you choose")
  print(game_iamges[user_choice]) 
  print("computer choose")
  print(game_iamges[computer_choice])
  if user_choice == 0 and computer_choice == 2:
    print("you win!")
  elif computer_choice == 0 and user_choice == 2:
    print("you loose")
  elif computer_choice > user_choice:
    print("you lose")
  elif user_choice > computer_choice:
    print("you win!")
  else:
    print("draw")
    
  