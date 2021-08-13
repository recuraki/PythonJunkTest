from typing import List, Tuple
from pprint import pprint


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        st = map(int, startTime.split(":"))
        fi = map(int, finishTime.split(":"))
        st = list(st)
        fi = list(fi)
        s = st[0] * 60 + st[1]
        f = fi[0] * 60 + fi[1]
        #print(s, f)
        if f < s:
            f += (60 * 24)
        isstart = False
        cnt = 0
        for t in range(s, f + 1):
            if (t % 15) != 0:
                continue
            if isstart is False:
                isstart = True
                continue
            cnt += 1
        return cnt




st = Solution()

print(st.numberOfRounds(startTime = "12:01", finishTime = "12:44"))
print(st.numberOfRounds(startTime = "20:00", finishTime = "06:00"))
print(st.numberOfRounds(startTime = "00:00", finishTime = "23:59"))

