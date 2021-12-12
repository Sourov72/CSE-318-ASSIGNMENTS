
import random

from mancalaBoard import *

class Heurisitic:
    
    


    def _heuristic1(self, m, currentplayer):
        
        return m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage]


    def _heuristic2(self, m, currentplayer):
        
        w1 = 3
        w2 = 5
        
        myside = 0
        opponentside = 0
        
        for i in range (m.storage):
            myside += m._getboard()[currentplayer][i]
            opponentside += m._getboard()[1 - currentplayer][i]
        
        # return random.randint(1, w1) * m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage] + random.randint(1, w2) * (myside - opponentside)
        return w1 * m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage] + w2 * (myside - opponentside)


    def _heuristic3(self, m, currentplayer):
        
        w1 = 4
        w2 = 0
        w3 = 8
        
        myside = 0
        opponentside = 0
        
        for i in range (m.storage):
            myside += m._getboard()[currentplayer][i]
            opponentside += m._getboard()[1 - currentplayer][i]
        
        # print("w1 " , ((m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage])))
        # print("w2 " , (myside - opponentside))
        # print("current player ", currentplayer, "opposite player ", 1 - currentplayer)
        # print("w3 " , (m._getfreemove(currentplayer) + m._getfreemove(1 - currentplayer)))
        # input()
        
        
        return (w1 * (m._getboard()[currentplayer][m.storage] - m._getboard()[1 - currentplayer][m.storage]) + w2 * (myside - opponentside) + w3 * (m._getfreemove(currentplayer) + m._getfreemove(1 - currentplayer)))



        