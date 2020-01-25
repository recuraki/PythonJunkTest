
class segmentTreeMin():
    # とりあえず9 * 12桁
    inf = 999999999999
    dat = []
    lenData = -1

    def __init__(self):
        pass

    def load(self, l):
        # len(l)個よりも大きい2の二乗を得る
        self.lenData = 2 ** (len(l)-1).bit_length() # len 5 なら 2^3 = 8
        self.dat = [self.inf] * (self.lenData * 2)
        # 値のロード
        for i in range(len(l)):
            self.dat[self.lenData - 1 + i] = l[i]
        self.build()

    def build(self):
        for i in range(self.lenData - 2, -1, -1):
            self.dat[i] = min(self.dat[2*i + 1], self.dat[2*i + 2])

    def setValue(self, i, a):
        """
        set a to list[i]
        """
        self.dat[self.lenData - 1 + i] = a
        while i != 0:
            i = (i-1) // 2
            self.dat[i] = min(dat[2 * i + 1], dat[2 * i + 2])


l = [3,0,5,6,2,4]
stm = segmentTreeMin()
stm.load(l)
stm.build()
print(stm.dat)


