import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        s = input() # ABCを
        s = s.replace("A", "0").replace("B", "1").replace("C", "2") # 012にして
        s = list(s) # ["0", "1", "2"]にしてから
        s = list(map(int, s)) # [0, 1, 2]にする

        def f(t, i):
            if t == 0: return s[i]
            if t<=60:
                if i % 2 == 0: return (f(t-1, i//2) + 1) % 3
                else: return (f(t-1, i//2) + 2) % 3
            else:
                return (f(60, i) + (t-60)) % 3

        q = int(input())
        ansdict = {0:"A", 1:"B", 2:"C"}
        for _ in range(q):
            t, k = map(int, input().split())
            k -= 1 # 1-indexed -> 0-indexed
            print(ansdict[f(t, k)])
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
        input = """ABC
4
0 1
1 1
1 3
1 6"""
        output = """A
B
C
B"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """CBBAACCCCC
5
57530144230160008 659279164847814847
29622990657296329 861239705300265164
509705228051901259 994708708957785197
176678501072691541 655134104344481648
827291290937314275 407121144297426665"""
        output = """A
A
C
A
A"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()