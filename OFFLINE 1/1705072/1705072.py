
#!/usr/bin/env python3


from queue import PriorityQueue
import math


class node:
    def __init__(self, parent, pattern, gDist):

        #parent is a node, pattern is graph
        self.parent = parent
        self.gDist = gDist
        self.pattern = pattern
        self.blank = []
        
    def _findBlankSpace(self):
        # print("find blank distance")
        for i in range(k):
            for j in range(k):
                if self.pattern[i][j] == '*':
                    self.blank.append(i)
                    self.blank.append(j)
                    break
    
    
    def _copyitems(self):
        temp = []
        for i in self.pattern:
            tempc = []
            for j in i:
                tempc.append(j)
            temp.append(tempc)
        return temp
        

    def _moveLeft(self):
        # print("move left")
        
        if self.blank[1] == 0:
            return None
        else:
            left = self._copyitems()
            temp = left[self.blank[0]][self.blank[1] - 1]
            left[self.blank[0]][self.blank[1] - 1] = '*'
            left[self.blank[0]][self.blank[1]] = temp
            return node(self, left, self.gDist + 1)
        
    def _moveRight(self):
        # print("move Right")
        
        if self.blank[1] == (k - 1):
            return None
        
        else:
            right = self._copyitems()
            temp = right[self.blank[0]][self.blank[1] + 1]
            right[self.blank[0]][self.blank[1] + 1] = '*'
            right[self.blank[0]][self.blank[1]] = temp
            return node(self, right, self.gDist + 1)
        
    def _moveUp(self):
        # print("move Up")
        
        if self.blank[0] == 0:
            return None
        
        else:
            up = self._copyitems()
            temp = up[self.blank[0] - 1][self.blank[1]]
            up[self.blank[0] - 1][self.blank[1]] = '*'
            up[self.blank[0]][self.blank[1]] = temp
            return node(self, up, self.gDist + 1)
        
    def _moveDown(self):
        # print("move down")
        
                
        if self.blank[0] == (k - 1):
            return None
        
        else:
           
            down=self._copyitems()
            # down.append(self.pattern))
            temp = down[self.blank[0] + 1][self.blank[1]]
            down[self.blank[0] + 1][self.blank[1]] = '*'
            down[self.blank[0]][self.blank[1]] = temp
            return node(self, down, self.gDist + 1)
        
        
    def _addChildren(self):
        # print("add children")
        children = []
        children.append(self._moveUp())
        children.append(self._moveDown())
        children.append(self._moveLeft())
        children.append(self._moveRight())
        
        # print("children: ")
        # for i in self.children:
        #     if i is not None:
        #         print(i.pattern)
        
        # print("end children")
        return children
        



