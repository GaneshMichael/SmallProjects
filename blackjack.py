import random

def dealCard():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards) 
    return card


def calculateScore(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, compScore):
    """Compares the user's score and the computer's score and returns the winner."""
    if userScore == compScore:
        return "Draw"
    elif userScore == 0:
        return "Win with a Blackjack"
    elif compScore == 0:
        return "Lose, opponent has Blackjack"
    elif userScore > 21:
        return "You went over. You lose"
    elif compScore > 21:
        return "Opponent went over. You win"
    elif userScore > compScore:
        return "You win"
    else:
        return "You lose"


def playGame():
    """Plays the game of Blackjack."""
    userCards = []
    computerCards = []
    isGameOver = False

    for _ in range(2):
        "Deals two cards to the user and the computer."
        userCards.append(dealCard())
        computerCards.append(dealCard())

    while not isGameOver:
        "While the game is not over, the user can choose to get another card or pass."
        userScore = calculateScore(userCards)
        compScore = calculateScore(computerCards)

        print(f"Your cards: {userCards}, current score: {userScore}")
        print(f"Computers cards: {computerCards}, current score: {compScore}")

        if userScore == 0 or compScore == 0 or userScore > 21:
            isGameOver = True
        else:
            anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
            if anotherCard == 'y':
                userCards.append(dealCard())
                userScore = calculateScore(userCards)
            else:
                isGameOver = True

    while compScore != 0 and compScore < 17:
        "The computer will get another card if the score is less than 17."
        computerCards.append(dealCard())
        compScore = calculateScore(computerCards)

    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"Computer's final hand: {computerCards}, final score: {compScore}")
    print(compare(userScore, compScore))

    while input("Do you want to play again? (y/n):"):
        "The user can choose to play again."
        playGame()

playGame()