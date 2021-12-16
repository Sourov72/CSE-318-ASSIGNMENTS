
import random
import math

from mancalaBoard import *

class Heurisitic:
    
    
    def _heuristic(self, m, currentplayer, type):
        
        if(type == 1):
            return self._heuristic1(m, currentplayer)
        
        elif(type == 2):
            return self._heuristic2(m, currentplayer)
        
        elif(type == 3):
            return self._heuristic3(m, currentplayer)
        
        elif(type == 4):
            return self._heuristic4(m, currentplayer)
        
        elif(type == 5):
            return self._heuristic5(m, currentplayer)
        
        elif(type == 6):
            return self._heuristic6(m, currentplayer)
        
    
    def _stonesinstorage(self, m, currentplayer):
        
        myside = 0
        opponentside = 0
        
        for i in range (m.storage):
            myside += m._getboard()[currentplayer][i]
            opponentside += m._getboard()[1 - currentplayer][i]
            
        return myside, opponentside
    
    def _closetowinning(self, m, currentplayer):
        
        closetomyside = 0
        closetomyopponentside = 0
        
        for i in range (m.storage):
            
            noofstones = m._getboard()[currentplayer][i]
            if(noofstones <= m.storage - i):
                closetomyside += (noofstones)
            else:
                closetomyside += (m.storage - i)
                noofstones -= (m.storage - i)
                res = math.ceil(noofstones / 6)
                if(not res % 2):
                    closetomyside += ((res / 2) - 1) * 6
                    if(not noofstones % 6):
                        closetomyside += noofstones % 6
                    else:
                        closetomyside += m.storage
                else:
                    closetomyside += (math.ceil(res / 2) - 1) * 6
                        
                        
        for i in range (m.storage):
            
            noofstones = m._getboard()[1 - currentplayer][i]
            if(noofstones <= m.storage - i):
                closetomyopponentside += (noofstones)
            else:
                closetomyopponentside += (m.storage - i)
                noofstones -= (m.storage - i)
                res = math.ceil(noofstones / 6)
                if(not res % 2):
                    closetomyopponentside += ((res / 2) - 1) * 6
                    if(not noofstones % 6):
                        closetomyopponentside += noofstones % 6
                    else:
                        closetomyopponentside += m.storage
                else:
                    closetomyopponentside += (math.ceil(res / 2) - 1) * 6
                    
                    
                    
        return closetomyside, closetomyopponentside



    def _heuristic1(self, m, currentplayer):
        
        return m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage]


    def _heuristic2(self, m, currentplayer):
        
        w1 = 3
        w2 = 2
        
        myside, opponentside = self._stonesinstorage(m, currentplayer)
        
        # return random.randint(1, w1) * m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage] + random.randint(1, w2) * (myside - opponentside)
        return w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside)


    def _heuristic3(self, m, currentplayer):  
        
        w1 = 3
        w2 = 2
        w3 = 5
        
        myside, opponentside = self._stonesinstorage(m, currentplayer)
        
        # if(m._getfreemove(currentplayer) != 0):
        #     f.write(str(m._getfreemove(currentplayer)) + "\n")



        return (w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside) + w3 * (m._getfreemove(currentplayer)))



    def _heuristic4(self, m, currentplayer):
            
        
        w1 = 7
        w2 = 3
        w3 = 11
        
        myside, opponentside = self._stonesinstorage(m, currentplayer)
        
        return (w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside) + w3 * (m._getfreemove(currentplayer) - m._getfreemove(1 - currentplayer))) 





    def _heuristic5(self, m, currentplayer):
        
        w1 = 3
        w2 = 2
        w3 = 7
        
        myside, opponentside = self._stonesinstorage(m, currentplayer)
        
        

        
        # print(w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside) + w3 * (m._getcapturemove(currentplayer) - m._getcapturemove(1 - currentplayer)))
        
        # input()
        
        return w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside) + w3 * (m._getcapturemove(currentplayer) - m._getcapturemove(1 - currentplayer))
    
    

        
      
    def _heuristic7(self, m, currentplayer):
        
        w1 = 3
        w2 = 2
        w3 = 7
        w4 = 5
        w5 = 3
        
        myside, opponentside = self._stonesinstorage(m, currentplayer)
        closemyside, closeopposide = self._closetowinning(m, currentplayer)
        
        # print("current player ", currentplayer)
        # print("free move ", m._getfreemove(currentplayer))
        # currentplayer = m._getcurrentplayer()
        return w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside) + w3 * (m._getfreemove(currentplayer) - m._getfreemove(1 - currentplayer)) + w4 * (m._getcapturemove(currentplayer) - m._getcapturemove(1 - currentplayer)) + w5 * (closemyside - closeopposide)
    
    
    
    def _heuristic6(self, m, currentplayer):
        
        w1 = 3
        w2 = 2
        w3 = 7
        w4 = 5
        
        myside, opponentside = self._stonesinstorage(m, currentplayer)
        
        return w1 * self._heuristic1(m, currentplayer) + w2 * (myside - opponentside) + w3 * (m._getcapturemove(currentplayer)) + w4 * (m._getfreemove(currentplayer))