
from typing import List, Tuple
from pprint import pprint


class Solution:
    def countCollisions(self, directions: str) -> int:
        from collections import deque
        q = deque([])
        ans = 0
        for x in directions:
            #print(x, q, ans)
            if x == "L": # 左に行きたい
                if len(q) == 0:
                    # 何もないなら、キューにすら残さなくていい
                    continue
                else:
                    n = q.pop()
                    if n == "S":
                        ans += 1
                    if n == "R":
                        ans += 2
                    # Sになるときの処理
                    while len(q) > 0:
                        nn = q.pop()
                        if nn == "R": ans += 1
                        else: continue
                    q.append("S")

            elif x == "S": #ストップ
                if len(q) == 0:
                    q.append("S")
                    continue
                else:
                    n = q.pop()
                    if n == "S":
                        q.append("S")
                        continue
                    q.append(n)
                    # Sになるときの処理
                    #print("!", q)
                    while len(q) > 0:
                        nn = q.pop()
                        #print("nn", nn)
                        if nn == "R": ans += 1
                        else: continue
                    q.append("S")

            elif x == "R": #ストップ
                q.append("R")

        return ans







st = Solution()

print(st.countCollisions(directions = "RLRSLL")==5)
print(st.countCollisions(directions = "LLRR")==0)
print(st.countCollisions(directions = "RRRRS")==4)
print(st.countCollisions(directions = "SLLLL")==4)

