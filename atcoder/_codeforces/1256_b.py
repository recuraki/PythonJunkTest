import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    qq = int(input())
    for q in range(qq):
        n = int(input())
        dat = list(map(int, input().split()))
        already = [False] * 110
        for j in range(0, n - 1):
            #print("j:{0}".format(j))
            ma = 99999
            maindex = 99999
            for i in range(0, n - 1):
                if already[i]:
                    continue
                if dat[i] < dat[i+1]:
                    continue
                if dat[i + 1] < ma:
                    if dat[i+1] == n:
                        continue
                    maindex = i
                    ma = dat[i + 1]
            if maindex == 99999:
                break
            else:
                #print("maindex:{0}, ma:{1}".format(maindex, ma))
                already[maindex] = True
                dat[maindex], dat[maindex+1] = dat[maindex + 1], dat[maindex]
        #print(dat)
        dat = list(map(lambda x: str(x), dat))
        print(" ".join(dat))






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
5 4 1 3 2
4
1 2 4 3
1
1
4
4 3 2 1"""
        output = """1 5 2 4 3
1 2 3 4
1
1 4 3 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


