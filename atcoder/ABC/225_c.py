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
    def do():
        n, m = map(int, input().split())
        dat = []
        for _ in range(n):
            l = list(map(int, input().split()))
            dat.append(l)
        # まず、縦がうまく合うかを確認する
        for h in range(n - 1):
            for w in range(m):
                if (dat[h][w] + 7) == dat[h+1][w]: continue
                print("No")
                return
        # 次に、よこが正しいかを確認: 1( 1incか？)
        for w in range(m - 1):
            if (dat[0][w] + 1) == dat[0][w+1]: continue
            print("No")
            return
        # 要素-1 mod 7取って
        l = []
        for w in range(m):
            l.append( (dat[0][w] - 1) % 7)
        #print("step2", l)
        for w in range(m - 1):
            if (l[w] + 1) == l[w+1]: continue
            print("No")
            return

        print("Yes")

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
        input = """2 3
1 2 3
8 9 10"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
1
2"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 4
1346 1347 1348 1349
1353 1354 1355 1356
1360 1361 1362 1363
1367 1368 1369 1370
1374 1375 1376 1377
1381 1382 1383 1384
1388 1389 1390 1391
1395 1396 1397 1398
1402 1403 1404 1405
1409 1410 1411 1412"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_2")
        input = """2 1
1
8"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_212(self):
        print("test_input_2")
        input = """1 7
2 3 4 5 6 7 8"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()