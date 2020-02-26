import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = "0" + input()
    s = list(map(int,s))
    so = list(map(int,s))
    pay = 0
    otsuri = 0
    import collections
    dpay = collections.deque([])
    dotsuri = collections.deque([])

    kuriagari = False
    for i in range(len(s)-1, -1, -1):
        c = s[i]

        if i == 0 and c == 0:
            break

        if c == 10:
            s[i] = 0
            s[i - 1] += 1
            dotsuri.appendleft(0)
            dpay.appendleft(0)
            continue

        if 0 <= c <= 5:
            pay += c # 自分が払う
            dpay.appendleft(c)
            dotsuri.appendleft(0)
        elif 6 <= c:
            s[i - 1] += 1
            otsuri += (10 - c)  # お釣りの枚数
            dpay.appendleft(0)
            dotsuri.appendleft((10 - c) )

    print(pay + otsuri)

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
        input = """314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """91"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_51111112(self):
        print("test_input_3")
        input = """91"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_511111123(self):
        print("test_input_3")
        input = """50"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()