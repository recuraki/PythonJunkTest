import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        #print(dat)
        initval = 0
        end = False
        for iii in range(n):
            if end:
                break
            if iii == n-1:
                print(n-1)
                end = True
            if end:
                break
            initval += dat[iii]
            #print(">", iii, initval)
            cur = 0
            can = True
            for i in range(iii + 1, n):
                cur += dat[i]
                #print(" >", i, cur)
                if cur == initval:
                    cur = 0
                    continue
                if cur > initval:
                    #print(">>fail")
                    can = False
                    break
            if cur != 0:
                can = False
            if can is True:
                target = initval
                res = 0
                i = 0
                cur = 0
                cnt = 0
                #print("target", target)
                for i in range(n):
                    cur += dat[i]
                    #print("i", cur)
                    cnt += 1
                    if cur == target:
                        res += cnt - 1
                        cur = 0
                        cnt = 0
                        continue
                print(res)
                return
            if end:
                break



    q = int(input())
    for _ in range(q):
        do()




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
        input = """4
5
3 1 6 6 2
4
1 2 2 1
3
2 2 2
4
6 3 2 1"""
        output = """4
2
0
2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()