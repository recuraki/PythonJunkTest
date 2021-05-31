import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        maze = []
        for _ in range(n):
            l = list(map(int, input().split()))
            maze.append(l)
        diffx = []
        diffy = []
        curdiff = None
        for i in range(n - 1):
            diffx.append(maze[0][i+1] - maze[0][i])
            diffy.append(maze[i+1][0] - maze[i][0])
        #print(diffx)
        #print(diffy)
        check = True
        for j in range(n):
            for i in range(n - 1):
                if (maze[j][i + 1] - maze[j][i]) != diffx[i]:
                    check = False
                    print("No")
                    return
                if (maze[i + 1][j] - maze[i][j]) != diffy[i]:
                    check = False
                    print("No")
                    return
        x = 10** 14
        resa = [maze[0][0]]
        resb = [0]
        for i in range(n - 1):
           resa.append(resa[-1] + diffx[i])
           resb.append(resb[-1] + diffy[i])
        #print(resa)
        #print(resb)

        m = min(resa)
        if m < 0:
            resa = list(map(lambda x: x - m, resa))
            resb = list(map(lambda x: x + m, resb))
        #print(resa)
        #print(resb)

        m = min(resb)
        if m < 0:
            resa = list(map(lambda x: x + m, resa))
            resb = list(map(lambda x: x - m, resb))
        #print(resa)
        #print(resb)

        if min(resa) < 0:
            print("No")
        if min(resb) < 0:
            print("No")

        print("Yes")
        resa, resb = resb, resa
        for i in range(n):
            l = []
            for j in range(n):
                l.append(resa[i] + resb[j])
            print(" ".join(list(map(str, l))))

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
        input = """3
4 3 5
2 1 3
3 2 4"""
        output = """Yes
2 0 1
2 1 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
4 3 5
2 2 3
3 2 4"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()