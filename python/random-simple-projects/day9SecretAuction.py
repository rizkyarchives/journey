# art and replit is not necessary you could just delete them if you want to run it. (and perhaps find a replacement for clear())
# from replit import clear
# from art import logo
#HINT: You can call clear() to clear the output in the console.

auction_data = {"blank": 0}
def input_data():
  name = input("What is your name? ")
  price = float(input("What's your bid? $"))
  auction_data[name] = price

def whoWin(auction_data):
  winner = ["blank"]
  for key in auction_data:
    if auction_data[key] != 0 and auction_data[key] > auction_data[winner[0]]:
      winner = []
      winner.append(key)
    elif auction_data[key] == auction_data[winner[0]]:
      winner.append(key)  
  return winner

# print(logo)
print("Welcome to Auctioner!")
auctioning = True
noWinner = True
while noWinner:
  while auctioning:
    input_data()
    errorChecking = True
    while errorChecking:
      continuing = input("Is there anyone else who wants to participate? 'yes' or 'no':\n")
      if continuing == 'no':
        auctioning = False
        errorChecking = False
      elif continuing == 'yes':
        break
      elif continuing != 'no' or continuing != 'yes':
        print("Wrong input. Retrying...")
    # clear()
  winner = whoWin(auction_data)
  if len(winner) == 1:
    print(f"The winner for this auction is {winner[0]} with a bid value of ${auction_data[winner[0]]}.")
    noWinner = False
  elif len(winner) > 1:
    string = ', '.join(winner)
    print(f"There are {len(winner)} winners this round. They are {string} with bid values of ${auction_data[winner[0]]}. A round restart is necessary.")
    auction_data = {"blank": 0}
    winner = []
    auctioning = True
    # clear()
    print("Start of next round.")
      