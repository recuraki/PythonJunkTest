from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        se1 = defaultdict(int)
        se2 = defaultdict(int)
        for x in word1: se1[x] += 1
        for x in word2: se2[x] += 1
        # se 1 >= se 2としたい
        if len(se1) < len(se2):
            se1, se2 = se2, se1
            word1, word2 = word2, word1
        #print(se1, se2)
        diffchar = (len(se1) - len(se2))
        print(">", diffchar, word1, word2)
        # 3以上の時は何をしてもだめ
        if diffchar >= 3:
            return False
        # 0の場合、必ずswapしないといけないので
        # pat1: count1同士をswapする
        # pat2: count>=2同士をswapする
        # が必要
        if diffchar == 0:
            for a in list_lower:
                if se1[a] == 0: continue
                for b in list_lower:
                    if se2[b] == 0: continue
                    if se1[a] == se2[b] == 1: return True
                    if se1[a] >=2 and  se2[b] >= 2: return True
            return False
        # 1の時、se2を1つ増やさないといけない
        # pat1: se1に2つ以上あり、se2にないものをあげる (se2++)
        # pat1: se1に1つしかなく、se2にあるものを上げる (se1++)
        if diffchar == 1:
            for a in list_lower:
                if se1[a] == 0: continue
                for b in list_lower:
                    if se2[b] == 0: continue
                    #if se1[a] >= 2 and se2[b] == 0: return True
                    if se1[a] == 1 and se2[b] >= 2:
                        return True
            return False
        # 2の時、se2を2つふやさないといけない
        # pat1: se1に1つしかなく、se2にないものを上げる(se1--, se2++)
        if diffchar == 2:
            for a in list_lower:
                if se1[a] == 0: continue
                for b in list_lower:
                    if se2[b] == 0: continue
                    if se1[a] == 1 and se2[b] == 0: return True
            return False


st = Solution()

print(st.isItPossible(word1 = "abcd", word2 = "a")==False) # むり
print(st.isItPossible(word1 = "abc", word2 = "d")==False) # むり
print(st.isItPossible(word1 = "abc", word2 = "a")==False) # むり
print(st.isItPossible(word1 = "ac", word2 = "b")==False) # むり
print(st.isItPossible(word1 = "ac", word2 = "a")==True) # aa, c
print(st.isItPossible(word1 = "abcc", word2 = "aab")==True) # abca, acb
print(st.isItPossible(word1 = "abcde", word2 = "fghij")==True) # どれをひっくりかえしてもOK
print(st.isItPossible(word1 = "abc", word2 = "ddeeff")==False) # abd, cdeeff など絶対に3,4になる
print(st.isItPossible(word1 = "c", word2 = "ac")==True) # a, cc

