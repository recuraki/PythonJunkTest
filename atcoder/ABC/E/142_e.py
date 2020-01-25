import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    openkey = []
    openkeyval = []
    keycanopen = []
    keycost = []
    for i in range(n + 1):
        # 何番麺のカギを使うと開けられるか
        openkey.append([])
        openkeyval.append([])
    for i in range(m):
        # そのカギは何を開けられるか
        keycanopen.append(None)
        keycost.append(-99999)

    for i in range(m):
        a, b = map(int, input().split())
        keycanopen[i] = list(map(int, input().split()))
        keycost[i] = a
        for j in range(b):
            openkey[keycanopen[i][j]].append(i)

    for i in range(1, len(openkey)):
        openkeyval[i] = list(map(lambda x: tuple(x, keycost[x]), openkeyval[i] ))

    print(openkey)
    print(openkeyval)

    import copy
    def tryopen (cur, openstatus, cost):
        #print("tryopen cur={0}, openstatus={1}, cost={2}".format(cur, openstatus, cost))
        if cur == n + 1:
            #print("CLEAR!")
            return cost
        elif openstatus[cur] == 1:
            # もう空いているなら次に
            return tryopen(cur + 1, openstatus, cost)
        else:
            nextcost = 10000000000
            #print("cur{0} can open key {1}".format(cur, openkey[cur]))
            costtmp = cost
            for nextkeyindex in openkey[cur]:
                #print("use key {0}".format(nextkeyindex))
                nextopenstatus = copy.deepcopy(openstatus)
                #print("prev{0}".format(nextopenstatus))
                for openbox in keycanopen[nextkeyindex]:
                    # openboxが空けられる箱
                    nextopenstatus[openbox] = 1
                #print("after{0}".format(nextopenstatus))
                # 次のboxを全部開けた
                nextcosttmp = tryopen(cur + 1, nextopenstatus, costtmp + keycost[nextkeyindex])
                nextcost = min(nextcost, nextcosttmp)
            return nextcost

    res = tryopen(1, [0] * (n+1), 0)
    if res == 10000000000:
        print(-1)
    else:
        print(res)




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
        input = """2 3
10 1
1
15 1
2
30 2
1 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """12 1
100000 1
2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 6
67786 3
1 3 4
3497 1
2
44908 3
2 3 4
2156 3
2 3 4
26230 1
2
86918 1
3"""
        output = """69942"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()