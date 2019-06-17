import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())

    dat_a = list(map(int, input().split()))

    d = []
    for i in range(len(dat_a)):
        if dat_a[i] in d:
            # print("dup" + str(dat_a[i]))
            index = i+1
        d.append(dat_a[i])


    for i in range(n + 1):
        k = i + 1 # 何個選ぶか

        up = (n + 1)
        down = 1
        for x in range(1, k):
            down *= (x + 1)
            up *= (n + 1) - x
        # print("{0} / {1} = {2}".format(up, down, up//down))

        print("index")
        print(index)
        up = (n + 1) - index
        down = 1
        for x in range(1, k):
            down *= (x + 1)
            up *= (n + 1) - index - x
        print("{0} / {1} = {2}".format(up, down, up//down))


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
1 2 1 3"""
        output = """3
5
4
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
1 1"""
        output = """1
1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """32
29 19 7 10 26 32 27 4 11 20 2 8 16 23 5 14 6 12 17 22 18 30 28 24 15 1 25 3 13 21 19 31 9"""
        output = """32
525
5453
40919
237336
1107568
4272048
13884156
38567100
92561040
193536720
354817320
573166440
818809200
37158313
166803103
166803103
37158313
818809200
573166440
354817320
193536720
92561040
38567100
13884156
4272048
1107568
237336
40920
5456
528
33
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()