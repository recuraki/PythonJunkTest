from typing import List, Tuple
from pprint import pprint


###################################
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        ans = 0
        tasks.sort(reverse=True)
        workers.sort(reverse=True)
        #print(tasks)
        #print(workers)
        nokoriTask = []
        nokoriWorker = []
        ans = 0
        taskind = 0
        for i in range(len(workers)):
            # 弱いやつを回す
            if workers[i] >= tasks[taskind]:
                taskind += 1
                ans += 1
                continue
            nokoriWorker.append(workers[i])
        for i in range(taskind, len(tasks)):
            nokoriTask.append(tasks[i])
        #print("end")
        #print(nokoriTask)
        #print(nokoriWorker, ans)
        nokoriTask.sort()
        from collections import deque
        nokoriWorker.sort(reverse=True)
        nokoriWorker = deque(nokoriWorker)
        import math
        for i in range(len(nokoriTask)):
            #print(i , ans, pills)

            if len(nokoriWorker) <= 0: break
            need = nokoriTask[i]
            power = nokoriWorker.popleft()
            needpill = math.ceil((need - power ) / strength)
            if needpill <= pills and needpill == 1:
                #print("Ues")
                ans += 1
                pills -= 1
        return ans



###################################


st = Solution()
print(st.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))
print(st.maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))
print(st.maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))
print(st.maxTaskAssign(tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5))


"""
クエリ以下で買える最大の美しさ
"""