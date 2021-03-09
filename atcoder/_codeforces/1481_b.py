import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        #print()
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        res = -1
        for kcnt in range(k):
            #print(dat, k)
            done = False
            for i in range(n-1):
                #print(">try",i)
                if dat[i] >= dat[i+1]:
                    continue
                else: # dat[i] < dat[i+1]
                    #print(" fit!", kcnt, k-1)
                    dat[i] += 1
                    res = i + 1
                    done = True
                    if kcnt == k-1:
                        #print("leave")
                        print(i+1)
                        return
                    break
            if done is False:
                print(-1)
                return
        print(res)



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
4 3
4 1 2 3
2 7
1 8
4 5
4 1 2 3
3 1
5 3 1"""
        output = """2
1
-1
-1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()