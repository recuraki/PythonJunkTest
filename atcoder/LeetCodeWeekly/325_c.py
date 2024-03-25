from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict

###################################
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:

        # [ok, ng) for max value
        # (ng, ok] for min value
        # CATION: ok is result  (NOT mid)
        price.sort()
        def f(target):
            cnt = 2
            lval = price[0]
            rval = price[len(price)-1]
            #print(price)
            if abs(lval - rval) < target: return False
            l = 1
            r = len(price) - 2
            while cnt < k:
                if not (l <= r): return False
                #print("cut cnt", cnt, lval, rval, l, r, price[l], price[r])
                if abs(lval - price[l]) >= target and abs(rval - price[l]) >= target:
                    lval = price[l]
                    l += 1
                    cnt += 1
                    #print("ok1")
                    continue
                l+=1
                if abs(lval - price[r]) >= target and abs(rval - price[r]) >= target:
                    rval = price[r]
                    r -= 1
                    cnt += 1
                    #print("ok2")
                    continue
                r-=1
            return True

        ok = 0
        ng = 10**9 + 20

        while (abs(ok - ng) > 1):
            mid = (ok + ng) // 2;
            #print(mid, f(mid))

            if (f(mid)):
                ok = mid;
            else:
                ng = mid;
        print(ok)
        return ok



st = Solution()

print(st.maximumTastiness(price = [13,5,1,8,21,2], k = 3)==8)
print(st.maximumTastiness(price = [1,3,1], k = 2)==2)
print(st.maximumTastiness(price = [7,7,7,7], k = 2)==0)
print(st.maximumTastiness(price = [2,4,6], k = 3)==2)
print(st.maximumTastiness([34,116,83,15,150,56,69,42,26], 6) == 19)
