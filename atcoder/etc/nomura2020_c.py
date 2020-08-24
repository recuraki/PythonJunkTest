import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    print(dat)
    dat.reverse()
    print(dat)
    isCan = True
    depth = n
    lastLeaf = 0
    lastParent = 0
    res = 0
    import math
    buf = [None] * (n + 10)

    for i in range(n + 1):
        maxNode = 2 ** (depth)
        print("i", i, "depth", depth, "lastLeaf", lastLeaf, "lastParent", lastParent, "maxNode", maxNode, "res", res)

        needLeaf = dat[i]
        needParent = maxNode - needLeaf

        if needParent * 2 < (lastLeaf + math.ceil(lastParent/2)):
            isCan = False
            break

        print( ">> needLeaf{0}, needParent{1}".format(needLeaf, needParent))
        if (lastLeaf + lastParent) == needParent:
            pass
        elif (lastParent + lastLeaf) > (needParent * 2): # 子供のparentを圧縮
            print(" >> assyuku", (lastParent + lastLeaf) - (needParent*2))
            print(">>")
            res -= (lastParent + lastLeaf) - (needParent*2)
        elif (lastLeaf + lastParent) < needParent:
            needParent = (lastLeaf + lastParent)

        print( ">> Write needLeaf{0}, needParent{1}".format(needLeaf, needParent))

        res += needLeaf + needParent
        lastLeaf = needLeaf
        lastParent = needParent

        depth -= 1

    if isCan is False:
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
        input = """3
0 1 1 2"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
0 0 1 0 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
0 3 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """1
1 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """10
0 0 1 1 2 3 5 8 13 21 34"""
        output = """264"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()