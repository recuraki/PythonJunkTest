from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        need = [0] * n
        useful = [0] * 2000
        hani = [0] * n # カバーできる範囲
        cando = [set() for _ in range(2000)] # その時間にこなせるタスク
        for taskid in range(n):
            tasks[taskid][0] -= 1
            tasks[taskid][1] -= 1
        nokori = []
        for taskid in range(n):
            s, e, d = tasks[taskid]
            need[taskid] = d
            hani[taskid] = e - s + 1
            for t in range(s, e+1):
                useful[t] += 1
                cando[t].add(taskid)
        #print(useful[:10])
        ans = 0
        while True:
            #print(useful[:10])
            #print(hani)
            curmax = 0
            dot = -1
            cans = 10**9
            cane = 10**9
            hanimin = -1
            haniid = None
            for taskid in range(n):
                if hani[taskid] > hanimin:
                    hanimin = hani[taskid]
                    haniid = taskid
            if haniid is None: break
            s, e, _ = tasks[haniid]
            #print("wanto do", taskid, s,e)
            for t in range(s, e+1):
                if useful[t] > curmax:
                    curmax = useful[t]
                    dot = t

            if dot == -1: break
            #print("> do", dot)
            ans += 1
            useful[dot] = 0 # もう使った
            # dotをやっていくぞい
            finished = []
            for dotask in cando[dot]:
                need[dotask] -= 1
                hani[dotask] -= 1
                if need[dotask] == 0: # dotaskが終わった
                    finished.append(dotask)
                    hani[dotask] = -100
            for dotask in finished:
                s, e, _ = tasks[dotask]
                for t in range(s, e + 1):
                    useful[t] = max(0, useful[t] - 1)
                    cando[t].remove(dotask)
        #print(ans)
        return ans



st = Solution()

print(st.findMinimumTime(tasks = [[2,3,1],[4,5,1],[1,5,2]])==2)
print(st.findMinimumTime(tasks = [[2,2,1],[4,4,1],[5,5,1]])==3)
print(st.findMinimumTime(tasks = [[1,3,2],[2,5,3],[5,6,2]])==4)
print(st.findMinimumTime(tasks = [[1,2000,2000], [2,2,1]])==2000)
print(st.findMinimumTime(tasks = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],])==1)

print(st.findMinimumTime(tasks = [[1,2000,1], [2,2,1]])==1)
print(st.findMinimumTime(tasks = [[1,2000,1], [1,4,3], [2,4,2], [4,4,1]])==3)
print(st.findMinimumTime(tasks = [[2000,2000,1], [1,1,1]])==2)


