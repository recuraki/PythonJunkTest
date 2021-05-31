from typing import List, Tuple
from pprint import pprint


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        dat = []
        zatsuforward = dict()
        zatsuback = dict()
        restrictions.sort()
        print(restrictions)
        if len(restrictions) == 0:
            return n-1
        for i in range(len(restrictions)):
            dat.append([i, restrictions[i][0], restrictions[i][1] ])
            zatsuforward[restrictions[i][0]] = i
            zatsuback[i] = restrictions[i][0]
        bufl = [0] * (len(restrictions) + 1)
        bufr = [0] * (len(restrictions) + 1)
        #print(zatsuforward)
        lasttime = 1
        for i in range(len(dat)):
            ind, nexttime, limit = dat[i]
            #print(nexttime)
            curlimit = bufl[i]
            bufl[i+1] = min(curlimit+ (nexttime-lasttime), limit)
            lasttime = nexttime
        #print(bufl)


        lasttime = dat[-1][1]
        bufr[-1] = dat[-1][2]
        #print(bufr)
        for i in range(len(dat)-1, 0, -1):
            #print("ind", i)
            ind, nexttime, limit = dat[i]
            #print(i, nexttime)
            curlimit = bufr[i+1]
            bufr[i] = min(curlimit+ (lasttime-nexttime), limit)
            lasttime = nexttime
        #print(bufr)

        import math
        res = 0
        dat = [[0,0,0]] + dat
        bufl.append(bufl[-1] + (n-restrictions[-1][0]))
        bufr.append(10**18)
        print(bufl)
        print(bufr)
        dat.append([None, n, None])
        for i in range(len(dat) - 1):
            #print("i", i)
            _, curtime, _ = dat[i]
            _, nexttime, _ = dat[i+1]
            print("calo", curlimit, curtime, nexttime)
            limitl = min(bufl[i], bufr[i])
            limitr = min(bufl[i+1], bufr[i+1])
            curtime += abs(limitl - limitr)
            curlimit = max(limitl, limitr)
            if (nexttime - curtime) > 1:
                curlimit += math.ceil( (nexttime - curtime) / 2)
            print("calc", curlimit, curtime, nexttime)
            res = max(curlimit , res)
        return res

st = Solution()

#print(st.maxBuilding(n = 5, restrictions = [[2,1],[4,1]]))
#print(st.maxBuilding(n = 6, restrictions = []))
#print(st.maxBuilding(n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]))
#print(st.maxBuilding(n=10, restrictions=[[6,0],[5,2],[7,0],[9,1],[2,4],[3,4],[4,0],[8,2],[10,0]]) == 1)
#print(st.maxBuilding(10, [[2, 4], [3, 2], [4, 0], [5, 3], [6, 2], [7, 3], [8, 5], [9, 0], [10, 0]]) == 2)
print(st.maxBuilding(100,[[2, 35], [3, 46], [4, 19], [5, 36], [6, 2], [7, 26], [8, 50], [9, 3], [10, 42], [11, 3], [12, 15], [13, 27], [14, 47], [15, 39], [16, 4], [17, 10], [18, 38], [19, 9], [20, 24], [21, 50], [22, 40], [23, 48], [24, 17], [25, 30], [26, 34], [27, 0], [28, 30], [29, 39], [30, 8], [31, 8], [32, 36], [33, 47], [34, 19], [35, 0], [36, 22], [37, 22], [38, 48], [39, 39], [40, 5], [41, 0], [42, 48], [43, 25], [44, 32], [45, 20], [46, 15], [47, 24], [48, 12], [49, 30], [50, 9], [51, 21], [52, 19], [53, 8], [54, 9], [55, 43], [56, 39], [57, 50], [58, 4], [59, 33], [60, 45], [61, 29], [62, 12], [63, 35], [64, 45], [65, 0], [66, 45], [67, 43], [68, 36], [69, 21], [70, 48], [71, 15], [72, 12], [73, 33], [74, 25], [75, 45], [76, 32], [77, 42], [78, 36], [79, 3], [80, 7], [81, 2], [82, 27], [83, 33], [84, 15], [85, 21], [86, 42], [87, 30], [88, 38], [89, 27], [90, 12], [91, 11], [92, 9], [93, 30], [94, 25], [95, 26], [96, 10], [97, 21], [98, 5], [99, 12], [100, 35]]
)==11)