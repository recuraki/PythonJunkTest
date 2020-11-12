import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    data = list(map(int, input().split()))
    n = int(input())
    data.sort(reverse=True)
    datb = list(map(int, input().split()))
    datb.sort(reverse=True)
    finalres = 10**9+10
    for basestring in range(6):
        first = datb[0] - data[basestring]
        #print(">>> use string", basestring, first)
        resultlist = []

        res = [first]
        costlist = []
        selected = []
        # onpu-onpu-onpu-onpu-onpu-onpu-onpu-onpu-onpu-onpu-
        minpluses = []
        minminuses = []
        inf = 10**9 + 10
        minf = -inf
        for i in range(1, n):
            #print("onpu", i, datb[i])
            minval =  1000000009
            minplus = inf
            minminus = inf
            cost = None
            for string in range(6):
                diff = datb[i] - data[string]
                #print("string", string, "diff", datb[i], data[string])
                diffabs = abs(first - diff)
                #print("firstdiff", diff)
                if diffabs < minval:
                    minval = diffabs
                    cost = first - diff
                    #print("cost", cost)
                    select = string
                    if cost == 0:
                        minplus = 0
                        minminus = 0
                    elif cost > 0:
                        if minplus > cost:
                            minplus = cost
                    elif cost < 0:
                        if minminus > (-cost):
                            minminus = -cost

            m, p = -1, -1
            if minplus != inf:
                p = minplus
            if minminus != inf:
                m = abs(minminus)
            resultlist.append([m, p])


            costlist.append(cost)
            res.append(minval)
            selected.append(select)

        ##############################################################
        resultlist.sort(key=lambda x: x[0], reverse=True)
        costplus = 0
        costminus = 0
        for m, p in resultlist:
            canplus = inf
            canminus = inf
            if m != -1:
                canminus = m
            if p != -1:
                canplus = p
            if canplus < costplus or canminus < costminus:
                continue
            if abs(costplus-canplus) <= abs(costminus-canminus):
                costplus = canplus
            else:
                costminus = costminus
        #print("cost cal = ", costplus + costminus)
        finalres = min(finalres, costplus + costminus)

        resultlist.sort(key=lambda x: x[1], reverse=True)
        costplus = 0
        costminus = 0
        for m, p in resultlist:
            canplus = inf
            canminus = inf
            if m != -1:
                canminus = m
            if p != -1:
                canplus = p
            if canplus < costplus or canminus < costminus:
                continue
            if abs(costplus - canplus) <= abs(costminus - canminus):
                costplus = canplus
            else:
                costminus = costminus
        #print("cost cal = ", costplus + costminus)
        finalres = min(finalres, costplus + costminus)

        ##############################################################
        resultlist.sort(key=lambda x: x[0], reverse=False)
        costplus = 0
        costminus = 0
        for m, p in resultlist:
            canplus = inf
            canminus = inf
            if m != -1:
                canminus = m
            if p != -1:
                canplus = p
            if canplus < costplus or canminus < costminus:
                continue
            if abs(costplus-canplus) <= abs(costminus-canminus):
                costplus = canplus
            else:
                costminus = costminus
        #print("cost cal = ", costplus + costminus)
        finalres = min(finalres, costplus + costminus)

        resultlist.sort(key=lambda x: x[1], reverse=False)
        costplus = 0
        costminus = 0
        for m, p in resultlist:
            canplus = inf
            canminus = inf
            if m != -1:
                canminus = m
            if p != -1:
                canplus = p
            if canplus < costplus or canminus < costminus:
                continue
            if abs(costplus - canplus) <= abs(costminus - canminus):
                costplus = canplus
            else:
                costminus = costminus
        #print("cost cal = ", costplus + costminus)
        finalres = min(finalres, costplus + costminus)


    print(finalres)




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
        input = """1 4 100 10 30 5
6
101 104 105 110 130 200"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1 2 2 3 3
7
13 4 11 12 11 13 12"""
        output = """7"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()