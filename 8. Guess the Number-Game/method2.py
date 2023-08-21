#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

easy_limit=10
hard_limit=5


print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

easy_limit=10
hard_limit=5

def guess_number():
  guess = int(input("Make a guess: "))
  return guess

def hardness():
  if level == "hard":
    if hard_limit>0:
      print(f"You have {hard_limit} attempts remaining to guess the number")
    else:
      print("You have run out of guesses, you lose")
  elif level =="easy":
    if easy_limit>0:
      print(f"You have {easy_limit} attempts remaining to guess the number")
    else:
      print("You have run out of guesses, you lose")

hardness()
guess = int(input("Make a guess: "))

def match():
  if number==guess:
    print(f"You got it! The answer was {guess}")
  else:
    return False    

while match()==False:
  easy_limit-=1
  hard_limit-=1
  if easy_limit<1 or hard_limit<1:
    print("To low\nGuess again ")
    hardness()
    break
  elif guess>=number:
    print("To high\nGuess again ")
    hardness()
    guess = int(input("Make a guess: "))
  elif guess<=number:
    print("To low\nGuess again ")
    hardness()
    guess = int(input("Make a guess: "))
