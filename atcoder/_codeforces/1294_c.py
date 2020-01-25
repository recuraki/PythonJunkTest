import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                for j in range(cnt):
                    arr.append(i)

        if temp != 1:
            arr.append(temp)

        if arr == []:
            arr.append(n)

        return arr
    n = int(input())
    for _ in range(n):
        x = int(input())
        dat = factorization(x)
        datlen = len(dat)
        #print("--")
        #print(x)
        #print(l)
        if len(dat) <= 2:
            print("NO")
        else:
            f = False
            a = 1
            for i in range(datlen):
                a *= dat[i]
                b = 1
                for j in range(i+1, datlen):
                    b *= dat[j]
                    c = 1
                    for k in range(j+1, datlen):
                        c *= dat[k]
                    if a != b and b != c and a != c and a != 1 and b != 1 and c != 1:
                        f = True
                        break
                if f:
                    break
            if f:
                print("YES")
                print("{0} {1} {2}".format(a, b, c))
            else:
                print("NO")




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
        input = """5
64
2
97
2
12345"""
        output = """YES
2 4 8 
NO
NO
NO
YES
3 5 823 """
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()