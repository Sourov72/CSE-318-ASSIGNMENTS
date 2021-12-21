


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
        self.move = move
        self.gameType = gametype
        self._initiate()
        self.heuristic = Heurisitic()
        self.mainBoard = mancalaBoard(self.currentplayer, self.board)
        
        
    def _initiate(self):
        
        for i in range(self.noofPlayers):
            temp = []
            for j in range(self.noofBins):
                temp.append(int(self.noofStones))
            temp.append(0)
            self.board.append(temp)
            
            
            
    def _moveOrdering(self, mboard, player):
        
        childList = []
        
        tiebreak = 0
        
        for i in range(6):
            
            temp=[]
            
            
            
            
            if(mboard._getboard()[player][i] == 0):
                continue
            m = copy.deepcopy(mboard)
            m._setcurrentPlayer(player)
            tf = m._move(i)
            if(self.mainBoard._getcurrentPlayer() == 1):
                res = self.heuristic._heuristic(m, self.mainBoard._getcurrentPlayer(), self.type1)

            else:
                res = self.heuristic._heuristic(m, self.mainBoard._getcurrentPlayer(), self.type2)
                
            temp.append(res)
            temp.append(tiebreak)
            temp.append(m)
            temp.append(tf)
            temp.append(i)
            childList.append(temp)
            tiebreak += 1
            
        return childList
                
                
        
    
    def _play(self):
        
        i = 0

        while(True):
            
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
                    while(True):
                        bestPos = random.randint(0, 5)
                        if(self.mainBoard._getboard()[self.mainBoard._getcurrentPlayer()][bestPos] != 0):
                            break
                        
                        
                else:
                    
                    childList = self._moveOrdering(self.mainBoard, self.mainBoard._getcurrentPlayer())
                
                    if(self.move):
                        childList.sort(reverse = True)    
                    
                    for i in childList:

                        m = i[2]
                        mval = i[3]

                        if(not mval):

                            eval = self._minimax(m, depth - 1, alpha, beta, False, self.mainBoard._getoppositePlayer())
                            
                        else:

                            eval = self._minimax(m, depth - 1, alpha, beta, True, self.mainBoard._getcurrentPlayer()) 
                            
                            
                        if(eval > maxEval):
                            
                            bestPos = i[4]
                            maxEval = eval
                            
                            
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
                
                

                
            print(chr(bestPos + 97))
            if(not self.mainBoard._move(bestPos)): 
                self.mainBoard._setcurrentPlayer(self.mainBoard._getoppositePlayer())
                
            self.mainBoard._reset()
            self._printBoard(self.mainBoard._getboard())
            
            
            
            
    
    def _minimax(self, testmancalaBoard, depth, alpha, beta, maximizingPlayer, playerTurn):
        
        # here testmancalaBoard is a manacalaBoard object
        
        if(testmancalaBoard._gameover(self.mainBoard._getcurrentPlayer()) or testmancalaBoard._gameover(self.mainBoard._getoppositePlayer()) or depth == 0):
    
            
            if(self.mainBoard._getcurrentPlayer() == 1):
                return self.heuristic._heuristic(testmancalaBoard, self.mainBoard._getcurrentPlayer(), self.type1)

            else:
                return self.heuristic._heuristic(testmancalaBoard, self.mainBoard._getcurrentPlayer(), self.type2)
        
        if(maximizingPlayer):
            maxEval = -inf
            
            
            childList = self._moveOrdering(testmancalaBoard, playerTurn)
            

            if(self.move):
                childList.sort(reverse = True)
            
            for i in childList:
                
                m = i[2]
                mval = i[3]

                if(not mval):

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
            
            childList = self._moveOrdering(testmancalaBoard, playerTurn)
            
            if(self.move):
                childList.sort()

            for i in  childList: 
                
                m = i[2]
                mval = i[3]

                if(not mval):

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
            # print(board[i])
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
        
    
            
