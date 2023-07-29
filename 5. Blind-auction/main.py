from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

data = {}
question = "yes"
while not question == "no":
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  data[name] = bid
  question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if (question != "yes" and  question != "no"):
    print("Invalid answer")
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")


print(data)

highest_bid = 0
highest_bidder=''
for name in data:
  bidding_amount = data[name]
  if bidding_amount>highest_bid:
    highest_bid = bidding_amount
    highest_bidder = name

clear()
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


