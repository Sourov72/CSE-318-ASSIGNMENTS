
from mancalaPlay import *



gameType = int(input("press 1: human vs computer and press 2: computer vs computer: "))

depth1 = 0
depth2 = 0

type1 = 0
type2 = 0

move = int(input("press 1: experiment with move ordering"))

winner = [0, 0, 0]

if(gameType == 1):
    if(move != 1):
        depth2 = int(input("depth for computer? "))
    type2 = int(input("The type of herustic you want to choose?: "))

else:
    if(move != 1):
        depth1 = int(input("depth for computer player 1?: "))

        depth2 = int(input("depth for computer player 2?: "))
    else: 
        depth1 = depth2 = 1
    
    type1 = int(input("heuristic choosen for player 1: "))
    
    type2 = int(input("heuristic choosent for player 2: "))


playerTurn = int(input("which player will play first?: "))



if(playerTurn == 2):
    playerTurn = 0
    
 
for i in range(1):    


    # depth1 = random.randint(3, depth1)
    # depth1 = random.randint(3, depth2)
    m = manacalaPlay(playerTurn, gameType, depth1, depth2, type1, type2, move)

    m._printBoard(m.board)

    winner[m._play()] += 1
    

print("winner 1", winner[1])
print("winner 2", winner[2])
print("game tied", winner[0])



