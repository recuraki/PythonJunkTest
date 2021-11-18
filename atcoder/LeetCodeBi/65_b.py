from typing import List, Tuple
from pprint import pprint

###################################
class Robot:
    dir  = 1
    name = ["North", "East", "West", "South"]
    maze = []
    pos = []
    isMove = False
    def __init__(self, width: int, height: int):
        self.rob = 0
        self.maze = []
        self.pos = []
        self.isMove = False
        self.maze = ([3] + [1] * (width-1 ) ) + ([0] * (height - 1) ) + ([2] * (width - 1) ) + ([3] * (height - 2) )
        for i in range(width):
            self.pos.append( [i, 0] )
        for i in range(height - 1):
            self.pos.append( [width-1, i+1] )
        for i in range(width-1-1, -1, -1):
            self.pos.append( [i, height - 1] )
        for i in range(height - 1 -1 , 0, -1):
            self.pos.append( [0, i] )
        #print(self.maze)
        #print(self.pos)
        #print(len(self.maze))
        #print(len(self.pos))


    def move(self, num: int) -> None:
        self.rob += num
        self.rob %= len(self.maze)
        self.isMove = True
        #print("move", num, self.getPos(), self.getDir())


    def getPos(self) -> List[int]:
        if self.isMove is False: return [0,0]
        return self.pos[self.rob]

    def getDir(self) -> str:
        if self.isMove is False: return "East"
        return self.name[self.maze[self.rob]]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
###################################
"""
obj = Robot(6, 3)
obj.move(2)
obj.move(2)
print(obj.getPos())
print(obj.getDir())
obj.move(2)
obj.move(1)
obj.move(4)
print(obj.getPos())
print(obj.getDir())
obj.move(1)
print(obj.getPos())
print(obj.getDir())
obj.move(1)
print(obj.getPos())
print(obj.getDir())
obj.move(1)
print(obj.getPos())
print(obj.getDir())
obj.move(1)
print(obj.getPos())
print(obj.getDir())
obj.move(14)
print(obj.getPos())
print(obj.getDir())
"""
#obj = Robot(2,2)
# ["Robot","move","move","getPos","getDir","move","getPos","getDir","getPos","getDir"]
# [[20,13],[12],[21],[],[],[17],[],[],[],[]]
# Exp [null,null,null,[17,12],"West",null,[0,12],"West",[0,12],"West"]
obj = Robot(20,13)
print(obj.getPos())
print(obj.getDir())
obj.move(12)
obj.move(21)
print(obj.getPos())
print(obj.getDir())
obj.move(17)
print(obj.getPos())
print(obj.getDir())
print(obj.getPos())
print(obj.getDir())
