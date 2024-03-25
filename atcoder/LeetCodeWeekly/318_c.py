from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        from heapq import heappop, heapify, heappush
        n = len(costs)
        ans = 0
        q = []
        visited = [False] * n
        for i in range(candidates):
            if visited[i] is True: continue
            visited[i] = True
            q.append( (costs[i], i, 0) )
        for i in range(candidates):
            if visited[n-1-i] is True: continue
            visited[n-1-i] = True
            q.append( (costs[n-1-i], n-1-i, 1) )
        heapify(q)
        #print(visited)
        # l, rまでとっている
        l = candidates-1
        r = n-candidates
        for i in range(k):
            c, _, dir = heappop(q)
            ans += c
            #print(c, dir)
            if dir == 0:
                if l < (n-1):
                    if visited[l+1] is False:
                        l += 1
                        heappush(q, (costs[l], l, 0) )
                        visited[l]= True
            else: # dir = 1
                if r > 0:
                    if visited[r-1] is False:
                        r -= 1
                        heappush(q, (costs[r], r, 1) )
                        visited[r] = True
        print(ans)
        return ans


st = Solution()

print(st.totalCost( costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)==11)
print(st.totalCost(costs = [1,2,4,1], k = 3, candidates = 3)==4)
print(st.totalCost(costs = [2,2,2,2,1,3], k = 3, candidates = 1)==6)
print(st.totalCost(costs = [1,1,1], k = 3, candidates = 3)==3)
print(st.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2) == 423)
print(st.totalCost([28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34]
,32
,12) == 1407)
