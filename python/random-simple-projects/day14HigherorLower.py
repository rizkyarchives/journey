# CANNOT RUN THE PROGRAM, I COULDN'T REMEMBER WHERE I PUT THE art, game_data files. This code was created and tried in replit as well.
# import art
# from game_data import data
# import random
# from replit import clear

# def compareFollowers(followers1, followers2):
#   if followers1 > followers2:
#     return 'A'
#   elif followers1 < followers2:
#     return 'B'
#   else:
#     return 'C'

# def nextComparison(celebChosen):
#   picking = True
#   celebChosen[0] = celebChosen[1]
#   while picking:
#     celebChosen[1] = random.choice(data)
#     if celebChosen[1] != celebChosen[0]:
#       return celebChosen
      
# print(art.logo)
# score = 0
# game_running = True
# celebToCompare = random.sample(data, 2)
# while game_running:
#   print(f"Compare A: {celebToCompare[0]['name']}, a {celebToCompare[0]['description']}, from {celebToCompare[0]['country']}.")
#   print(art.vs)
#   print(f"Againts B: {celebToCompare[1]['name']}, a {celebToCompare[1]['description']}, from {celebToCompare[1]['country']}.")
#   result = compareFollowers(celebToCompare[0]['follower_count'], celebToCompare[1]['follower_count'])
#   playerAnswer = input("Who has more followers? 'A' or 'B'? ")
#   clear()
#   print(art.logo)
#   if playerAnswer == result:
#     score += 1
#     print(f"You're right! Current score: {score}")
#     celebToCompare = nextComparison(celebToCompare)
#   elif playerAnswer != result:
#     break
# print(f"Sorry, that's wrong. Game Over! Final score: {score}.") 
