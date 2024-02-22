import os

from blind_auction_art import logo

print(logo)

bid_dict = {}

def add_bid(name, bid):
  bid_dict[name] = bid

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      winner = bidder
      highest_bid = bidding_record[bidder]
  print(f"The winner is {winner} with a bid of ${highest_bid}")

more_bidders = True
while more_bidders:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_bid(name, bid)
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more_bidders == "no":
    more_bidders = False
    find_highest_bidder(bid_dict)
  else:
    os.system('cls' if os.name == 'nt' else 'clear')

    