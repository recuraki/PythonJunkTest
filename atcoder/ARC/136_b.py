import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        from copy import deepcopy
        a = deepcopy(data)
        b = deepcopy(datb)
        oa = deepcopy(data)
        ob = deepcopy(datb)
        a.sort()
        b.sort()
        if a != b: # 数が違えばそもそもだめ
            print("No")
            return
        a = None
        b = None
        def rot(i):
            data[i], data[i+1], data[i+2] = data[i+2], data[i], data[i+1]

        for _ in range(5):
            for i in range(n-2): # 揃えたい文字目
                target = datb[i] # ほしい文字
                for j in range(i, n):
                    if data[j] == target: break
                # j = ほしい文字が今ある場所
                cnt = 0
                while data[i] != target: # 揃うまで回す
                    cnt += 1
                    if cnt > 10000:
                        print("No")
                        return
                    if (j-i) == 1:
                        rot(i)
                        j = i + 2
                        continue
                    if (j-i) == 2:
                        rot(i)
                        j = i
                        continue
                    rot(j-2)
                    j -= 2
            for _ in range(10):
                if data == datb:
                    print("Yes")
                    return
                rot(n - 3)

            data = data[::-1]
            datb = datb[::-1]

            for i in range(n-2): # 揃えたい文字目
                target = datb[i] # ほしい文字
                for j in range(i, n):
                    if data[j] == target: break
                # j = ほしい文字が今ある場所
                cnt = 0
                while data[i] != target: # 揃うまで回す
                    cnt += 1
                    if cnt > 10000:
                        print("No")
                        return
                    if (j-i) == 1:
                        rot(i)
                        j = i + 2
                        continue
                    if (j-i) == 2:
                        rot(i)
                        j = i
                        continue
                    rot(j-2)
                    j -= 2
            for _ in range(10):
                if data == datb:
                    print("Yes")
                    return
                rot(n - 3)
            data = data[::-1]
            datb = datb[::-1]


        print("No")

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
3 1 4 5
4 1 5 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 2 2
2 1 2"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1 2 3
2 3 4"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """3
1 2 3
3 2 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()