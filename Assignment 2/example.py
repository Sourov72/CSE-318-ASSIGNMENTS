


import copy


class hell:

    def __init__(self):
       self.free = [1, 2]
       
    def change(self):
        self.free[0] = 5
    

m = hell()



h = copy.deepcopy(m) 
print(m.free)
print(h.free)

m.change()

print(m.free)
print(h.free)




  

    