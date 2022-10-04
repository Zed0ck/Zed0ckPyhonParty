# This is third lesson in Python Party project
# Here I try to make simple rock, paper, scissors game

import random, sys

print('ROCK, PAPER, SCISSORS')

# Track your games with these variables
wins = 0
losses = 0
ties = 0

while True: # Loop for the main game
  print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
  while True: # Loop for the player input
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    playerMove = input()
    if playerMove == 'q':
      sys.exit() # Quit the game.
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
      break # Break player input loop
    print('Type one of r, p, s or q.')
    
    # Display what player chose:
    if playerMove == 'r':
      print('ROCK versus...')
    elif playerMove == 'p':
      print('PAPER versus...')
    elif playerMove == 's':
      print('SCISSORS versus...')
      
    # Display what the computer choce:
    randomNumber = random.randint(1,3) # Use random to randomize computers choose
    if randomNumber == 1:
      computerMove = 'r':
        print('ROCK versus...')
    elif randomNumber == 2:
      computerMove = 'p':
        print('PAPER versus...')
    elif randomNumber == 3:
      computerMove = 's':
        print('SCISSORS versus...')
    
    # Display and record the win/loss/tie:
    if playerMove == computerMove:
      print('It is a tie')
      ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
      print('You win')
      wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
      print('You win')
      wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
      print('You win')
      wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
      print('You lose')
      losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
      print('You lose')
      losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
      print('You lose')
      losses = losses + 1
