alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
  #'encrypt' that takes the 'text' and 'shift' as inputs"
  if direction == "decode":
    shift *= -1

  updated_text = []
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      new_index = index + shift
      updated_letter = alphabet[new_index]
      updated_text.append(updated_letter)
    else:
      updated_text.append(char)

  updated_text=''.join(updated_text)
  print(f"The {direction}d text is {updated_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
  shift = shift % 26
  caesar(text, shift, direction)

  result = input("Type 'yes' if you want to continue. Otherwise type 'no'.\n")

  if result == "no":
    should_continue = False
    print("Thank you for trying the program")
  elif result == "yes":
    should_continue = True
  else:
    print("Wrong input.")
    print("Thank you for trying the program.\n")
  