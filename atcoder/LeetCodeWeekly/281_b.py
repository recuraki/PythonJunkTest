from typing import List, Tuple, Optional
from pprint import pprint


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pesudo = ListNode()
        cur = pesudo
        pesudo.next = cur
        while head.next != None:
            if head == None: break
            # head == 0
            newnode = ListNode()
            cur.next = newnode
            head = head.next # 0の次
            while head.val != 0:
                cur.val += head.val
                head = head.next

        return pesudo.next







st = Solution()

print(st.defdef())
