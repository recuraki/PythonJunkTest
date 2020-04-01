# 区間和
class segmentTreeSum():
    initValue = 0
    dat = []
    lenTreeList = -1
    depthTreeList = 0
    lenOriginalList = -1

    def __init__(self):
        pass

    def load(self, l):
        # len(l)個よりも大きい2の二乗を得る
        self.lenOriginalList = len(l)
        self.lenTreeList = 2 ** (len(l) - 1).bit_length()  # len 5 なら 2^3 = 8
        self.depthTreeList = (len(l) - 1).bit_length() # 木の段数(0 origin)
        self.dat = [self.initValue] * (self.lenTreeList * 2)
        # 値のロード
        for i in range(len(l)):
            self.dat[self.lenTreeList - 1 + i] = l[i]
        self.build()

    def build(self):
        for i in range(self.lenTreeList - 2, -1, -1):
            self.dat[i] = self.dat[2 * i + 1] + self.dat[2 * i + 2]

    # 若干無駄なインストラクションあるのでコードレベルでマージしたほうがいいかも
    def addValue(self, i, a):
        nodeId = (self.lenTreeList - 1) + i
        self.dat[nodeId] += a
        self.setValue(i, self.dat[nodeId])

    def setValue(self, i, a):
        """
        set a to list[i]
        """
        #print("setValue: {0}, {1}".format(i, a))
        nodeId = (self.lenTreeList - 1) + i
        #print(" first nodeId: {0}".format(nodeId))
        self.dat[nodeId] = a
        while nodeId != 0:
            nodeId = (nodeId - 1) // 2
            #print(" next nodeId: {0}".format(nodeId))
            self.dat[nodeId] = self.dat[nodeId * 2 + 1] + self.dat[nodeId * 2 + 2]

    def querySub(self, a, b, nodeId, l, r):
        """
        [a,b) 区間の親クエリに対するノードnodeへ[l, r)の探索をデリゲート
        区間については、dataの添え字は0,1,2,3,4としたときに、
        [0,3)なら0,1,2の結果を返す
        """
        # print("querySub: a={0}, b={1}, nodeId={2}, l={3}, r={4}".format(a, b, nodeId, l, r))
        if (r <= a or b <= l):
            return self.initValue
        if a <= l and r <= b:
            return self.dat[nodeId]
        resLeft = self.querySub(a, b, 2 * nodeId + 1, l, (l + r) // 2)
        resRight = self.querySub(a, b, 2 * nodeId + 2, (l + r) // 2, r)
        return resLeft + resRight

    def query(self, a, b):
        return self.querySub(a, b, 0, 0, self.lenTreeList)

    def findNthValueSub(self, x, nodeId):
        """
        [2, 3, 5, 7] = [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
        とマッピングされているセグメント木においてx番目に小さい値を得るための関数
        """
        #print("call findNthValueSub x={0}, nodeId={1} nodeval={2}".format(x, nodeId, self.dat[nodeId]))
        # ここから先は葉ではないノードへの処理
        if self.dat[nodeId] < x: # このノードが要求されているよりも小さい値しか持たないとき
            return (None, x - self.dat[nodeId])
        if nodeId >= self.lenTreeList - 1: # nodeIfがノードのときは
            #print(" hit node: nodeId = {0} , x = {1}, retval = {2}".format(nodeId, x, nodeId - (self.lenTreeList - 1)))
            return (True, nodeId - (self.lenTreeList - 1)) # そのindex番号を返す
        #print(" call L()")
        resLeft = self.findNthValueSub(x, 2 * nodeId + 1) # 左側の探索を行う
        if resLeft[0] != None: # もし、値が入っているならそれを返す
            #print(" call L: hit")
            return (True, resLeft[1])
        #print(" call R()")
        resRight = self.findNthValueSub(resLeft[1], 2 * nodeId + 2) #右側の探索を行う
        return resRight

    def findNthValue(self, x):
        return self.findNthValueSub(x, 0)[1]

def test1():
    l = [1, 0, 2, 3, 4, 0]
    st = segmentTreeSum()
    st.load(l)
    st.build()
    print(st.dat)
    for i in range(1, len(l)+1):
        print(" query[0, {0}) = {1}".format(i, st.query(0, i)))

def test2():
    # 単なる2分探索
    def segmentTreeBisectLeft(segTreeTarget: segmentTreeSum, x):
        lo, hi = 0, st.lenOriginalList
        while lo < hi:
            mid = (lo+hi)//2
            if segTreeTarget.query(0, mid + 1) < x: lo = mid + 1 # ここでRSQ[0,mid)のクエリ
            else: hi = mid
        return lo

    inData = [2, 3, 5, 7, 15,11, 9, 200000]# 入力データ
    l = [0] * (max(inData) + 1)
    for i in range(len(inData)):
        l[inData[i]] = 1
    #print(l) # 入力をセグメントツリーの入力形式に変換
    st = segmentTreeSum()
    st.load(l)
    st.build()
    start = time.time()
    for i in range(1, len(inData) + 1):
        print(" {0} th value = {1}".format(i, segmentTreeBisectLeft(st, i) ))
    print("elapsed_time:{0}".format(time.time() - start) + "[sec]")

def test3():
    inData = [2, 3, 5, 7, 15,11, 9, 200000]# 入力データ
    l = [0] * (max(inData) + 1)
    for i in range(len(inData)):
        l[inData[i]] = 1
    #print(l) # 入力をセグメントツリーの入力形式に変換
    st = segmentTreeSum()
    st.load(l)
    st.build()
    start = time.time()
    for i in range(1, len(inData) + 1):
        print(" {0} th value = {1}".format(i, st.findNthValue(i) ))
    print("elapsed_time:{0}".format(time.time() - start) + "[sec]")
    #
    st.setValue(2,0)
    st.setValue(18,1)
    start = time.time()
    for i in range(1, len(inData) + 1):
        print(" {0} th value = {1}".format(i, st.findNthValue(i) ))
    print("elapsed_time:{0}".format(time.time() - start) + "[sec]")


import time

# 単純なsumの試験
#test1()
# k番目に小さい数値を得る O(log^2 N)
test2()
# k番目に小さい数値を得る O(log N)
test3()

l = [1, 0, 2, 3, 4, 0]
st = segmentTreeSum()
st.load(l)
st.build()
print(st.dat)
print(st.query(0,1))