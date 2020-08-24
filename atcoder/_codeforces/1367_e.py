import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import collections


    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        print("INPUT", n,k,s)

        c = collections.Counter(s)
        buf = []
        for key in c:
            buf.append( [c[key], key] )
        buf.sort(reverse=True)
        print(buf)
        canChainDict = collections.defaultdict(lambda: 0)

        finalres = 0
        for i in range(len(buf)):
            ind = i + 1
            charNum = buf[i][0]
            #print("char", buf[i][1], charNum)
            for j in range(1, charNum + 1):
                #print(" > add", ind * j)
                canChainDict[ind * j] = max(canChainDict[ind * j], j)
                if k % j == 0:
                    finalres = max(finalres, ind * j)
                    print(" final calc", k , j, ind * j)

        canChain = list(canChainDict.keys())
        canChain.sort(reverse=True)
        print(canChain)
        for i in range(len(canChain)):
            print(canChain[i], k)
            if canChain[i] % k == 0 or k % canChain[i] == 0:
                print(canChain[i])
                break
        print("final")
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
        input = """6
6 3
abcbac
3 6
aaa
7 1000
abczgyo
5 4
ababa
20 10
aaebdbabdbbddaadaadc
20 5
ecbedececacbcbccbdec"""
        output = """6
3
5
4
15
10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()