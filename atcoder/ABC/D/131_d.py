import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    tasks = []
    for i in range(n):
        a,b = map(int, input().split())
        tasks.append((a,b))

    tasks.sort(key=lambda x:x[1])
    #print(tasks)

    cur = 0
    c = True
    for i in range(n):
        cur += tasks[i][0]
        if cur > tasks[i][1]:
            c = False

    print("Yes" if c else "No")


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
2 4
1 9
1 8
4 9
3 12"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
334 1000
334 1000
334 1000"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """30
384 8895
1725 9791
170 1024
4 11105
2 6
578 1815
702 3352
143 5141
1420 6980
24 1602
849 999
76 7586
85 5570
444 4991
719 11090
470 10708
1137 4547
455 9003
110 9901
15 8578
368 3692
104 1286
3 4
366 12143
7 6649
610 2374
152 7324
4 7042
292 11386
334 5720"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()