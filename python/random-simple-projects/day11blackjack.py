############### FEEDBACK #####################
#use more function for this for greater modularity
#question, cards do not need to be the argument for this to work. However, if ComputerCards and PlayerCards is not a local variable inside the function
#(or it is not an argument for the function if those 2 variables were defined outside the function), there would be an error. why? wtf? that's... inconsistent

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# from art import logo
# from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack(cards):
  computerCards = []
  playerCards = []
#   print(logo)
  game_running = True
  while game_running:
    for i in range(2):
      computer = random.choice(cards)
      player = random.choice(cards)
      computerCards.append(computer)
      playerCards.append(player)
      if sum(computerCards) == 22:
        computerCards[0] = 1
      if sum(playerCards) == 22:
        playerCards[0] = 1
    getting_card = True
    while getting_card:
      print(f"\tYour cards: {playerCards}, current score: {sum(playerCards)}")
      print(f"\tComputer's first card: {computerCards[0]}")
      choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if choice == 'y':
        player = random.choice(cards)
        playerCards.append(player)
        if sum(playerCards) > 21 and player == 11:
          playerCards[len(playerCards) - 1] = 1
          if sum(playerCards) > 21:
            getting_card = False
            break
        elif sum(playerCards) > 21 and player != 11:
          getting_card = False
          break
      elif choice == 'n':
        getting_card = False
        while sum(computerCards) < 17:
          computer = random.choice(cards)
          computerCards.append(computer)
    print(f"\tYour final cards: {playerCards}, Final score: {sum(playerCards)}")
    print(f"\tComputer's final card: {computerCards}, Final score: {sum(computerCards)}")
    if sum(playerCards) > 21:
      print("You went over. You lose.")
    elif sum(computerCards) > 21:
      print("The computer went over. You won!")
    elif sum(playerCards) > sum(computerCards):
      print("Congrats, You Won!")
    elif sum(playerCards) < sum(computerCards):
      print("Computer had more score. You Lost.")
    elif sum(playerCards) == sum(computerCards):
      print("Same score. It's a draw.")
    choice = input("Wanna play again?\n1. Yes\n2. No\n> ")
    if choice == '1':
      computerCards = []
      playerCards = []
    #   clear()
    elif choice == '2':
      game_running = False
    else:
      print("Wrong input, meh just gotta assume it's a no yeah? fair yeah? bye.")
      game_running = False

goofy_start = input("Do you want to play the Blackjack?\n1. Yes\n2. No\n> ")
if goofy_start == '1':
  blackjack(cards)
elif goofy_start == '2':
  print("Ok, WTF?")
else:
  print("Dumbass, wrong input. I'm not even gonna bother letting you try re-inputting your answer. Just restart the program if you want to play haha.")