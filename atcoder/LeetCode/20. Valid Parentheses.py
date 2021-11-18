class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        q = deque([])
        for x in s:
            if x in ["(", "[", "{"]:
                q.appendleft(x)
                continue
            if len(q) <= 0: return False
            if x == ")":
                if q[0] != "(": return False
                q.popleft()
            elif x == "}":
                if q[0] != "{": return False
                q.popleft()
            elif x == "]":
                if q[0] != "[": return False
                q.popleft()
        if len(q) > 0: return False
        return True


