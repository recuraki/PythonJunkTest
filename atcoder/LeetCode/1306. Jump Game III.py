class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)
        from collections import deque
        q = deque([start])
        while len(q) > 0:
            cur = q.popleft()
            if visited[cur]: continue
            visited[cur] = True
            if arr[cur] == 0: return True
            l = cur - arr[cur]
            r = cur + arr[cur]
            if 0 <= l < len(arr) and visited[l] is False: q.append(l)
            if 0 <= r < len(arr) and visited[r] is False: q.append(r)
        return False