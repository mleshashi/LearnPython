#divide
def divide(n1,n2):
  return n1/n2 
#add
def add(n1,n2):
  return n1+n2
#multiply
def multiply(n1,n2):
  return n1*n2
#subtract
def subtract(n1,n2):
  return n1-n2


operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

import os
from art import logo

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculator():
  print(logo)
  num1 = int(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue=True
  
  while should_continue:
    operation_symbol = input("Pick an operation from above: ")
    if operation_symbol in ("+","-","*","/"):
      num2 = int(input("What's the second number?: "))
      operation_function =operations[operation_symbol]
      answer = operation_function(num1,num2)
      print(f"{num1} {operation_symbol} {num2} ={answer}")
    else:
      print("Oops!! Incorrect symbol")
      operation_symbol = input("Pick an operation again from above: ")
      num2 = int(input("What's the second number?: "))
      operation_function =operations[operation_symbol]
      answer = operation_function(num1,num2)
      print(f"{num1} {operation_symbol} {num2} ={answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower() == "y":
      num1 = answer
    else:
      should_continue = False
      clear_screen()
      calculator()

calculator()