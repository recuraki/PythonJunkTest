import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    n, k = map(int, input().split())
    dat = list(map(int, input().split()))
    maze = []
    initmaze=[]
    recurmaze=[]
    used = [-1] * (n + 10)
    cur = 0
    cnt = 0
    while True:
        if used[cur] != -1:
            break
        used[cur] = cnt
        maze.append(cur)
        cur = dat[cur] - 1
        cnt += 1

    recurpoint = used[cur]
    #print("return to ",recurpoint)
    initmaze = maze[:recurpoint]
    recurmaze = maze[recurpoint:]

    #print(maze)
    #print(initmaze)
    #print(recurmaze)

    l = len(maze)
    li = len(initmaze)
    lr = len(recurmaze)
    if k < li:
        print(initmaze[k] + 1)
    else:
        k -= li
        print(recurmaze[k%lr] + 1)




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
        input = """4 5
3 2 4 1"""
        output = """4"""       self.assertIO(input, output)

    def test_input_12(self):
        print("test_input_12")
        input = """4 1
3 2 4 1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """6 0
6 5 2 5 3 2"""
        output = """6"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()