class sparseTable(object):
    func = None
    depthTreeList: int = 0
    table = []

    def __init__(self):
        self.table = []
        self.depthTreeList = 0

    def load(self, l):
        self.n = len(l)
        self.depthTreeList = (self.n - 1).bit_length() # Level
        self.table.append(l)
        print(l)
        for curLevel in range(1, self.depthTreeList):
            l = []
            for i in range( self.n - (2**curLevel -1) ):
                l.append(self.func(self.table[curLevel - 1][i], self.table[curLevel - 1][i + (2**(curLevel - 1)) ] ))
            self.table.append(l)
            print(l)

    def query(self, l, r): # [l, r)
        diff = r - l
        if diff <= 0:
            raise
        if diff == 1:
            return self.table[0][l]
        level = (diff - 1).bit_length() - 1
        return self.func(self.table[level][l], self.table[level][r - (2 ** level)])


class sparseTableMax(sparseTable):
    func = max


class sparseTableMin(sparseTable):
    func = min


import fractions


class sparseTableGcd(sparseTable):
    func = lambda self, x, y: fractions.gcd(x,y)


class sparseTableLcm(sparseTable):
    func = lambda self, x,y: (x * y) // fractions.gcd(x, y)

l = [3, 1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6]
st = sparseTableMax()
st = sparseTableLcm()
st = sparseTableGcd()
st = sparseTableMin()
st.load(l)
print(st.query(0,1))
print(st.query(0,2))
print(st.query(0,len(l)))
print(st.query(2,3))
print(st.query(2,4))
print(st.query(4,7))
