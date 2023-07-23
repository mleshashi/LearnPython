#Step 5

import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

print(logo)


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#print(f"The chosen_word word is: {chosen_word}")

end_of_game = False
lives = 6


#Create blanks
display = []
for _ in range(word_length):
  display.append("_")

while not end_of_game:
  guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print(f"You've already guessed {guess}")

  #Check guessed letter
  for idx in range(word_length):
    letter = chosen_word[idx]
    if guess==letter:
      display[idx] = guess

  #Check if user is wrong.
  if guess not in chosen_word:
    lives-=1
    print(f"Your guess {guess}, that's not in the word. You lose a life")
        
  if lives<=0:
    end_of_game = True
    print("You Loose.:(")
    print(f"The word is {chosen_word}")
    

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("Congratulations! You win.:)")

    
  current_live = stages[lives]
  print(current_live)
