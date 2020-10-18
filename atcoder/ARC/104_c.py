import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        import collections
        n = int(input())
        maze = [-1] * (2*n)
        mazedir = [-1] * (2*n)
        datc = [-1] * n
        dathuman = []
        for i in range(n):
            dathuman.append([-1, -1])
        for i in range(n):
            a, b = map(int, input().split())
            a, b = a-1, b-1

            datc[i] = b-a-1

            print(a, b, maze)
            if a != -2 and maze[a] != -1:
                print("No")
                return
            elif a != -2:
                maze[a] = i
                mazedir[a] = "L"
                dathuman[i][0] = a if a != -2 else -1

            if b != -2 and maze[b] != -1:
                print("No")
                return
            elif b != -2:
                maze[b] = i
                mazedir[b] = "R"
                dathuman[i][1] = b if b != -2 else -1

        print("datc", datc)
        print("dathuman", dathuman)
        print("umeru start",maze)
        print("umeru start",mazedir)

        #  カウント
        allfree = maze.count(-1)
        print("allfree" , allfree)
        fcntL = [None] * (2*n)
        fcntR = [None] * (2*n)
        # ⇒
        cnt = allfree
        for i in range(2*n):
            if mazedir[i] == -1:
                fcntL[i] = cnt
                cnt -= 1
            else:
                fcntL[i] = cnt
                continue
        # ←
        cnt = allfree
        for i in range(2*n-1, -1, -1):
            if mazedir[i] == -1:
                fcntR[i] = cnt
                cnt -= 1
            else:
                fcntR[i] = cnt
                continue

        #print("L", fcntL)
        #print("R", fcntR)

        #
        for i in range(n):
            a, b = dathuman[i]
            if a != -1 and b != -1: # 両方決まっている人なら何もしない
                continue
            if a == -1 and b == -1: # どこでもいい人は一旦後回しにする
                continue
            print("fill", i, a,b, maze)

            if b == -1: # 終わりが決まっていない人
                for j in range(2*n - 1 , a, -1): # 向こうから探索
                    if maze[j] == -1:
                        maze[j] = i # そこはiのものにして
                        dathuman[i][1] = j # bにする
                        break # で、おわり
            if a == -1: # 始まりがない人
                print("a try")
                for j in range(0, b):
                    print(j)
                    if maze[j] == -1:
                        print("fill!")
                        maze[j] = i # そこはiのものにして
                        dathuman[i][0] = j # aにする
                        break # で、おわり

        for i in range(n):
            a, b = dathuman[i]
            if a != -1 and b != -1:
                for j in range(2*n):
                    if maze[j] == -1:
                        for k in range(j+1, 2*n):
                            if maze[k] == -1:
                                maze[j] = j
                                maze[k] = k
                                dathuman[i] = [j, k]

        # ここで未決定があるならだめ
        if -1 in maze:
            print("No")
            return
        c = collections.Counter(maze)
        # 3つ以上あるのもだめ
        for k in c.keys():
            if c[k] != 2:
                print("No")
                return

        # ここから判定
        for i in range(n):
            a, b = dathuman[i]
            datc[i] = b-a-1

        print("datc", datc)
        print("dathuman", dathuman)
        print("judge start",maze)
        can = True
        isride = [False] * n
        rideval = -1
        ridecount = 0

        for i in range(2*n):
            print("i,", i, ridecount, rideval)
            x = maze[i]
            if isride[x] is True:
                ridecount -= 1
                if ridecount == 0:
                    rideval = -1
            if ridecount == 0:
                ridecount += 1
                rideval = datc[x]
                isride[x] = True
                continue
            if rideval != datc[x]:
                print("No")
                return
            ridecount += 1
            isride[x] = True
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
        input = """3
1 -1
-1 4
-1 6"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1 4
2 3"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
4 1
2 4"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()