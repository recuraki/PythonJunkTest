from typing import List, Tuple, Optional
from pprint import pprint
from collections import deque, defaultdict


class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        g = [set() for _ in range(n)]
        cnt = [0] * n
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].add(v)
            g[v].add(u)
            cnt[u] += 1
            cnt[v] += 1
        odd = even = 0
        oddnode = []
        evennode = []
        for i in range(n):
            if (cnt[i] % 2) == 0:
                even += 1
                evennode.append(i)
            else:
                odd += 1
                oddnode.append(i)
        # 判定: fullでoddがある場合絶対無理
        for i in range(n):
            if (cnt[i] % 2 ) == 0: continue
            # oddで fullなら絶対無理
            if (cnt[i] == (n-1)): return False

        # まず、奇数が4つ以上あるなら無理
        if odd > 4: return False
        if odd == 0: return True # 既にOK
        if odd == 1: return False # だめ
        if odd == 3: return False # だめ
        if odd == 2:
            # その2つは対応できる？
            assert len(oddnode) == 2
            u, v = oddnode[0], oddnode[1]
            if v not in g[u]: return True # 結びつけて終わり
            # そうでないなら、両方をつなげるevenがないとダメ
            for i in evennode:
                if v not in g[i] and u not in g[i]: return True
            return False
        # odd = 4
        import itertools
        from copy import deepcopy
        oevennode = deepcopy(evennode)
        ooddnode = deepcopy(oddnode)
        oodd = odd
        oeven = even
        ocnt = deepcopy(cnt)
        og = deepcopy(g)
        for pat in itertools.permutations(ooddnode):
            evennode = deepcopy(oevennode)
            oddnode = deepcopy(pat)
            oddnode = list(oddnode)
            odd = oodd
            even = oeven
            cnt = deepcopy(ocnt)
            g = deepcopy(og)



            for loop in range(2):
                if len(oddnode) == 0: break
                # ↑oddがないなら終わり
                cur = oddnode.pop()
                odd -= 1
                candidate = None
                # 奇数ノードとのマッチングを測る
                for i in range(len(oddnode)):
                    x = oddnode[i]
                    if cnt[x] == n - 1: assert False # これはいてはならない
                    if x in g[cur]: continue # もう辺があるなら無理
                    # そうでないならマッチング
                    candidate = x
                    del oddnode[i]
                    odd -= 1
                    break
                if candidate is not None:
                    even += 2
                    evennode.append(cur)
                    evennode.append(candidate)
                    g[cur].add(candidate)
                    g[candidate].add(cur)
                    continue
                # 偶数ノードとのマッチングを測るしかない
                for i in range(len(evennode)):
                    x = evennode[i]
                    if cnt[x] == n - 2: continue # これはだめ
                    if x in g[cur]: continue # もう辺があるなら無理
                    candidate = x
                    del evennode[i]
                    even -= 1
                    break
                if candidate is not None:
                    even += 1
                    odd += 1
                    evennode.append(cur)
                    oddnode.append(candidate)
                    g[cur].add(candidate)
                    g[candidate].add(cur)
                    continue
                return False
            if odd == 0: return True

        return False








        return True




st = Solution()

#print(st.isPossible(n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]])==True)
#print(st.isPossible(n = 4, edges = [[1,2],[3,4]])==True)
#print(st.isPossible(n = 4, edges = [[1,2],[1,3],[1,4]])==False)
#print(st.isPossible(n = 4, edges = [[1,2],[2,3],[2,4],[3,4]])==False)
print(st.isPossible(n = 6, edges = [[1,6],[1,3],[1,4],[4,5],[5,2]])==True)
