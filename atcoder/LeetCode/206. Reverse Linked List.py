# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        O(N)が目指せそう
        1個ずつswapすれば良さそう
        初期ノードはNoneに向けてあげることに注意
        0の時0
        p:n -> c:1->2->3->4->5 -> n
        p:1->n , c:2->3->4->5 -> n
        p:2->1->n , c:3->4->5 -> n

        """
        if head is None: return None
        curnode = head
        prevnode = None
        while curnode is not None:  # 例えば、2にいるとき、
            nextnode = curnode.next  # いったん、次の探索は3と覚えて起き、
            curnode.next = prevnode  # 2 のnextは前の、つまり、1として、おわり。
            prevnode = curnode  # 3にとての前は2
            curnode = nextnode  # 次は3を探索する
        return prevnode