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
import random
x=int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))

if x<=2 and x>=0:
  choice = [rock, paper, scissors]
  you = choice[x]
  print(you)

  length = len(choice)-1
  print("Computer chose")
  y = random.randint(0,length)
  computer=choice[y]
  print(y)
  print(computer)
  
  if you==rock and computer==scissors:
    print("You win!")
  elif you==scissors and computer==paper:
    print("You win!")
  elif you==paper and computer==rock:
    print("You win!")
  elif you == computer:
    print("Draw!")
  else:
    print("You lose!")
    
else:
  print("You typed Invalid number!")
