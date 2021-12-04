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

choice_list = [rock, paper, scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
random_choice = random.randint(0,2)

#Paper wins against Rock
#Scissors wins against Paper
#Rock wins against Scissors

print("Your Chose:")
print(choice_list[user_input])
print("Computer Chose:")
print(choice_list[random_choice])
    
if user_input==0:
    if random_choice ==1:
        print("You lose")
    elif random_choice==0:
        print("Tie")
    else:
        print("You win")
elif user_input==1:
    if random_choice==2:
        print("You lose")
    elif random_choice==1:
        print("Tie")
    else:
        print("You win")
elif user_input==2:
    if random_choice==0:
        print("You lose")
    elif random_choice==2:
        print("Tie")
    else:
        print("You win")
else:
    print("Enter correct input")
