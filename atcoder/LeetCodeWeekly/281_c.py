from typing import List, Tuple
from pprint import pprint


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = [0] * 26
        for x in list(s):
            ch = ord(x) - ord("a")
            cnt[ch] += 1
        cnt = reversed(cnt)
        cnt = list(cnt)
        ans = []
        last = -1 # 何を使った？
        while True:
            did = False
            best = -1 # 一番使いたい奴！
            for i in range(26):
                if cnt[i] == 0: continue # もうないなら使えない
                best = i
                break

            for i in range(26):
                if i == last: continue # 同じ文字は使えない
                if cnt[i] == 0: continue # もうないなら使えない
                # 作れる
                if i == best:
                    for loop in range(min(repeatLimit, cnt[i])):
                        ans.append(chr(ord("z") - i))
                    cnt[i] -= min(repeatLimit, cnt[i])
                else: # not best
                    ans.append(chr(ord("z") - i))
                    cnt[i] -= 1
                did = True
                last = i
                break

            if did is False: break # all 0

        return("".join(ans))


st = Solution()

print(st.repeatLimitedString(s = "cczazcc", repeatLimit = 3))
print(st.repeatLimitedString(s = "aababab", repeatLimit = 2))
