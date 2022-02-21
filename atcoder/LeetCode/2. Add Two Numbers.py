
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = False
        new = ListNode()
        ans = new
        new.val = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
        if new.val > 9:
            new.val %= 10
            carry = True
        while l1 is not None or l2 is not None:
            new.next = ListNode()
            new = new.next
            new.val += l1.val if l1 is not None else 0
            new.val += l2.val if l2 is not None else 0
            new.val+= 1 if carry else 0
            carry = False
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if new.val > 9:
                new.val %= 10
                carry = True
        if carry:
            new.next = ListNode(val=1)
        return ans