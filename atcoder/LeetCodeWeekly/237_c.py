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
        # madamada taskは全体のタスクをenqueの順番に並べたもの．
        # 実施するタスクではなくて、今後実施できるようになるタスク
        curtime = -1
        res = []
        # korekarataskはすでに実施できて、どれを実施するか迷うもの．
        # これは、条件の通り、needtimeが最小、同じ場合はindexが最小の物を取り出す
        while len(madamadatask) != 0 or len(korekaraq) != 0:
            if len(korekaraq) == 0: # キューに仕事がないなら新しい仕事が必要．
                # この場合、現在の時間に関係なく１つ取り出し、時間を開始時間まで飛ばす
                enque, needtime, index = heappop(madamadatask)
                heappush(korekaraq, (needtime, index, enque) )                #
                curtime = enque
                continue
            # やるべき仕事がある場合、それを実施する
            needtime, index, enque  = heappop(korekaraq)
            if curtime < enque:
                curtime = enque
            curtime += needtime
            res.append(index)
            # ここで時間は現在の実施後まで飛んでいるので、
            # それで実施可能になった仕事をキューに入れる
            while len(madamadatask) > 0:
                enque, needtime,  index = heappop(madamadatask)
                if enque > curtime:
                    heappush(madamadatask, (enque ,needtime, index))
                    break
                heappush(korekaraq, (needtime, index, enque) )
        return (res)


st = Solution()

print(st.getOrder(tasks = [[1,2],[2,4],[3,2],[4,1]]))
print(st.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]))

print(st.getOrder(tasks =[[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
print(st.getOrder(tasks =[[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]) == [6,1,2,9,4,10,0,11,5,13,3,8,12,7])
# NG:[6, 1, 2, 9, 4, 10, 0, 11, 13, 5, 3, 8, 12, 7]
# OK:[6,1,2,9,4,10,0,11,5,13,3,8,12,7]
