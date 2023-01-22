
from typing import List, Tuple
from pprint import pprint


# 最小値（最大値）を O(logN)O(log⁡N)で取り出す
class Solution:

    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        sq = []
        eventq = []
        taskq = []
        madamadaq = []

        from heapq import heapify, heappop, heappush

        # 処理するサーバの順序。あたまこそやりたい
        for i in range(len(servers)):
            sq.append( (servers[i], i) ) # 重みが小さく、インデックスが小さい
        heapify(sq)


        for i in range(0,len(tasks)):
            eventq.append((i, 0, (i, tasks[i])))
        heapify(madamadaq)

        heapify(eventq)
        res = [-1] * len(tasks)

        curtime = 0
        while len(eventq) > 0:
            curtime, _, _ = eventq[0]
            #print(">>> ", curtime, sq)
            while len(eventq) > 0: # 同じ時間のイベントを処理する
                time, type, arg = eventq[0]
                assert time >= curtime
                if time > curtime: # 未来のイベントなら無視
                    break
                # 今のイベントなら
                time, type, arg = heappop(eventq)
                if type == 0: # (i, 0, (-i, tasks[i])) タスク発生, index
                    #print("REGIST", curtime, ": newtask", arg)
                    heappush(taskq, arg)
                if type == 1: #(i, 1, (weigth, index)) サーバ処理終わり
                    #print("RELEASE", curtime, ": release server", arg)
                    heappush(sq, arg)

            while len(taskq) > 0: # 仕事がある場合
                if len(sq) <= 0: # 割り当てられないかとらい
                    break
                # あるなら絶対処理できるので
                weigth, sindex = heappop(sq)
                taskind, taskomosa = heappop(taskq)
                taskind *= 1
                res[taskind] = sindex
                heappush(eventq,  (curtime + taskomosa, 1, (weigth, sindex)) )
                #print("ASSIGN! task{0} omosa{1} -> server{2} weitgh{3} -> release will {4}".format(taskind, taskomosa, sindex, weigth, curtime + taskomosa))

        return (res)




st = Solution()
print(st.assignTasks(servers = [3,3,2], tasks = [1,2,3,2,1,2]))
print(st.assignTasks( servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]))
print(st.assignTasks([10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5]))
print(st.assignTasks([10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5]) == [8,0,3,9,5,1,10,6,4,2,7,9,0])