class playGame:
    
    def __init__(self, initial, goal):
        #initial and goal is graph
        self.initial = initial
        self.goal = goal
        self.open = PriorityQueue()
        self.close = []
        self.solvedNode = None
        
        
    def _noofInversion(self):
        
        row = 0
        col = 0
        noofinversion = 0
        for t in range(k * k):
           
            row = int(t / k)
            col = t % k
            c = col + 1
            temp = self.initial[row][col]

            if temp != "*":
                for i in range(row, k):
                    for j in range(c, k):
                        if self.initial[i][j] != "*" and temp > self.initial[i][j]:
                            noofinversion += 1
                    
                    c = 0
                    row += 1
                    
        

        return noofinversion
    
    
    def _noofrowLinearConflicts(self, state):
        # print("in no of row conflict function")
        noofConflicts = 0

        
        for i in range (k):
            for j in range(k - 1):
                if(state[i][j] != "*"):
                    temp = int(state[i][j])
                    row = math.ceil(temp / k) - 1
                    if(row == i):
                        for testcol in range(j + 1, k):
                            if (state[i][testcol] != "*"):
                                if (int(state[i][testcol]) < temp) and math.ceil(int(state[i][testcol]) / k) - 1 == i:
                                    noofConflicts += 1;
                            
        
        # print("no of row conflicts: " + str(noofConflicts))
        return noofConflicts
        
        
        
    def _noofcolLinearConflicts(self, state):
        # print("in no of column conflict function")
        noofConflicts = 0

    
        for j in range (k):
            for i in range(k - 1):
                if(state[i][j] != "*"):
                    temp = int(state[i][j])
                    col = int(temp) % k
                    if(col == 0):
                        col = k
                    col -= 1
                    if(col == j):
                        for testrow in range(i + 1, k):
                            if (state[testrow][j] != "*"):
                                tc = (math.ceil(int(state[testrow][j]) % k))
                                if(tc == 0):
                                    tc = k
                                tc -= 1
                                if (int(state[testrow][j]) < temp) and (math.ceil(int(state[testrow][j]) % k) - 1 == j):
                                    noofConflicts += 1;
                            
        
        # print("no of column conflicts: " + str(noofConflicts))
                        
                    
    
    def _isSolveable(self):
        
        inversion = self._noofInversion()
        # print("no of inversion: ")
        # print(inversion)
        
        if(k % 2) == 0:
            # print("k is even")
            if inversion % 2 == 0 and self.start_node.blank[0] % 2 == 1:
                return True
            elif inversion % 2 == 1 and self.start_node.blank[0] % 2 == 0:
                return True
            
            return False
            
            
        else:
            # print("k is odd")

            if inversion % 2 == 0:
                return True
            else:
                return False        
       
        
        
    def _calcHdistance(self, state):
        #goal is goal graph
        # print("calc hamming dist")
        hamingDist = 0
        for i in range(k):
            for j in range(k):
                if(self.goal[i][j] != state[i][j]) and state[i][j] != "*":
                    hamingDist += 1
        # print(hamingDist)
        return hamingDist
        
        
    def _calcMdistance(self, state):
        # print("calc manhattan distance")
        
        manhattanDist = 0
        for i in range(k):
            for j in range(k):
                if(self.goal[i][j] != state[i][j]) and state[i][j] != "*":
                    row = math.ceil(int(state[i][j]) / k)
                    col = int(state[i][j]) % k
                    if(col == 0):
                        col = k
                    x = abs((i + 1) - row) + abs((j + 1) - col)
                    manhattanDist += x
        
        #print(manhattanDist)
        return manhattanDist
    
        
    def print_path(self,solved_node):
    
        if(solved_node.parent is not None):
            self.print_path(solved_node.parent)
        for i in solved_node.pattern :
            print(i)  
        print("     |     ")
        print("     |     ")
        print("    \|/     ")
        print("     '     ")    
        
    
    def _solve(self, type):
        
        
        self.open.queue.clear()
        self.close.clear()

        distype = 0
        
        self.open.put((0, 0, self.start_node))
        bug = 0
        while(True):
            currenttestNode = self.open.get()[2]
            currenttestNode._findBlankSpace()
            #self._calcMdistance(currenttestNode.pattern)
            self.close.append(currenttestNode.pattern)
            if currenttestNode.pattern == self.goal:
                # print("found the goal state")
                self.solvedNode = currenttestNode
                break
            else:
                children = currenttestNode._addChildren()

                for i in children:
                    if i is not None and i.pattern not in self.close:
                        bug -= 1
                        if(type == 0):
                            distype = self._calcHdistance(i.pattern)
                        elif(type == 1):
                            distype = self._calcMdistance(i.pattern)
                        elif(type == 2):
                            distype = self._calcMdistance(i.pattern) + 2 * self._noofrowLinearConflicts(i.pattern)
                        self.open.put((distype + currenttestNode.gDist + 1, bug, i))
       
        
        if(type == 0):
            print("using Hamming Distance Heuristic:   ")
            print("No of expanded nodes: " + str(len(self.close)))
            print("No of explored nodes: " + str((self.open.qsize() + len(self.close))))
            print("optimal cost to reach the goal state" + ": " + str(self.solvedNode.gDist))
            self.print_path(self.solvedNode)
        elif(type == 1):
            print("using Manhattan Distance Heuristic:   ")
            print("No of expanded nodes: " + str(len(self.close)))
            print("No of explored nodes: " + str((self.open.qsize() + len(self.close))))
            print("optimal cost to reach the goal state" + ": " + str(self.solvedNode.gDist))
            self.print_path(self.solvedNode)
        elif(type == 2):
            print("using Linear Conflict Heuristic:   ")
            print("No of expanded nodes: " + str(len(self.close)))
            print("No of explored nodes: " + str((self.open.qsize() + len(self.close))))
            print("optimal cost to reach the goal state" + ": " + str(self.solvedNode.gDist))
            self.print_path(self.solvedNode)
            
    
    
    
        
    def _play(self):
        # print("let's play")
        
        self.start_node = node(None, self.initial, 0)
        self.start_node._findBlankSpace()
        
        if self._isSolveable():
            
            print("the puzzle is solvable")
            
            self._solve(0)
            self._solve(1)
            self._solve(2)
  
        else:
            
            print("the puzzle is not solvable")
            
        
        
                

            
        
        
def take_input():

    init_list = [] 
    goal_list = []       
    for i in range(k):
        temp = input().split(" ")
        init_list.append(temp)
    for i in range(k):
        temp = []
        for j in range(k):
            temp.append(str(k * i + (j + 1)))
        goal_list.append(temp)
    goal_list[k - 1][k - 1] = '*'
    
    return init_list, goal_list
                

print("no of test cases: ")
t = input()
t = int(t)

for i in range(t):
    
    
    k = input("grid size: ")

    k = int(k)
    
    goal_list = []
    initial_list = []
    
    
    initial_list, goal_list = take_input()
    p = playGame(initial_list, goal_list)
    p._play()
    
    
   




            