from typing import List, Tuple
from pprint import pprint


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        from collections import deque
        from heapq import heapify, heappop, heappush
        turn = 0
        madamadatask = []
        heapify(madamadatask)
        korekaraq = []
        heapify(korekaraq)
        for i in range(len(tasks)):
            enque, needtime = tasks[i]
            heappush(madamadatask, (enque,needtime, i))
        curtime = -1
        res = []
        while len(madamadatask) != 0 or len(korekaraq) != 0:
            if len(korekaraq) == 0: # 新しい仕事が必要
                enque, needtime, index = heappop(madamadatask)
                heappush(korekaraq, (needtime, index, enque) )
                curtime = enque
                continue
            # やるべき仕事がある
            #print(" search", korekaraq)
            #print(" time", curtime)
            needtime, index, enque  = heappop(korekaraq)
            if curtime < enque:
                curtime = enque
            #print("step", turn, "dodo", needtime, enque, index, "using", needtime)
            curtime += needtime
            #print('curtime =', curtime)
            res.append(index)
            while len(madamadatask) > 0:
                enque, needtime,  index = heappop(madamadatask)
                if enque > curtime:
                    heappush(madamadatask, (enque ,needtime, index))
                    break
                heappush(korekaraq, (needtime, index, enque) )
            #print("endjob", korekaraq)
        return (res)


st = Solution()

print(st.getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
print(st.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))

print(st.getOrder(tasks =[[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(st.getOrder(tasks =[[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]) == [6,1,2,9,4,10,0,11,5,13,3,8,12,7])
# NG:[6, 1, 2, 9, 4, 10, 0, 11, 13, 5, 3, 8, 12, 7]
# OK:[6,1,2,9,4,10,0,11,5,13,3,8,12,7]
