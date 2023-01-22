from typing import List, Tuple, Optional
from pprint import pprint


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import math
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        target = math.floor(n/2)
        print(n, target)
        cur = head
        if n == 1:
            return None
        n = 0
        while cur is not None:
            n += 1 # next index
            if n == target:
                cur.next = cur.next.next
            cur = cur.next
        return head


"""
7 3
4 2
2 1

[1,3,4,1,2,6]
[1,2,4]
[2]
"""


st = Solution()

print(st.defdef())

