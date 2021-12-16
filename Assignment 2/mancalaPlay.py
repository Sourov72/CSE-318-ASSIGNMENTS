


import copy

from math import inf

from mancalaBoard import *


from Heuristic import *
class manacalaPlay:
    
    def __init__(self, currentplayer, gametype, depth1, depth2, type1 , type2, move):
        self.noofBins = 6
        self.noofStones = 4
        self.board=[]
        self.noofPlayers = 2
        self.currentplayer = currentplayer
        self.depth1 = depth1
        self.depth2 = depth2
        self.type1 = type1
        self.type2 = type2
        self.gameType = gametype
        self._initiate()
        self.heuristic = Heurisitic()
        self.mainBoard = mancalaBoard(self.currentplayer, self.board)
        # self.f = open("write.txt", "w")
        
        
    def _initiate(self):
        
        for i in range(self.noofPlayers):
            temp = []
            for j in range(self.noofBins):
                temp.append(int(self.noofStones))
            temp.append(0)
            self.board.append(temp)
            
            
            
    def _moveOrdering(self, mboard):
        
        childList = []
        
        for i in range(mboard.storage):
            
            temp=[]
            
            
            if(self.mboard._getboard()[self.mboard._getcurrentPlayer()][i] == 0):
                continue
            m = copy.deepcopy(self.mboard)
            
            m._move(i)
            if(self.mainBoard._getcurrentPlayer() == 1):
                res = self.heuristic._heuristic(m, self.mainBoard._getcurrentPlayer(), self.type1)
                # self.f.write(str(ret) + "\n")

            else:
                res = self.heuristic._heuristic(m, self.mainBoard._getcurrentPlayer(), self.type2)
                
            temp.append(res)
            temp.append(i)
            temp.append(m)
            childList.append(temp)
            
        return childList
                
                
            
            
            
               
                   
    
    def _play(self):
        
        i = 0
        depth1here = -inf
        depth2here = -inf
        while(True):
            
            
            # print("current player", self.mainBoard._getcurrentPlayer())
        
            # print("opposite player", 1 - self.mainBoard._getcurrentPlayer())
            
            # print("current capture ", self.mainBoard._getcapturemove(self.mainBoard._getcurrentPlayer()))
            
            # print("opponent capture ",  self.mainBoard._getcapturemove(1 - self.mainBoard._getcurrentPlayer()))
            
            depth1here = -inf
            depth2here = -inf
            if(self.mainBoard._getcurrentPlayer() == 0 or self.gameType == 2):
                bestPos = -1
                alpha = -inf
                beta = inf
                maxEval = -inf
                
                
                if(self.mainBoard._getcurrentPlayer() == 1):
                    htype = self.type1
                    depth = self.depth1
                else:
                    htype = self.type2
                    depth = self.depth2
                
                
                if(self.mainBoard._gameover(self.mainBoard._getoppositePlayer()) or self.mainBoard._gameover(self.mainBoard._getcurrentPlayer())):
                    self._printBoard(self.mainBoard._getboard())
                    return self.mainBoard._gamewin()
                  
                  
                if(depth == 0):
                    print("Game Tied")
                    break
                    
                    
                
                for i in range(6):
                    if(self.mainBoard._getboard()[self.mainBoard._getcurrentPlayer()][i] == 0):
                        continue
                    m = copy.deepcopy(self.mainBoard)

                    
                    if(not m._move(i)):

                        eval = self._minimax(m, depth - 1, alpha, beta, False, self.mainBoard._getoppositePlayer())
                        
                        
                    else:

                        eval = self._minimax(m, depth - 1, alpha, beta, True, self.mainBoard._getcurrentPlayer()) 
                        
                        
                    
                    if(eval > maxEval):
                        
                        bestPos = i
                        maxEval = eval
                        
                        depth1here = capture1
                        depth2here = capture2
                        
                    alpha = max(alpha, eval)
                    
                    
                    if (beta <= alpha):
                        break                    
                    

            else:
                if(not (self.mainBoard._gameover(self.mainBoard._getoppositePlayer()) or self.mainBoard._gameover(self.mainBoard._getcurrentPlayer()))):
                    bestPos = input("which bin you want to select?: ") 
                    bestPos = ord(bestPos) - 97
                else: 
                    bestPos = -1
            
            
            if(bestPos == -1):
                self._printBoard(self.mainBoard._getboard())
                return self.mainBoard._gamewin()
                
            if(self.mainBoard._getcurrentPlayer() == 0):
                
                print("player 2's move: chosen position for next move: ")
            else:
                
                print("player 1's move: chosen position for next move: ")
                
                
            print("captured value for ", self.mainBoard._getcurrentPlayer(), depth1here)    
            print("captured value for ", 1 - self.mainBoard._getcurrentPlayer(), depth2here)
                
            print(chr(bestPos + 97))
            if(not self.mainBoard._move(bestPos)): 
                self.mainBoard._setcurrentPlayer(self.mainBoard._getoppositePlayer())
                
            self.mainBoard._reset()
            self._printBoard(self.mainBoard._getboard())
            
            
            
            
    
    def _minimax(self, testmancalaBoard, depth, alpha, beta, maximizingPlayer, playerTurn):
        
        # here testmancalaBoard is a manacalaBoard object
        

        
        
        if(testmancalaBoard._gameover(self.mainBoard._getcurrentPlayer()) or testmancalaBoard._gameover(self.mainBoard._getoppositePlayer()) or depth == 0):
            
            global capture1, capture2
            
            capture1 = testmancalaBoard._getcapturemove(self.mainBoard._getcurrentPlayer())
            
            capture2 = testmancalaBoard._getcapturemove(1 - self.mainBoard._getcurrentPlayer())
            
            
            
            if(self.mainBoard._getcurrentPlayer() == 1):
                return self.heuristic._heuristic(testmancalaBoard, self.mainBoard._getcurrentPlayer(), self.type1)
                # self.f.write(str(ret) + "\n")

            else:
                return self.heuristic._heuristic(testmancalaBoard, self.mainBoard._getcurrentPlayer(), self.type2)
                # self.f.write(str(ret) + "\n")
        
        if(maximizingPlayer):
            maxEval = -inf
            for i in range (6):

                if(testmancalaBoard._getboard()[playerTurn][i] == 0):
                    continue;
                
                m = copy.deepcopy(testmancalaBoard)
                m._setcurrentPlayer(playerTurn)
                
                
                if(not m._move(i)):

                    eval = self._minimax(m, depth - 1, alpha, beta, False, 1 - playerTurn)
                else:

                    eval = self._minimax(m, depth - 1, alpha, beta, True, playerTurn)
                    
                
                    
                maxEval = max(eval, maxEval)
                
                alpha = max(alpha, eval)
                
                
                if (beta <= alpha):
                    break
                
            return maxEval
                
        else:

            minEval = inf
            for i in range (6):
                
                if(testmancalaBoard._getboard()[playerTurn][i] == 0):
                    continue;
                
                m = copy.deepcopy(testmancalaBoard)
                m._setcurrentPlayer(playerTurn)
                

            
                if(not m._move(i)):

                    eval = self._minimax(m, depth - 1, alpha, beta, True, 1 - playerTurn)
                    
                else:

                    eval = self._minimax(m, depth - 1, alpha, beta, False, playerTurn)
                    
                
                minEval = min(minEval, eval)

                beta = min(beta, eval)
                if (beta <= alpha):
                    break
                
                
            return minEval                 
        
    
            
    def _printBoard(self, board1):
        
        board = copy.deepcopy(board1)
        
        sum = 0
        
        
        for i in range(self.noofPlayers):
            print(board[i])
            for j in range(self.noofBins + 1):
                sum += board[i][j]
                if(int(board[i][j]) < 10):
                    board[i][j] = " " + str(board[i][j])
                else: 
                    board[i][j] = str(board[i][j])

        
        print("total number of stones: " + str(sum))
        
        print()
        print("+-----+  f     e     d     c     b     a  +-----+")
        print("+-----+-----------------------------------+-----+")
        print("|     | " +  board[0][5]  + "  | " +  board[0][4]  + "  | " +  board[0][3]  + "  | " +  
              board[0][2]  + "  | " +  board[0][1]  + "  | " +  board[0][0]  + "  |     |")
        
        
        print("| " + board[0][6] + "  |-----|-----|-----|-----|-----|-----| " + board[1][6] + "  |")
        
        
        print("|     | " +  board[1][0]  + "  | " +  board[1][1]  + "  | " +  board[1][2]  + "  | " +  
              board[1][3]  + "  | " +  board[1][4]  + "  | " +  board[1][5]  + "  |     |")
        print("+-----+-----------------------------------+-----+")
        print("+-----+  a     b     c     d     e     f  +-----+")     
        print()  
        
    
            
