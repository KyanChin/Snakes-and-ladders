#Map: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ymimports.com%2Fpages%2Fhow-to-play-snakes-and-ladders&psig=AOvVaw2PcpmjKP-I_x0IDmCP_NlP&ust=1712807838199000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDs9OzgtoUDFQAAAAAdAAAAABAI
#Snakes: 32 -> 10, 36 -> 6, 48 -> 26, 62 -> 18, 88 -> 24, 95 -> 56, 97 -> 78
#Ladders: 1 -> 38, 4 -> 14, 8 -> 30, 21 -> 42, 28 -> 76, 50 -> 67, 71 -> 92, 80 -> 99

#Modules
import random


#Function to return a random number 1 to 6
def rand():
    return random.randint(1, 6)

#Function for pray (slighly rig the odds [by ~11.9% more in favour of number])
def pray(number):
    odds = [1, 2, 3, 4, 5, 6]
    odds.append(number)
    return random.choice(odds) 

#Dictionary for snakes and ladders
ladders = {
    1: 38,
    4: 14,
    8: 30,
    21: 42,
    28: 76,
    50: 67,
    71: 92,
    80: 99
    }

snakes = {
    32: 10,
    36: 6,
    48: 26,
    62: 18,
    88: 24,
    95: 56,
    97: 78
    }

#Starting positions of player1 and player2
player1 = rand()
player2 = rand()
print(f'Player 1 starts at {player1}, player 2 starts at {player2}', end = '\n\n')

turn = 0
while player1 < 100 and player2 < 100: #Game will continue until someone reach tile 100 or above
    #Check if player1 or player2 hit a ladder
    if player1 in ladders: 
        print(f'Player 1 climbed a ladder from {player1} to {ladders[player1]}! Current position: {ladders[player1]}')
        player1 = ladders[player1]
    if player2 in ladders:
        print(f'Player 2 climbed a ladder from {player2} to {ladders[player2]}! Current position: {ladders[player2]}')
        player2 = ladders[player2]
        
    #Check if player1 or player2 hit a ladder
    if player1 in snakes: 
        print(f'Player 1 slipped down a snake from {player1} to {snakes[player1]}! Current position: {snakes[player1]}')
        player1 = snakes[player1]
    if player2 in snakes:
        print(f'Player 2 slipped down a snake from {player2} to {snakes[player2]}! Current position: {snakes[player2]}')
        player2 = snakes[player2]

    print()
    
    cont = True #Validity Check
    while cont:
        if turn % 2 == 0: #Prompts for different players
            print(f'Current tile: {player1}')
            player_turn = str(input('(P1) Enter a number u hope u get: '))
        else:
            print(f'Current tile: {player2}')
            player_turn = str(input('(P2) Enter a number u hope u get: '))
            
        if player_turn.isdigit(): #Type check 
            player_turn = int(player_turn)
            if player_turn in range(1, 7): #Range check
                cont = False
            else:
                print('Please enter again.')
        else:
            print('Please enter again.')

    
    if turn % 2 == 0: #decide whose turn it is
        dice = pray(player_turn)
        print(f'Player 1 rolled a {dice}. Current position: {player1 + dice}')
        player1 += dice #add steps to current position
    else:
        dice = pray(player_turn)
        print(f'Player 2 rolled a {dice}. Current position: {player2 + dice}')
        player2 += dice #add steps to current position

    turn += 1

if player1 >= 100: #Decides who wins
    print('Player 1 wins')
else:
    print('Player 2 wins')
