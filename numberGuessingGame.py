#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import * 


Easy = 10
Hard = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Numbers too high")
        return turns - 1
    elif guess < answer:
        print("Numbers too low")
        return turns - 1
    else:
        print(f"correct! The right answer was {answer}")

def difficulty():
    difficulty = input("Select difficulty, type 'easy' or 'hard'")
    if difficulty == 'easy':
        return Easy
    elif difficulty == 'hard':
        return Hard


def game():
    print("Welcome to the number guessing game")
    print("Guess the number between 1 and 100")
    answer = randint(1, 100)
    print(answer)
    turns = difficulty()
    guess = 0

    while guess != answer:
        print(f"you have {turns} attempts remaining!")
        
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("No attempts remaining, you lose.")
            return
        elif guess != answer:
            print("guess again. ")

game()