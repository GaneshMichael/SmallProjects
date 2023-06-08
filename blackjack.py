import random

def dealCard():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards) 
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    "Deals two cards to the user and the computer."
    user_cards.append(dealCard())
    computer_cards.append(dealCard())

def calculateScore(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

calculateScore(user_cards)
calculateScore(computer_cards)
