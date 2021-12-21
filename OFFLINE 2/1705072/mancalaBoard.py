



class mancalaBoard:
    
    def __init__(self, currentplayer, board):
        self.noofBins = 6
        self.noofStones = 4
        self.board=board
        self.noofPlayers = 2
        self.storage = 6
        self.currentplayer = currentplayer
        self.step = 0
        self.freemove = [0, 0]
        self.capturemove = [0, 0]
        
            
            
    def _getoppositePlayer(self):
        
        return 1 - self._getcurrentPlayer()
    
    def _setcurrentPlayer(self, currentplayer):
        
        self.currentplayer = currentplayer
        
    def _getcurrentPlayer(self):
        
        return self.currentplayer
            
    def _getboard(self):
        return self.board
    
    def _gameover(self, player):
        
  
        sum = 0
        
        for i in range(self.noofBins):
            if(self.board[player][i] > 0):
                return False
            sum += self.board[1 - player][i]
         
         
        for i in range(6):
            self.board[0][i] = 0
            self.board[1][i] = 0
             
        self.board[1 - player][self.storage] += sum
        return True
    
    def _gamewin(self):
        
        print("no of steps ", self.step)
        
        
        if(self.board[0][self.storage] > self.board[1][self.storage]):
            print("Player 2 wins!!")
            return 2, self.step
        elif(self.board[0][self.storage] == self.board[1][self.storage]):
            print("Game Tied!!")
            return 0, self.step
        else:
            print("Player 1 wins!!")
            return 1, self.step
    
    def _capture(self, binno):
        
        # opposite player all the bins in the speicified bin no and plus one for my last stone in the empty bin 
        # print("captured bin no is: " + str(binno))
        
        capture = None

        if(self.board[self._getoppositePlayer()][self.noofBins - 1 - binno] != 0):
            capture = self.board[self._getoppositePlayer()][self.noofBins - 1 - binno] + 1
            self.board[self._getcurrentPlayer()][self.storage] += capture
            self.board[self._getoppositePlayer()][self.noofBins - 1 - binno] = 0
            return True, capture
        else:
            return False, capture
        
    def _getfreemove(self, player):

        return self.freemove[player]    
    
    def _getcapturemove(self, player):
        
        return self.capturemove[player] 
    
    
    
    
    def _reset(self):
        self.freemove[0] = 0
        self.freemove[1] = 0
        
        self.capturemove[0] = 0
        self.capturemove[1] = 0

    def _move(self, selectedBin):
        self.step += 1
        currentplayer = self._getcurrentPlayer()
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
                    
                    # condition for capturing
                    check, value = self._capture(selectedBin)
                    if(check):
                        self.board[currentplayer][selectedBin] = -1
                        self.capturemove[self._getcurrentPlayer()] += value
                
            if(currentplayer != self._getcurrentPlayer() and selectedBin == self.storage):
                pass
            else:    
                self.board[currentplayer][selectedBin] += 1
                s -= 1
          
        return False      
        
            
    