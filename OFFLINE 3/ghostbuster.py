import copy
from operator import truediv
from unittest.mock import _CallList

mainBoard = []
tempBoard = []


probabilityBoard = []

class prob:
    
    def __init__(self, x, y):
        self.adj = x
        self.cross = y


def _initiate(m, n, k):
        
    legal_cells = (m * n) - k;
    initial_prob = 1 / legal_cells;
    for row in range(m):
        temp = []
        for column in range(n):
            temp.append(initial_prob)
        mainBoard.append(temp)
    
    for row in range(k):
        x, y = [int(x) for x in input().split()]
        mainBoard[x][y] = 0
        
        
def _probCalculate(m, n, adjprob, crossprob):
    
    print(m, n)
    for row in range(m):
        temp = []
        for column in range(n):
            if(tempBoard[row][column] != 0):
                noofoavailadj = 0
                noofavailcross = 0
                transprobadj = 0
                transprocross = 0
                    
                liadj = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                
                for i in range(len(liadj)):
                    
                    if(row + liadj[i][0] >= 0 and row + liadj[i][0] < m and column + liadj[i][1] >= 0 and column + liadj[i][1] < n):
                        if(tempBoard[row + liadj[i][0]][column + liadj[i][1]] != 0):
                            noofoavailadj += 1
                        
                if(noofoavailadj != 0):
                    transprobadj = adjprob / noofoavailadj    
                
                li = [[-1, -1], [1, -1], [-1, 1], [1, 1], [0, 0]]
                
                for i in range(len(li)):
                    
                    if(row + li[i][0] >= 0 and row + li[i][0] < m and column + li[i][1] >= 0 and column + li[i][1] < n):
                        if(tempBoard[row + li[i][0]][column + li[i][1]] != 0):
                            noofavailcross += 1
                        
                if(noofavailcross != 0):
                    transprocross = crossprob / noofavailcross
                p = prob(transprobadj, transprocross)
             
            else: 
                p = prob(0, 0)   
           
            temp.append(p)
        probabilityBoard.append(temp)
        
    
def _adjacencyCheck(u, v, row, column):
    
    liadj = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, -1], [-1, 1], [1, 1], [0, 0]]
    
    for i in range(len(liadj)):
        
        if(liadj[i][0] + row == u and liadj[i][1] + column == v):
            return True        

    return False
    
    
def _foradjacent(m, n, row, column):
    
    summation = 0
        
    liadj = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for i in range(len(liadj)):
        
        if(row + liadj[i][0] >= 0 and row + liadj[i][0] < m and column + liadj[i][1] >= 0 and column + liadj[i][1] < n):
            if(tempBoard[row + liadj[i][0]][column + liadj[i][1]] != 0):
                summation += (tempBoard[row + liadj[i][0]][column + liadj[i][1]] * probabilityBoard[row + liadj[i][0]][column + liadj[i][1]].adj) 
        
    # print(summation)
    return summation



def _forcross(m, n, row, column, evi, presum):
    
    li = [[-1, -1], [1, -1], [-1, 1], [1, 1], [0, 0]]
    summation = presum
    for i in range(len(li)):
        if(row + li[i][0] >= 0 and row + li[i][0] < m and column + li[i][1] >= 0 and column + li[i][1] < n):
            if(tempBoard[row + li[i][0]][column + li[i][1]] != 0):
                summation += (tempBoard[row + li[i][0]][column + li[i][1]] * probabilityBoard[row + li[i][0]][column + li[i][1]].cross) 
            
    
    mainBoard[row][column] = summation * evi


def _maxrowcolumnretrun(m, n):
    
    sum = 0
    row = 0
    column = 0
    for i in range(m):
        for j in range (n):
            if(mainBoard[i][j] > sum):
                sum = mainBoard[i][j]
                row = i
                column = j
    
    return row, column
            



def _printBoard(no, sum):
    
    if(sum == 0):
        temp = 1
    else:
        temp = sum
    
    print("Time ", no)
    print("------------------------")
    
    for i in range(len(mainBoard)):
       
        for j in range(len(mainBoard[0])):
            if(mainBoard[i][j] != 0):
                print(float("{:.4f}".format((mainBoard[i][j] / temp) * 100)), end = " ")
            else:
                print("0.0000", end = " ")
        print()
    print("-------------------------------------------------------\n\n")
    
      


m = 0
n = 0
k = 0
evidance = 0.85
adjacprob = 0.9
crossprob = 0.1


m, n, k = [int(x) for x in input().split()]

_initiate(m, n, k)

tempBoard = copy.deepcopy(mainBoard)

_probCalculate(m, n, adjacprob, crossprob)

time = 0

_printBoard(time, 0)


# for i in range(m):
#     for j in range(n):
#         print(probabilityBoard[i][j].adj, end=" ")
#     print()
    

while(True):
    
    x = [x for x in input("Enter next value: ").split(" ")]
    if(x[0] == 'R'):
        u = int(x[1])
        v = int(x[2])
        b = int(x[3])
        time += 1
        if(b == 1):
            tempev = evidance
        else:
            tempev = 1 - evidance
        for i in range(m):
            for j in range(n):
                if(tempBoard[i][j] != 0):
                    if(_adjacencyCheck(u, v, i, j)):
                        
                        sum = _foradjacent(m, n, i, j)
                        _forcross(m, n, i, j, tempev, sum)
                    else:
                        sum =  _foradjacent(m, n, i, j)
                        _forcross(m, n, i, j, 1 - tempev, sum)
                            
        totalSum = 0
        for i in range(m):
            for j in range(n):
                totalSum += mainBoard[i][j]
            
        _printBoard(time, totalSum)
        tempBoard = copy.deepcopy(mainBoard)  

    elif(x[0] == 'C'):
        
       r, c = _maxrowcolumnretrun(m, n)
       print("most probable cell-----> ", r, c)
        
    else:
        break
        
    




