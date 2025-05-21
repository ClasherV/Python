# Write a Program to perform a Silent Auction

import os
print("Welcome to Silent Auction\n")
bidders_data={}
def auction(bidders_data):
    highest_bid=0
    winner=""
    for bidder in bidders_data:
        bid_price=bidders_data[bidder]
        if bid_price>highest_bid:
            highest_bid=bid_price
            winner=bidder
    print(f"Here is a List of all the Bidders: {bidders_data}")
    print(f"Winner is {winner} with a Bid Price of {highest_bid}")
end_of_auction=False
while not end_of_auction:
    name=input("Enter Your Name: ")
    bid=int(input("What is Your Bid?: "))
    bidders_data[name]=bid
    more_bidders=input("Are there more Bidders? ('Yes' or 'No): ").lower()
    if more_bidders=='no':
        auction(bidders_data)
        end_of_auction=True
    elif more_bidders=='yes':
        os.system('cls')