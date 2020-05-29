import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class segmentTreeSum():
        initValue = 0
        dat = []
        lenTreeList = -1
        depthTreeList = 0
        lenOriginalList = -1

        def __init__(self):
            pass

        def load(self, l):
            self.lenOriginalList = len(l)
            self.lenTreeList = 2 ** (len(l) - 1).bit_length()
            self.depthTreeList = (len(l) - 1).bit_length()
            self.dat = [self.initValue] * (self.lenTreeList * 2)
            for i in range(len(l)):
                self.dat[self.lenTreeList - 1 + i] = l[i]
            self.build()

        def build(self):
            for i in range(self.lenTreeList - 2, -1, -1):
                self.dat[i] = self.dat[2 * i + 1] + self.dat[2 * i + 2]

        def addValue(self, i, a):
            nodeId = (self.lenTreeList - 1) + i
            self.dat[nodeId] += a
            self.setValue(i, self.dat[nodeId])

        def setValue(self, i, a):
            """
            set a to list[i]
            """
            # print("setValue: {0}, {1}".format(i, a))
            nodeId = (self.lenTreeList - 1) + i
            # print(" first nodeId: {0}".format(nodeId))
            self.dat[nodeId] = a
            while nodeId != 0:
                nodeId = (nodeId - 1) // 2
                # print(" next nodeId: {0}".format(nodeId))
                self.dat[nodeId] = self.dat[nodeId * 2 + 1] + self.dat[nodeId * 2 + 2]

        def querySub(self, a, b, nodeId, l, r):
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
            if self.dat[nodeId] < x:
                return (None, x - self.dat[nodeId])
            if nodeId >= self.lenTreeList - 1:
                # print(" hit node: nodeId = {0} , x = {1}, retval = {2}".format(nodeId, x, nodeId - (self.lenTreeList - 1)))
                return (True, nodeId - (self.lenTreeList - 1))
            # print(" call L()")
            resLeft = self.findNthValueSub(x, 2 * nodeId + 1)
            if resLeft[0] != None:
                # print(" call L: hit")
                return (True, resLeft[1])
            # print(" call R()")
            resRight = self.findNthValueSub(resLeft[1], 2 * nodeId + 2)
            return resRight

        def findNthValue(self, x):
            return self.findNthValueSub(x, 0)[1]

    import gc
    l = [0] * (1000100)
    n, q = map(int, input().split())
    dat = list(map(int, input().split()))
    for i in range(n):
        l[dat[i]] += 1
    dat = None
    gc.collect()
    #print(l[:20])
    st = segmentTreeSum()
    st.load(l)
    l = None
    gc.collect()
    st.build()
    #print(st.dat)
    dat = list(map(int, input().split()))
    erasecnt = 0
    for i in range(q):
        c = dat[i]
        if c < 0:
            erasecnt += 1
            num = st.findNthValue(abs(c))
            cnt = st.query(num, num+1)
            #print( " get",num,cnt)
            #print( " set",num,cnt - 1)
            st.setValue(num,cnt - 1)
        else:
            num = st.query(c, c+1)
            #print( " get",c,num)
            num += 1
            #print( " set",c,num)
            st.setValue(c, num)
    #print(st.dat)
    if erasecnt == n:
        print(0)
    else:
        print(st.findNthValue(1))



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """5 5
1 2 3 4 5
-1 -1 -1 -1 -1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 4
1 2 3 4 5
-5 -1 -3 -1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6 2
1 1 1 2 3 4
5 6"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()