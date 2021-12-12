
import copy

from math import inf

from mancalaBoard import *

from Heuristic import *
class manacalaPlay:
    
    def __init__(self, currentplayer,depth):
        self.noofBins = 6
        self.noofStones = 4
        self.board=[]
        self.noofPlayers = 2
        self.currentplayer = currentplayer
        self.depth = depth
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
                   
    
    def _play(self):
        
        i = 0
        while(True):
            
            if(self.mainBoard._getcurrentPlayer() == 0):
                bestPos = -1
                alpha = -inf
                beta = inf
                maxEval = -inf
                
                if(self.mainBoard._gameover()):
                    self._printBoard(self.mainBoard._getboard())
                    self.mainBoard._gamewin()
                    break
                
                for i in range(6):
                    if(self.mainBoard._getboard()[self.mainBoard._getcurrentPlayer()][i] == 0):
                        continue
                    m = copy.deepcopy(self.mainBoard)
                    # print("free move, ", m._getfreemove(self.mainBoard._getcurrentPlayer()) + m._getfreemove(1 - self.mainBoard._getcurrentPlayer()))
                    # self._minimax(m, self.depth, -inf, inf, True, self.mainBoard._getcurrentPlayer(), -1)

                    print("in the primary max")
                    
                    if(not m._move(i)):
                        # print("In max player")
                        # print("player no: ", m._getcurrentPlayer(), self.mainBoard._getcurrentPlayer())
                        # print("self free move, ", m.freemove)
                        # input()
                        eval = self._minimax(m, self.depth - 1, alpha, beta, False, self.mainBoard._getoppositePlayer())
                    else:
                        # print("In max player")
                        # print("player no: ", m._getcurrentPlayer(), self.mainBoard._getcurrentPlayer())
                        print("self free move, ", m.freemove)
                        # input()
                        eval = self._minimax(m, self.depth - 1, alpha, beta, True, self.mainBoard._getcurrentPlayer()) 
                       
                     
                    
                    # print("values ", i, "eval :", eval, "maxval: ", maxEval)
                    if(eval > maxEval):
                       
                        bestPos = i
                        maxEval = eval
                        
                    alpha = max(alpha, maxEval)
                    # if (beta <= alpha):
                    #     break                    
                    

            else:
                if(not self.mainBoard._gameover()):
                    bestPos = input("which bin you want to select?: ") 
                    bestPos = ord(bestPos) - 97
                else: 
                    bestPos = -1
            
            
            if(bestPos == -1):
                print("in pos equals minus one: ")
                self._printBoard(self.mainBoard._getboard())
                self.mainBoard._gamewin()
                break
            i += 1
            # if(i == 40):
            #     break  
            if(self.mainBoard._getcurrentPlayer() == 0):
                print("player 2's move: ")
            else:
                print("player 1's move: ")
                
            print("chosen position for next move: ")
            print(chr(bestPos + 97))
            if(not self.mainBoard._move(bestPos)):
                self.mainBoard._setcurrentPlayer(self.mainBoard._getoppositePlayer())
            self._printBoard(self.mainBoard._getboard())
    
    def _minimax(self, testmancalaBoard, depth, alpha, beta, maximizingPlayer, playerTurn):
        
        # here testmancalaBoard is a manacalaBoard object
        
        
        if(testmancalaBoard._gameover() or depth == 0):
            if(playerTurn == 1):
                return self.heuristic._heuristic1(testmancalaBoard, self.mainBoard._getcurrentPlayer())
            else:
                return self.heuristic._heuristic3(testmancalaBoard, self.mainBoard._getcurrentPlayer())
        
        if(maximizingPlayer):
            maxEval = -inf
            for i in range (6):

                if(testmancalaBoard._getboard()[playerTurn][i] == 0):
                    continue;
                
                m = copy.deepcopy(testmancalaBoard)
                m._setcurrentPlayer(playerTurn)
                
                
                if(not m._move(i)):
                    # print("In max player")
                    # print("player no: ", m._getcurrentPlayer(), self.mainBoard._getcurrentPlayer())
                    # print("self free move, ", m.freemove)
                    # input()
                    eval = self._minimax(m, depth - 1, alpha, beta, False, 1 - playerTurn)
                else:
                    # print("In max player")
                    # print("player no: ", m._getcurrentPlayer(), self.mainBoard._getcurrentPlayer())
                    # print("self free move, ", m.freemove)
                    # input()
                    eval = self._minimax(m, depth - 1, alpha, beta, True, playerTurn)
                    
                
                    
                maxEval = max(eval, maxEval)
                
                alpha = max(alpha, maxEval)
                # if (beta <= alpha):
                #     break
                
            return maxEval
                
        else:

            minEval = inf
            for i in range (6):
                
                if(testmancalaBoard._getboard()[playerTurn][i] == 0):
                    continue;
                
                m = copy.deepcopy(testmancalaBoard)
                m._setcurrentPlayer(playerTurn)
                

            
                if(not m._move(i)):
                    # print("In min player")
                    # print("player no: ", m._getcurrentPlayer(), self.mainBoard._getcurrentPlayer())
                    # print("self free move, ", m.freemove)
                    # input()
                    eval = self._minimax(m, depth - 1, alpha, beta, True, 1 - playerTurn)
                else:
                    # print("In min player")
                    # print("player no: ", m._getcurrentPlayer(), self.mainBoard._getcurrentPlayer())
                    # print("self free move, ", m.freemove)
                    # input()
                    eval = self._minimax(m, depth - 1, alpha, beta, False, playerTurn)
                    
                
                minEval = min(minEval, eval)

                beta = min(beta, minEval)
                # if (beta <= alpha):
                #     break
                
                
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
        
        
        
        # for i in range(self.noofPlayers):
            
        #     for j in range(self.noofBins + 1):
                
        #         if(int(board[i][j]) < 10):

        #             board[i][j] = int(board[i][j]) 
            
    
            
