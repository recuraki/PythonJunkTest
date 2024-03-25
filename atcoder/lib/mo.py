"""
オフラインなクエリを
"""
import math

class moAlgo(onject):
    leftQuery = []
    rightQuery = []
    order = []
    width = 0
    nl = nr = ptr = 0;

    def __init__(self):
        pass


    def load(self, l):
        self.width = int(math.sqrt(len(l)))



    def build(self):
        # 0,1,2,3,4...n-1
        self.order = [i for i in range(0, len(self.leftQuery))]
        self.order.sort(key=lambda x: (self.leftQuery[x] // self.width, self.rightQuery[x]))


    def insertQuery(self, l, r):
        # insertQuery: l, rをクエリとして追加
        self.leftQuery.append(l)
        self.rightQuery.append(r)

    def runOnce(self):
        # クエリを一個だけ実行する
