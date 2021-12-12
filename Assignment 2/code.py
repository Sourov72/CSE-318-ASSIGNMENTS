


from mancalaPlay import *


playerTurn = int(input("which player will play first?: "))

if(playerTurn == 2):
    playerTurn = 0
    

m = manacalaPlay(playerTurn, 7)

m._printBoard(m.board)

m._play()




