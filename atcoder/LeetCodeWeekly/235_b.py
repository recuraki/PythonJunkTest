from typing import List, Tuple
import re


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ss=set()
        import collections
        d = collections.defaultdict(int)
        for id,task in logs:
            hash = 10**9 * id + task
            if hash in ss:
                continue
            d[id] += 1
            ss.add(hash)
        res = [0] * (k)
        for key in d.keys():
            res[d[key]-1] += 1
        return res


st=Solution()
print(st.findingUsersActiveMinutes(logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5))
print(st.findingUsersActiveMinutes(logs = [[1,1],[2,2],[2,3]], k = 4))

