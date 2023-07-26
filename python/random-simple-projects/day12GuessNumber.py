import random

def checkGuess(number, guess):
    if number == guess:
        return 0
    elif number > guess:
        return -1
    elif number < guess:
        return 1

difficulty = {
    "easy": 10,
    "hard": 5
}

chosenNumber = random.randint(0, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 100.")
playerLevel = input("Choose a difficulty, type 'easy' or 'hard': ").lower()
print(playerLevel)
lives = difficulty[playerLevel]
while lives != 0:
    print(f"You have {lives} attempt(s) left.")
    playerGuess = int(input("Guess the number: "))
    result = checkGuess(chosenNumber, playerGuess)
    lives -= 1
    if result == 0:
        print("You guessed it! You won!")
        break
    elif lives == 0:
        print("Wrong guess! No more attempt left. You lost :(")
        print(f"My number was {chosenNumber}")
        break
    elif result > 0:
        print("Too high, try again!")
    elif result < 0:
        print("Too low, try again!")