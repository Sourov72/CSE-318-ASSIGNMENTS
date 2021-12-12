
class mancalaBoard:
    
    def __init__(self, currentplayer, board):
        self.noofBins = 6
        self.noofStones = 4
        self.board=board
        self.noofPlayers = 2
        self.storage = 6
        self.currentplayer = currentplayer
        self.freemove = [0, 0]
        self.capturemove = [0, 0]

        # storage is the number of the bin where bins are stored for a player
        # 0, 6 is for the player 2
        # 1, 6 is for the player 1
        
        
        
    # def _initiate(self):
        
    #     for i in range(self.noofPlayers):
    #         temp = []
    #         for j in range(self.noofBins):
    #             temp.append(int(self.noofStones))
    #         temp.append(0)
    #         self.board.append(temp)
            
            
    def _getoppositePlayer(self):
        
        return 1 - self._getcurrentPlayer()
    
    def _setcurrentPlayer(self, currentplayer):
        
        self.currentplayer = currentplayer
        
    def _getcurrentPlayer(self):
        
        return self.currentplayer
            
    def _getboard(self):
        return self.board
    
    def _gameover(self):
        
        
        # print("IN actual game over")
        # print()
        
        # self._printBoard()
        
        sum = 0
        
        for i in range(self.noofBins):
            if(self.board[self._getoppositePlayer()][i] > 0):
                return False
            sum += self.board[self._getcurrentPlayer()][i]
         
         
        for i in range(6):
            self.board[0][i] = 0
            self.board[1][i] = 0
             
        self.board[self._getcurrentPlayer()][self.storage] += sum
        return True
    
    def _gamewin(self):
        
        if(self.board[0][self.storage] > self.board[1][self.storage]):
            print("Player 2 wins!!")
        elif(self.board[0][self.storage] == self.board[1][self.storage]):
            print("Game Tied!!")
        else:
            print("Player 1 wins!!")
    
    def _capture(self, binno):
        
        # opposite player all the bins in the speicified bin no and plus one for my last stone in the empty bin 
        # print("captured bin no is: " + str(binno))
        

        if(self.board[self._getoppositePlayer()][self.noofBins - 1 - binno] != 0):
            self.board[self._getcurrentPlayer()][self.storage] += self.board[self._getoppositePlayer()][self.noofBins - 1 - binno] + 1
            self.board[self._getoppositePlayer()][self.noofBins - 1 - binno] = 0
            return True
        else:
            return False
        
    def _getfreemove(self, player):
        return self.freemove[player]    
    
    def _getcapturemove(self, player):
        return self.capturemove[player] 

    def _move(self, selectedBin):
        
        bla = selectedBin
        # self._printBoard()
        currentplayer = self._getcurrentPlayer()
        # print(selectedBin)
        noofstonesSelected = self.board[self._getcurrentPlayer()][selectedBin]
        self.board[self._getcurrentPlayer()][selectedBin] = 0
        #how many are in the selected bin
        
        rotate = 0
        s = noofstonesSelected
        while(s > 0):
            
            
            selectedBin += 1
            
            if(selectedBin > self.storage): 
                currentplayer = 1 - currentplayer
                selectedBin = 0

            if(currentplayer == self._getcurrentPlayer()):
                
                
                if(s == 1 and selectedBin == self.storage):
                    # condition for free turn
                    self.board[currentplayer][selectedBin] += 1
                    self.freemove[self._getcurrentPlayer()] += 1
                    return True
                    
                
                elif(s == 1 and self.board[currentplayer][selectedBin] == 0):
                    
                    # print("player turn "+ str(currentplayer))
                    # print("primary selected value for capturing: " + str(bla))
                    
                    # condition for capturing
                    if(self._capture(selectedBin)):
                        self.board[currentplayer][selectedBin] = -1
                        self.capturemove[self._getcurrentPlayer()] += 1
                
            if(currentplayer != self._getcurrentPlayer() and selectedBin == self.storage):
                pass
            else:    
                self.board[currentplayer][selectedBin] += 1
                s -= 1
          
        return False      
            
    # def _play(self, playerTurn):
        
        
    #     # code for two player play
        
        
    #     while(not self._gameover()):
            
    #         if(playerTurn == 1):
    #             print("player 1's turn: ")
                
    #         else:
    #             print("player 2's turn: ")
                
    #         self._setcurrentPlayer(playerTurn)   
    #         self._printBoard()
    #         selectedBin = input("which bin you want to select?: ") 
    #         selectedBin = ord(selectedBin) - 97
    #         if(self.board[self._getcurrentPlayer()][selectedBin]) == 0:
    #             continue
    #         currentplayer = playerTurn
    #         noofstonesSelected = self.board[self._getcurrentPlayer()][selectedBin]
    #         self.board[self._getcurrentPlayer()][selectedBin] = 0
    #         #how many are in the selected bin
            
            
    #         for s in range(noofstonesSelected, 0, -1):
                
                
    #             selectedBin += 1
                
    #             if(selectedBin > self.storage):    
    #                 currentplayer = 1 - currentplayer
    #                 selectedBin = 0

    #             if(currentplayer == self._getcurrentPlayer()):
                    
                    
    #                 if(s == 1 and selectedBin == self.storage):
    #                     # condition for free turn
    #                     self.board[currentplayer][selectedBin] += 1
    #                     playerTurn = 1 - playerTurn
    #                     continue
                    
    #                 elif(s == 1 and self.board[currentplayer][selectedBin] == 0):
                        
    #                     # condition for capturing
    #                     if(self._capture(selectedBin)):
    #                         self.board[currentplayer][selectedBin] = -1
                    
    #             if(currentplayer != self._getcurrentPlayer() and selectedBin == self.storage):
    #                 s += 1
    #             else:    
    #                 self.board[currentplayer][selectedBin] += 1
                    
    #         playerTurn = 1 - playerTurn
            
    def _printBoard(self):
        
        for i in range(self.noofPlayers):
            print(self.board[i])
            for j in range(self.noofBins + 1):

                if(int(self.board[i][j]) < 10):

                    self.board[i][j] = " " + str(self.board[i][j])
                else:
                    self.board[i][j] = str(self.board[i][j])

        
        print()
        print("+-----+  f     e     d     c     b     a  +-----+")
        print("+-----+-----------------------------------+-----+")
        print("|     | " +  self.board[0][5]  + "  | " +  self.board[0][4]  + "  | " +  self.board[0][3]  + "  | " +  
              self.board[0][2]  + "  | " +  self.board[0][1]  + "  | " +  self.board[0][0]  + "  |     |")
        
        
        print("| " + self.board[0][6] + "  |-----|-----|-----|-----|-----|-----| " + self.board[1][6] + "  |")
        
        
        print("|     | " +  self.board[1][0]  + "  | " +  self.board[1][1]  + "  | " +  self.board[1][2]  + "  | " +  
              self.board[1][3]  + "  | " +  self.board[1][4]  + "  | " +  self.board[1][5]  + "  |     |")
        print("+-----+-----------------------------------+-----+")
        print("+-----+  a     b     c     d     e     f  +-----+")     
        print()  
        
        
        
        for i in range(self.noofPlayers):
            
            for j in range(self.noofBins + 1):
                
                    self.board[i][j] = int(self.board[i][j]) 
            
    